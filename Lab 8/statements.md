# Lab 8

1.  
	- Implement using the socket module (TCP), a server that writes when a client connects to it the following data: the connection time in human-readable format, the address, and the port of the client.
	- Implement a client for the server developed at 1a: a script that receives from the command line a string addr and an integer port and connects through TCP to the addr address at the port port.
2.  
	- Implement using the socket module (UDP), a server that when is receiving a UDP packet (datagram) writes in a text file the following information: time and date, address, port, length, md5 hash of the content in hex format, sha256.
	- Implement a client for the server developed at 2a: a script that receives from the command line an addr string, a port integer, and a string msg, and sends a UDP packet to the addr address, the port port, and the msg content.
3. Start a server to expose the files and directories in the current directory. Access that server from a browser, and then using a python HTTP client (urllib.request)
4. Once the server from 3 is started, extract the .txt file names and write to the console.
5. Write a script that receives a URL from the command line (as an argument) and downloads all images (img src) to the current directory.
6. Write a script that receives a URL from the command line (as argument) and writes the following information into a file: response status, response size, response type (if known), md5 hash for each fragment of maximum 1000 bytes of response and server response time.