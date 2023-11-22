import zmq
from constPS import * #-

context = zmq.Context()
s = context.socket(zmq.SUB)          # create a subscriber socket
p = "tcp://"+ HOST2 +":"+ PORT        # how and where to communicate
s.connect(p)                         # connect to the server
s.setsockopt_string(zmq.SUBSCRIBE, "ROLETA")  # subscribe to ROLETA messages
s.setsockopt_string(zmq.SUBSCRIBE, "NAIPE")  # subscribe to ROLETA messages

for i in range(5):  # Five iterations
	time = s.recv()   # receive a message
	print (bytes.decode(time))
