import socket
s=socket.socket()
host=socket.gethostname()
d={}
port=23455
s.bind((host,port))
s.listen(5)
c, addr = s.accept()     
print 'Got connection from', addr
c.send('Thank you for connecting')                
while True:
   k=c.recv(1024)
   l=k.split()
   if(l[0]=='push'):
   		key=int(l[1])
   		val=int(l[2])
   		if d.has_key(key):
   			c.send('Key already exists')
   		else:
   			d[key]=val
   			c.send('Key added!')
   elif(l[0]=='pop'):
   		if d.has_key(int(l[1])):
   			m=d[int(l[1])]
   			c.send("Key: "+str(m))
   		else:
   			c.send("Key doesn't exist!")
   elif(l[0]=='del'):
   		if d.has_key(int(l[1])):
   			m=d[int(l[1])]
   			del d[m]
   			c.send("Deleted key: "+str(m))
   		else:
   			c.send("Key doesn't exist!")
   		

