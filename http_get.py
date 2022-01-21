# Name: Sean Perez
# Date: 1/20/2022
# CS 372: Project 1 Part 1
# Sources: TA - Alotaibi, Mazen Nasser A and Computer Networking A Top-Down Approach Ch. 2.7


from socket import *
# Variables for host and port# (which is 80 since it is an HTTP request)
serverName = 'gaia.cs.umass.edu'
serverPort = 80

# Open connection to server
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# GET request and Host
sentence = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"

# Encodes into bytes and sends
clientSocket.send(sentence.encode())

# Receive bytes from server
modifiedSentence = clientSocket.recv(1024)

# Print decoded html data
print('From Server: ', modifiedSentence.decode())

# Connection closed
clientSocket.close()
