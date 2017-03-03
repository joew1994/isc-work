#!/usr/bin/python2.7

import serial, io
from datetime import datetime

ser = serial.Serial(
    port ='/dev/ttyUSB0',
    baudrate=9600,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE
)

sio = io.TextIOWrapper(
    io.BufferedRWPair(ser, ser, 1),
    encoding='ascii', newline='\r'
)

outfile='temperature.log'

#"8" here is specific to the Papouch thermometer device
with open(outfile, 'a') as f: #appends to existing file
    while ser.isOpen():
        datastring = sio.readline()
        #\t is tab; \n is line separator
        f.write(datetime.utcnow().isoformat() + '\t' + datastring + '\n')
        f.flush() #included to force system to write to disk

print datetime.utcnow().isoformat(), datastring
ser.close()



