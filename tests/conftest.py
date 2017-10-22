import pytest


@pytest.fixture
def quiet_wav_file():
    import os
    return os.path.join(os.path.dirname(__file__), 'data', '1508673476734.wav')
