import serial
import win32com.client

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
    sep = data.split("\t")
    print(sep)
