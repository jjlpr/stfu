from stfu.wavalysis import wav_to_stats


def test_quiet(quiet_wav_file):
    """
    1508673476734 is a quiet file recorded off the audio card with no input
    """
    result = wav_to_stats(quiet_wav_file)

    assert result == (2, 10)
