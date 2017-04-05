import matplotlib.pyplot as plt
import serial
import numpy
from drawnow import *

afrData = []
dataStream = serial.Serial('COM3',115200)
plt.ion()
counter = 0

def liveData():
    plt.ylim(9,21)
    plt.xlim(0,50)
    plt.ylabel("AFR")
    plt.plot(afrData)

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
