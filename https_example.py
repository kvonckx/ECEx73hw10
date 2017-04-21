# Ken Vonckx
import socket, ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_default_certs()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(s, server_hostname='help.github.com')

try:
    ssl_sock.connect(('help.github.com', 443))
    ssl_sock.settimeout(1.0)
    ssl_sock.sendall("GET /page/SDU46 HTTP/1.1\r\nHostname: www.u-46.org\r\n\r\n")
    while 1:
        try:
            data = ssl_sock.recv(2048).strip()
            print data
        except:
            break
except:
    print "Socket connection error!"
finally:
    ssl_sock.close()
