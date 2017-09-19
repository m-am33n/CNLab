import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12332               # Reserve a port for your service.
flag=1
s.connect((host, port))
print s.recv(1024)
print "Enter reply:"
while True:
	m=raw_input()
	s.send("C:"+m)
	k=s.recv(1024)
	print k		
s.close           
