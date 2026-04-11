#!/bin/bash

# Controllo se è stato fornito un file in input
if [ -z "$1" ]; then
    echo "Errore: Devi trascinare un file mp4 sullo script o passarlo come argomento."
    echo "Utilizzo: ./process_lecture.sh nome_video.mp4"
    exit 1
fi

INPUT_FILE="$1"
# Ottengo il nome base senza estensione (es: "Lezione_1")
FILENAME=$(basename "$INPUT_FILE")
BASENAME="${FILENAME%.*}"

echo "--- Inizio elaborazione di: $BASENAME ---"

# 1. Creazione della cartella dedicata
mkdir -p "$BASENAME"

# 2. Conversione e Splitting in un unico comando
# -vn: Rimuove il video
# -f segment: Attiva la modalità divisione
# -segment_time 1800: Imposta pezzi da 30 minuti (1800 secondi)
# -c:a copy: Copia l'audio originale senza ricodificare (velocissimo!)
ffmpeg -i "$INPUT_FILE" -vn -f segment -segment_time 1800 -c:a copy "$BASENAME/${BASENAME}_part%03d.m4a"

echo "--- Completato! ---"
echo "I file si trovano nella cartella: ./$BASENAME/"
