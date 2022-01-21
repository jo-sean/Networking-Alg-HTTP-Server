# Name: Sean Perez
# Date: 1/20/2022
# CS 372: Project 1 Part 1
# Sources: Computer Networking A Top-Down Approach Ch. 2.7
# Adrian Hing and Shane Yen: https://edstem.org/us/courses/16852/discussion/1006512

from socket import *
# Variables for host and port# (which is 80 since it is an HTTP request)
serverName = 'gaia.cs.umass.edu'
serverPort = 80

# Open connection to server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# GET request and Host
sentence = "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

# Encodes into bytes and sends
clientSocket.send(sentence.encode())

# Receive bytes from server
html_string = ""                                    # Will hold the complete message
while 1:
    modifiedSentence = clientSocket.recv(1024)

    # Once server has nothing more to send, breaks
    if modifiedSentence <= bytes(0):
        break

    # Decodes bytes and appends html string together
    html_string = html_string + modifiedSentence.decode()


# Print appended string
print('From Server: ', html_string)

# Connection closed
clientSocket.close()
