import socket
import OpenSSL

#OpenSSL.SSL.SSLeay_version(OpenSSL.SSL.SSLEAY_VERSION)

ctx = OpenSSL.SSL.Context(OpenSSL.SSL.SSLv23_METHOD)
sock = socket.socket()
ssock = OpenSSL.SSL.Connection(ctx, sock)

connect = ssock.connect_ex(('www.ssllabs.com', 443))
if connect != 0:
    print connect

getHost = ssock.send('GET /ssltest/viewMyClient.html HTTP/1.1\r\nHost: www.ssllabs.com\r\n\r\n')
if getHost != 66:
    print getHost

print ssock.recv(16384)
print ssock.recv(16384)
print ssock.recv(16384)
print ssock.recv(16384)
d = ssock.recv(16384)
print d
#print d.find('TLS 1.1')
#print d.find('TLS 1.0')

#d[2324:2432]
