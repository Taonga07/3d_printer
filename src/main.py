from socket import socket, AF_INET, SOCK_STREAM
from json import loads, dumps


address: tuple(str, int) = ("octopi.local", 5000)

def http_requst():
    request: str = b"GET / HTTP/1.1\r\nHost:www.example.com\r\n\r\n"


"https://www.internalpointers.com/post/making-http-requests-sockets-python"
"https://marlinfw.org/docs/gcode/G092.html"
"https://docs.octoprint.org/en/master/api/printer.html#send-an-arbitrary-command-to-the-printer"


if __name__ =="__main__":
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(address)