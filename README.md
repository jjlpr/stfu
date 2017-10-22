# STFU

## Requirements

Python 3 or greater required.

To run the packages in `requirements/base.txt` will need to be installed. If
you have `virtualenv` installed then you can use the recipes in the `Makefile`:

    make install


## Execution

    venv/bin/python -m stfu [wav file]

Where `wav file` is the fully qualified path to the wav file. Usually `wav
file` will be named with "the epoc time in milliseconds dot wav"
