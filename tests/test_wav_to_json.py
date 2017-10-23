import json

from stfu.wavalysis import wav_to_json


def test(quiet_wav_file):
    result = wav_to_json(quiet_wav_file)

    try:
        data = json.loads(result)
    except json.JSONDecodeError:
        raise AssertionError('data is not JSON. data was {}'.format(result))
    assert set(data) == set(('time', 'htime', 'av', 'max'))
    assert data['time'] == 1508673476734
    assert data['htime'] == '2017-10-22 11:57:56.734000'
    assert data['av'] == 2
    assert data['max'] == 10
