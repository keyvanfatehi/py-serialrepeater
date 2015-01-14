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
  if ( length <= 0 ): return False
  print("repeating "+str(length)+" bytes from "+fromLabel+" into "+toLabel)
  if ( length < 50 ):
    # it's short, it's probably just control codes
    # let's print them as hex for later analysis
    # q1: is it always the same?
    hexstr = ':'.join(x.encode('hex') for x in data)
    print(hexstr)
    toPort.write(data)
  else:
    # this is probably the payload! let's fuck with it
    print("inserting our own shit!")
    toPort.write("There are no rules here -- we're trying to accomplish something.\n\t-- Thomas Edison")
    toPort.write(data)


print("Go for it")
while upstream.isOpen() and downstream.isOpen():
  repeat('pc', upstream, 'printer', downstream)
  repeat('printer', downstream, 'pc', upstream)
