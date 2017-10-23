import datetime
import os

import numpy

from .wavfile import read as wavfile_read


def wav_to_stats(wav_file):
    """
    Args:
        wav_file (str): fully qualified location of the wav file to be
            analysed.

    Returns:
        tuple (int, int): Average and max absolute volumes returned from the
            wav file.
    """
    data = wavfile_read(wav_file)[1]
    data = numpy.absolute(data)

    return int(numpy.round(numpy.average(data))), data.max()


def wav_to_json(wav_file):
    """
    Args:
        wav_file (str): fully qualified location of the wav file to be
            analysed.

    Returns:
        str: json data from analysis.
    """
    wav_av, wav_max = wav_to_stats(wav_file)
    wav_filename = os.path.split(wav_file)[-1]
    time_str = wav_filename.split('.')[0]
    human_time = datetime.datetime.utcfromtimestamp(int(time_str)/1000)
    return '{' + '"time":{},"htime":"{}","av":{},"max":{}'.format(time_str, human_time, wav_av, wav_max) + '}'
