# cs372_project1

Description:

Using a socket to GET a file
How do internet browsers work? They all manage networking “sockets” to contact a web 
server and download HTML files and resources. In this part you will make a bare-bones
socket program to do some of what your internet browser does.

Create a simple python program that uses a socket to interact with a server. Note that 
your program MUST USE THE PYTHON SOCKET API. Yes, it is possible to do this in 
one line of code with Python Requests or some other library. But that wouldn’t be any 
fun, would it?


Your program shall make a socket connection to the host: “gaia.cs.umass.edu” and send 
the GET request for the URI: “/wireshark-labs/INTRO-wireshark-file1.html”. To do this, you will 
send the following HTTP-compliant GET request to the server exactly as shown:
"GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n”
Note: If you are interested in the specification of an HTTP request, see: 
https://www.w3.org/Protocols/rfc2616/rfc2616
https://www.w3.org/Protocols/rfc2616/rfc2616-sec5.html#sec5.1.2
Run your program and receive a response from the server. 

GET the data for a large file
Your first program was probably written with a single read or recv command. This works 
fine for very small files, but would not be able to download anything larger. For this next 
part, you will write a socket program to receive arbitrarily large files. 
Your program will make a socket connection to the host: “gaia.cs.umass.edu” and send the 
GET request for the URI: “/wireshark-labs/HTTP-wireshark-file3.html”. To do this, you will send 
the following HTTP-compliant GET request to the server exactly as below:
"GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
There is no end-of-transmission (EOT) with sockets, so knowing when you’ve received 
all the data can be difficult. Fortunately for this project, the gaia.cs.umass.edu server will 
close the connection after sending its data, so the easy thing to do is detect when recv 
or read return <= 0 bytes in a loop.
Run your program.

The world’s simplest HTTP server
Now you’re going to create an HTTP server using the python socket api. Your program 
will create a listening socket bound to ‘127.0.0.1’ or ‘localhost’, and a random port
number > 1023. You will then use your web browser to connect to your server and 
receive data. Note that your server could be running on any host within your LAN (as 
long as there’s no firewall that can block access to it).
If you are interested in the choice of IP address, here is a deep-dive explanation. The 
short explanation, is that this is the local machine loopback address, so that you can 
have both client and server running locally and communicating.
When your socket accepts a request, a new socket is created. Read the socket request on the new 
socket and print it. Then send the following html data on the new socket and close it.
 data = "HTTP/1.1 200 OK\r\n"\
 "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
 "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"
Run your program (http_server.py). Start up your web browser and navigate to 
127.0.0.1:xxxx (where xxxx is the port you specified in your server).
