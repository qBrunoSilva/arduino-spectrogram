import pyaudio
import numpy as np

import pyaudio
import matplotlib.pyplot as plt

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 15
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK,
)

print("* Plotting")

plt.ion()
plt.show()
plt.title("Spectrogram")

while True:
    data = stream.read(CHUNK, exception_on_overflow=False)
    sig = np.frombuffer(data, dtype='<i2').reshape(-1, CHANNELS)

    plt.plot(sig)
    plt.draw()
    plt.pause(0.0001)
    plt.clf()
