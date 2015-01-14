import serial, time

upstreamName = '/dev/ttyO2'
downstreamName = '/dev/ttyO1'
serialConfig = {
        'baudrate': 38400,
        'bytesize': serial.EIGHTBITS,
        'parity': serial.PARITY_NONE,
        'stopbits': serial.STOPBITS_ONE,
        'timeout': 1
        }
upstream = serial.Serial(upstreamName, **serialConfig)
downstream = serial.Serial(downstreamName, **serialConfig)

def printByteCount(c, direction):
    if c > 0:
        print("wrote "+ str(c) +" bytes "+direction)


while upstream.isOpen() and downstream.isOpen():
    upstream.setDTR(True)
    ds = downstream.write(upstream.read())
    us = upstream.write(downstream.read())
    printByteCount(ds, 'downstream')
    printByteCount(us, 'upstream')
