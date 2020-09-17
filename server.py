# first of all import the socket library 
import socket   

# next create a socket object 
s = socket.socket()         

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print ('Socket successfully created')
except socket.error as err: 
    print ('socket creation failed with error %s' %(err)) 
    
    
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345 

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print ('socket binded to %s' %(port)) 

# put the socket into listening mode 
s.listen(5)      
print ('socket is listening')  

# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
    # Establish connection with client. 
    conn, addr = s.accept()      
    print ('Got connection from', addr) 
    data = conn.recv(4096)
    print(str(data, 'utf-8'))
  
    # send a thank you message to the client.  
    conn.send('Thank you for connecting'.encode()) 

    # Close the connection with the client 
    conn.close() 


# First of all we import socket which is necessary.
# Then we made a socket object and reserved a port on our pc.
# After that we binded our server to the specified port. 
# Passing an empty string means that the server can listen to incoming connections from other computers as well.
# If we would have passed 127.0.0.1 then it would have listened to only those calls made within the local computer.
# After that we put the server into listen mode.
# 5 here means that 5 connections are kept waiting if the server is busy and if a 6th socket trys to connect then the connection is refused.
# At last we make a while loop and start to accept all incoming connections and close those connections after a thank you message to all connected sockets.
