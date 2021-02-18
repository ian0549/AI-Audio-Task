import os

from preprocessor.Preprocessor import Pipeline

import pytest
import numpy as np
import librosa

@pytest.fixture(scope='module')
def pipeline():
    print('------------------setup-------------------')



    pipeline = Pipeline(dataset_path='music_dataset',
                        output_path='output',
                        sample_rate=22050,
                        mel_bands=10,
                        n_mfcc=10,
                        hop_length=512)

    yield pipeline
    print('------------------teardown-------------------')
    pipeline.loader.cache_clear()


@pytest.fixture(scope='module')
def loaded_signals(pipeline):

    signal = pipeline.loader()

    return signal


def test_loader(pipeline,loaded_signals):
    """
    Test that it can load audio files

    """
 


    expected_signal = []
    path, dirs, files = next(os.walk(pipeline["dataset_path"]))

    file_count = len(files)

    for f in files:

        file_path = os.path.join(path, f)

        loaded_audio_signal, _ = librosa.load(file_path, sr=pipeline["sample_rate"])
        expected_signal.append(loaded_audio_signal)

    actual_signal = loaded_signals

    assert actual_signal != []
    for i in range(file_count):
        assert np.allclose(actual_signal[i], expected_signal[i])


def test_mfccs(pipeline, loaded_signals):
    """
    Test that it can extract mfccs from audio signals
    """
 

    path, dirs, files = next(os.walk(pipeline["dataset_path"]))

    file_count = len(files)

    mfcc = pipeline.extract_mfccs(loaded_signals)

    for i in range(file_count):
        assert mfcc[i].shape[0] == pipeline["n_mfcc"]


def test_mel_spectrogram(pipeline, loaded_signals):
    """
    Test that it can extract mel spectrogram from audio signals
    """

   
    path, dirs, files = next(os.walk(pipeline["dataset_path"]))
    file_count = len(files)

    mel_spectorgram = pipeline.extract_mel_spectrogram(loaded_signals)

    for i in range(file_count - 1):
        assert mel_spectorgram[i].shape[0] == pipeline["mel_bands"]


def test_save_mfccs(pipeline, loaded_signals):
    """
    Test that it can save extracted save_mfccs as numpy array
    """

    # now load the features and check if it is loaded correctly
    path, dirs, files = next(os.walk(pipeline.output_path))

    mfccs = pipeline.extract_mfccs(loaded_signals)

    pipeline.save_features(mfccs, "mfccs")

    # now load the features and check if it is loaded correctly
    path, dirs, files = next(os.walk(pipeline["output_path"]))



    for f in files:

        if "mfccs" in str(f):

            file_path = os.path.join(path, f)

            # load array
            data = np.load(file_path)
            assert data.shape[0] == pipeline["n_mfcc"]


def test_save_mel_spectrograms(pipeline, loaded_signals):
    """
    Test that it can save extracted mel_spectrograms as numpy array
    """
    mel_spectrogram = pipeline.extract_mel_spectrogram(loaded_signals)

    pipeline.save_features(mel_spectrogram, "melspectrograms")

    # now load the features and check if it is loaded correctly
    path, dirs, files = next(os.walk(pipeline["output_path"]))

    for f in files:

        if "mel_spectrogram" in str(f):

            file_path = os.path.join(path, f)

            # load array
            data = np.load(file_path)
            assert data.shape[0] == pipeline["mel_bands"]