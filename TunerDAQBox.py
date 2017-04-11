import matplotlib.pyplot as plt
import serial
import numpy
from drawnow import *

afrData = []
dataStream = serial.Serial('COM3',115200)
plt.ion()
counter = 0

def liveData():
    plt.figure(1)
    plt.subplot(211)
    plt.ylim(9,21)
    plt.xlim(0,50)
    plt.ylabel("AFR")
    plt.plot(afrData)

    '''
    plt.subplot(212)
    plt.ylim(10000,-10000)
    plt.xlim(0,2000)
    plt.ylabel("RPM")
    plt.plot() RPM

    plt.subplot(213)
    plt.ylim(10000,-10000)
    plt.xlim(0,2000)
    plt.ylabel("Speed")
    plt.plot() Speed
    '''

while True:
    #while(dataStream.inWaiting()==0):
    #    pass
    
    dataContent = dataStream.readline()
    dataArray = dataContent.decode('utf-8').split(',')
    rawAFR = float(dataArray[0])
    afrData.append(rawAFR)
    drawnow(liveData)
    plt.pause(0.000001)
    counter = counter+1
    
    if(counter>50):
        afrData.pop(0)
