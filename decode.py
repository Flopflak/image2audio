# decode.py
from PIL import Image
from scipy.io import wavfile
import numpy as np

SIZE_MULTIPLAYER = 10
MAX_W = 1024 * SIZE_MULTIPLAYER
MAX_H = 1024 * SIZE_MULTIPLAYER
SAMPLE_RATE = 44100
SAMPLES_PER_VALUE = 1

def unpack_grayscale(normalized):
    g = int(normalized * 255.0)
    return g, g, g  # return grayscale as RGB for compatibility with PIL

def reconstruct_image(data_list, image_path):
    width, height = data_list[0], data_list[1]
    width = int(width * MAX_W)
    height = int(height * MAX_H)
    unpacked_pixels = [unpack_grayscale(p) for p in data_list[2:]]
    img = Image.new('RGB', (width, height))
    img.putdata(unpacked_pixels)
    img.save(image_path)

def wav_to_data(filename, max_amplitude=32767):
    sample_rate, audio_data = wavfile.read(filename)
    data = np.mean(audio_data.reshape(-1, SAMPLES_PER_VALUE), axis=1)
    data = (data.astype(np.float32) + max_amplitude) / (2 * max_amplitude)
    data = np.clip(data, 0, 1)  # Ensuring data doesn't exceed the [0,1] range
    return data.tolist()


data_from_wav = wav_to_data('audio_output.wav')
reconstruct_image(data_from_wav, 'reconstructed_image.png')
