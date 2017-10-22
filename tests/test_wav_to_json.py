import json

from stfu.wavalysis import wav_to_json


def test(quiet_wav_file):
    result = wav_to_json(quiet_wav_file)

    data = json.loads(result)
    assert set(data) == set(('time', 'av', 'max'))
    assert data['time'] == 1508673476734
    assert data['av'] == 2
    assert data['max'] == 10
