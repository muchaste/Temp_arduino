import serial
import matplotlib.pyplot as plt
import numpy as np
import win32com.client

connected = False

# finds COM port that the Arduino is on (assumes only one Arduino is connected)
wmi = win32com.client.GetObject("winmgmts:")
for port in wmi.InstancesOf("Win32_SerialPort"):
# print port.Name #port.DeviceID, port.Name
    if "Arduino" in port.Name:
        comPort = port.DeviceID
        print
        comPort, "is Arduino"

ser = serial.Serial(comPort, 9600)  # sets up serial connection (make sure baud rate is correct - matches Arduino)

while not connected:
    serin = ser.read()
    connected = True

plt.ion()  # sets plot to animation mode

length = 500  # determines length of data taking session (in data points)
x = [0] * length  # create empty variable of length of test
y = [0] * length

xline, = plt.plot(x)  # sets up future lines to be modified
yline, = plt.plot(y)
plt.ylim(0, 100)  # sets the y axis limits

for i in range(length):  # while you are taking data
    data = ser.readline()  # reads until it gets a carriage return. MAKE SURE THERE IS A CARRIAGE RETURN OR IT READS FOREVER
    sep = data.split()  # splits string into a list at the tabs
    # print sep

    x.append(int(sep[0]))  # add new value as int to current list
    y.append(int(sep[1]))

    del x[0]
    del y[0]

    xline.set_xdata(np.arange(len(x)))  # sets xdata to new list length
    yline.set_xdata(np.arange(len(y)))

    xline.set_ydata(x)  # sets ydata to new list
    yline.set_ydata(y)

    plt.pause(0.001)  # in seconds
    plt.draw()  # draws new plot

rows = zip(x, y)  # combines lists together

row_arr = np.array(rows)  # creates array from list
np.savetxt("C:\\Users\\Stefan Mucha\\Dropbox\\Uni backup\\Uni\\Promotion\\Arduino Code\\Temp_arduino\\Python_temp_readout\\test.txt",
           row_arr)  # save data in file (load w/np.loadtxt())

ser.close()  # closes serial connection (very important to do this! if you have an error partway through the code, type this into the cmd line to close the connection)