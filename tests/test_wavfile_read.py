from stfu.wavfile import read


def test(quiet_wav_file):
    result = read(quiet_wav_file)

    assert len(result) == 2
    assert result[0] == 44100
    assert result[1][0] == 1
    assert result[1][1] == 3
    assert result[1][2] == 1
