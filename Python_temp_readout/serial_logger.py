import serial
import win32com.client
import datetime
import numpy as np
import matplotlib.pyplot as plt

DO = [0] #hold DO values
Temp = [0] #hold temperature values

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

while True:
    data = ser.readline()  # read until it gets a carriage return
    data = data.decode().strip("\r\n") #strip serial read from carriage return
    sep = data.split("\t") #make list from serial read, split by tab
    DO.append(sep[0]) #add DO value
    Temp.append(sep[1]) #add Temp value
    del(DO[0]) #delete old DO value
    del(Temp[0]) #delete old temperature value
    rows = zip(DO, Temp)  # combine the lists
    row_arr = np.array(rows)  # create array from list
#    np.savetxt("C:\\Users\\Stefan Mucha\\Dropbox\\Uni backup\\Uni\\Promotion\\Arduino Code\\Temp_arduino", str(datetime.date.today()))  # save data in file
    print(DO)
    print(Temp)
