# encode.py
from PIL import Image
import numpy as np
from scipy.io import wavfile

SIZE_MULTIPLAYER = 10
MAX_W = 1024 * SIZE_MULTIPLAYER
MAX_H = 1024 * SIZE_MULTIPLAYER
ROUNDING_PRECISION = 6  # Modify as needed
SAMPLE_RATE = 44100
SAMPLES_PER_VALUE = 1

def pack_grayscale(g):
    normalized = g / 255.0
    return round(normalized, ROUNDING_PRECISION)

def image_to_list(image_path):
    with Image.open(image_path) as img:
        img = img.convert("L")
        img.thumbnail((MAX_W, MAX_H))
        width, height = img.size
        pixels = list(img.getdata())
        packed_pixels = [pack_grayscale(g) for g in pixels]
        width = width / MAX_W
        height = height / MAX_H
        return [width, height] + packed_pixels

def data_to_wav(data, filename, sample_rate=SAMPLE_RATE, max_amplitude=32767):
    audio_data = np.repeat(data, SAMPLES_PER_VALUE)
    audio_data = audio_data * 2 * max_amplitude - max_amplitude
    audio_data = audio_data.astype(np.int16)
    wavfile.write(filename, sample_rate, audio_data)

image_list = image_to_list('image.png')
data_to_wav(image_list, 'audio_output.wav')
