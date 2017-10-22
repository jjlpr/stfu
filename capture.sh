#!/bin/bash

set -eo pipefail

now=$(date +%s%3N)
wav_filename="soundfiles/$now.wav"

arecord --device=hw:1,0 -f S16_LE -d 1 "$wav_filename"
venv/bin/python -m stfu "$wav_filename" >> output.json
