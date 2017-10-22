from stfu.wavalysis import wav_to_json


def test():
    result = wav_to_json('')

    assert result == ''
