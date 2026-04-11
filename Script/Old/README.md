# Legacy Transcription Pipeline

This directory contains the legacy shell scripts (e.g., `00_Old_Script.sh`) previously used for processing lecture videos.

## Old Workflow Overview
Previously, lecture videos were processed manually by:
1. Running `00_Old_Script.sh` (or `script.sh`) to split a large `.mp4` video into 30-minute `.m4a` audio segments using `ffmpeg`.
2. Uploading these segments manually to TurboScribe AI online using an Incognito mode workaround to evade rate limits.
3. Downloading the transcriptions and manually concatenating them, while removing the TurboScribe watermarks.

## Current Workflow
This manual process has been completely deprecated in favor of a fully local, automated AI pipeline. 
The new process is handled by `../Transcription/01_AI_Model_Script.py`, which directly downloads videos and uses the `faster_whisper` large-v3-turbo model on the GPU to transcribe files automatically, saving the final text directly into the `../../Notes/Lectures_txt` folder.
