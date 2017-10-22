from stfu.wavalysis import wav_to_stats

import os


def test_quiet():
    """
    1508673476734 is a quiet file recorded off the audio card with no input
    """
    quiet_file = os.path.join(os.path.dirname(__file__), 'data', '1508673476734.wav')

    result = wav_to_stats(quiet_file)

    assert result == (2, 10)
