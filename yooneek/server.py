import zmq
import sys

from key import generator


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

counter = 0

while True:
    message = socket.recv()

    key = generator.key()
    key = str(key)

    socket.send(key)
