import socket


hostname = input("Enter your hostname ")
ip = socket.gethostbyname(hostname)

print('--------------------\n''HOSTNAME: ', hostname, '\n' 'INTERNET PROTOCOL: ', ip ,'\n--------------------')
