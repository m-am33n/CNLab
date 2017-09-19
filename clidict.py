import socket               

s = socket.socket()        
host = socket.gethostname() 
port = 23455               
flag=1
s.connect((host, port))
print s.recv(1024)
print "Enter request:"
while True:
	m=raw_input()
	s.send(m)
	k=s.recv(1024)
	print k		
s.close      
