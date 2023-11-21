import zmq, time
import random
from constPS import * #-

def roleta():
	if (random.randint(1,6)==3):
		msg = "bang! morestes"
	else: 
		msg = "esta salvo!"
	return msg

context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp:// 0.0.0.0:" + PORT      # how and where to communicate
s.bind(p)                          # bind socket to the address
while True:
	time.sleep(5)                    # wait every 5 seconds
	msg = str.encode("ROLETA " + roleta())
		
	s.send(msg) # publish the current time
	
