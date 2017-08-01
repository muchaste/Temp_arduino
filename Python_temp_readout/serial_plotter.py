import serial
import win32com.client
import numpy as np
import matplotlib.pyplot as plt

connected = False #Boolean to represent whether Arduino is connected or not

wmi = win32com.client.GetObject("winmgmts:") #Find com port where Arduino is connected
for port in wmi.InstancesOf("Win32_SerialPort"):
    if "Arduino" in port.Name:
        comPort = port.DeviceID
        print(comPort, "is Arduino")

ser = serial.Serial(comPort, 9600) #Read the com-port where the Arduino is connected

while not connected: #Loop until the Arduino tells us it's ready
    serin = ser.read()
    connected = True

plt.ion() #Set plot to animation mode

#length = 500
DO = [0]#*length #hold DO values
Temp = [0]#*length #hold temperature values

DOLine = plt.plot(DO) #Set up lines to be modified
TempLine = plt.plot(Temp)
plt.ylim(0, 120)

while True:
    data = ser.readline()  # read until it gets a carriage return
    data = data.decode().strip("\r\n") #strip serial read from carriage return
    sep = data.split("\t") #make list from serial read, split by tab

    DO.append(sep[0]) #add DO value
    Temp.append(sep[1]) #add Temp value

    del(DO[0]) #delete old DO value
    del(Temp[0]) #delete old temperature value

    DOLine.set_xdata(np.arange(500))  # Set xdata to new list length
    TempLine.set_xdata(np.arange(500))

    DOLine.set_ydata(DO)  # Set ydata to new value
    TempLine.set_ydata(Temp)

    plt.pause(0.1)
    plt.draw()







