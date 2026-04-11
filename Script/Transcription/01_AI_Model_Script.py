import sys
import os
import json
import urllib.request
import threading
import queue
from faster_whisper import WhisperModel
from tqdm import tqdm

# Helper class to connect urllib to the tqdm progress bar
class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_video(url, output_path):
    try:
        with DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc="Download Progress") as t:
            urllib.request.urlretrieve(url, output_path, reporthook=t.update_to)
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def download_worker(download_queue, ready_queue):
    while True:
        item = download_queue.get()
        if item is None:
            ready_queue.put(None) # Signal completion
            break
        
        index, url, filename = item
        temp_video = os.path.join(os.path.dirname(__file__), "MP4", f"temp_lecture_{index}.mp4")
        
        print(f"\n[Downloader] Starting download for: {filename}")
        success = download_video(url, temp_video)
        
        if success:
            ready_queue.put((index, temp_video, filename))
        else:
            ready_queue.put((index, None, filename))
            
        download_queue.task_done()

def main():
    # Setup paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "data.json")
    mp4_dir = os.path.join(base_dir, "MP4")
    
    # Destination in the repository structure
    output_dir = os.path.abspath(os.path.join(base_dir, "..", "..", "Notes", "Lectures_txt"))
    os.makedirs(mp4_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(json_path):
        print(f"Error: Configuration file not found at {json_path}")
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    lecture_urls = data.get("Lecture_URLs", [])
    file_names = data.get("File_Names", [])

    if len(lecture_urls) != len(file_names):
        print("Error: 'Lecture_URLs' and 'File_Names' in data.json must have the same length.")
        sys.exit(1)

    if not lecture_urls:
        print("Warning: No URLs found in data.json to process.")
        sys.exit(0)

    # --- Initialize Model ---
    print("Loading AI Model (large-v3-turbo) on GPU...")
    # Using float16 and cuda for optimized GPU execution
    model = WhisperModel("large-v3-turbo", device="cuda", compute_type="float16")

    # --- Set Up Queues ---
    download_queue = queue.Queue()
    ready_queue = queue.Queue()

    for i, (url, fname) in enumerate(zip(lecture_urls, file_names)):
        download_queue.put((i, url, fname))
    
    # Sentinel value to stop the worker
    download_queue.put(None)

    # Start background download thread
    t = threading.Thread(target=download_worker, args=(download_queue, ready_queue))
    t.start()

    print(f"\nStarting pipeline for {len(lecture_urls)} video(s).")
    total_tasks = len(lecture_urls)
    completed_tasks = 0

    while completed_tasks < total_tasks:
        result = ready_queue.get()
        if result is None:
            break # Thread finished
            
        index, temp_video, filename = result
        
        if temp_video is None:
            print(f"Skipping transcription for {filename} due to download error.")
            completed_tasks += 1
            continue

        output_file = os.path.join(output_dir, filename)
        
        # --- Transcribe Audio ---
        print(f"\n[Transcriber] Processing: {filename}")
        print("Estimating initial duration...")
        
        # vad_filter=True prevents memory crashes on long files
        segments, info = model.transcribe(temp_video, vad_filter=True)
        total_duration = round(info.duration, 2)

        # Set up the transcription progress bar based on the total audio seconds
        with open(output_file, "w", encoding="utf-8") as f:
            with tqdm(total=total_duration, unit=" audio sec", desc="Transcription Progress") as pbar:
                
                paragraph_text = ""
                paragraph_start = 0.0

                for segment in segments:
                    # Accumulate the text, cleaning up any weird spacing
                    paragraph_text += segment.text.strip() + " "

                    # Group into big 60-second chunks, but ensure we only break at sentence boundaries
                    if (segment.end - paragraph_start >= 60.0) and paragraph_text.strip().endswith(('.', '?', '!')):
                        f.write(f"{paragraph_text.strip()}\n\n")
                        paragraph_text = ""
                        paragraph_start = segment.end

                    # Update the progress bar
                    pbar.n = round(segment.end, 2)
                    pbar.refresh()

                # Catch any leftover text at the end of the video
                if paragraph_text:
                    f.write(f"{paragraph_text.strip()}\n")

        print(f"Success! Token-optimized transcript saved to: {output_file}")

        # --- Clean up ---
        if os.path.exists(temp_video):
            os.remove(temp_video)
            print(f"Cleaned up temporary video: {os.path.basename(temp_video)}")

        completed_tasks += 1

    t.join()
    print("\nAll lectures processed successfully.")

if __name__ == "__main__":
    main()