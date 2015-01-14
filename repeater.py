import serial, time

upstreamName = '/dev/ttyO2'
downstreamName = '/dev/ttyO1'
serialConfig = {
    'baudrate': 38400,
    'bytesize': serial.EIGHTBITS,
    'parity': serial.PARITY_NONE,
    'stopbits': serial.STOPBITS_ONE,
    'timeout': 0.1
    }
upstream = serial.Serial(upstreamName, **serialConfig)
downstream = serial.Serial(downstreamName, **serialConfig)

def repeat(fromLabel, fromPort, toLabel, toPort):
  data = fromPort.readall()
  length = len(data)
  if ( length > 0 ):
    print("repeating "+str(length)+" bytes from "+fromLabel+" into "+toLabel)
    hexstr = ':'.join(x.encode('hex') for x in data)
    print(hexstr)
    toPort.write(data);


while upstream.isOpen() and downstream.isOpen():
  repeat('pc', upstream, 'printer', downstream)
  repeat('printer', downstream, 'pc', upstream)
