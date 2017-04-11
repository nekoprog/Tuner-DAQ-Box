import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from drawnow import *

RATE = 44100
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2

plt.ion()
p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

def liveData():
    plt.figure(1)
    plt.subplot(211)
    plt.xlim(0,(CHUNK*2))
    plt.ylim(-8000,8000) #change this value to zoom in/out
    plt.plot(data)

while True:
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    drawnow(liveData)
    #print(data) #For debug only
    plt.pause(0.000001)
  
stream.stop_stream()
stream.close()
p.terminate()
