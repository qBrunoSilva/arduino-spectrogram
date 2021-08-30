import pyaudio
import numpy as np
import serial
import pyaudio

from math import ceil

port = "COM3"
bound = 9600

uno = serial.Serial(port, bound)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()


stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK,
)

print("* Started")

while True:
    data = stream.read(CHUNK, exception_on_overflow=False)
    sig = np.frombuffer(data, dtype='<i2').reshape(-1, CHANNELS)

    num = sig[0][0]

    if num < 0:
        num *= -1

    num = ceil(num / 10)

    if num < 1500:
        num = 10
    elif num > 1500 and num < 2000:
        num = 25
    elif num > 2000 and num < 3500:
        num = 35

    elif num > 3500 and num < 5500:
        num = 45

    elif num > 5500 and num < 6500:
        num = 50
    elif num > 6500 and num < 7000:
        num = 65

    elif num > 7000:
        num = 80
    else:
        num = 0

    uno.write('B\n'.encode())
    uno.write(f'{num}\n'.encode())
    uno.write('R\n'.encode())
    uno.write(f'{num}\n'.encode())
    uno.write('G\n'.encode())
    uno.write(f'{num}\n'.encode())
