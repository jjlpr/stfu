#!/bin/bash

set -eo pipefail

now=$(date +%s%3N)
wav_filename="soundfiles/$now.wav"

arecord --disable-softvol --device=hw:1,0 -f S16_LE -d 60 "$wav_filename"
venv/bin/python -m stfu "$wav_filename" >> output.json
