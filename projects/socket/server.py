import socket

s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
print "Socket Server"
print "[host]", host
print "[port]", port
while True:
    c, addr = s.accept()
    print "Got connection from ", addr
    c.send("Thank you for connecting.")
    c.close()
