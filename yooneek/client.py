import zmq
import time
import sys

context = zmq.Context()

socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")
x = 1

while True:
    socket.send("key")
    message = socket.recv()
    # sys.stdout.write("{0}  Key: {1}\n".format(x, message))
    x += 1
    if not x % 1000:
        print x
        # sys.stdout.flush()
    time.sleep(0.001)
