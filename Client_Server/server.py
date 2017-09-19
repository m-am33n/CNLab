import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12332               # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
flag=0
s.listen(5)
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
c.send('Thank you for connecting')                 # Now wait for client connection.
while True:
   k=c.recv(1024)
   print k
   m=raw_input()
   c.send("S:"+m)
			
       
c.close()                # Close the connection
