#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

#https://realpython.com/python-sockets/#socket-api-overview
#https://www.tecmint.com/ifconfig-command-examples/#:~:text=ifconfig%20in%20short%20%E2%80%9Cinterface%20configuration,in%20a%20system%20configuration%20scripts.
#https://searchapparchitecture.techtarget.com/definition/Remote-Procedure-Call-RPC#:~:text=Remote%20Procedure%20Call%20(RPC)%20is,to%20understand%20the%20network's%20details.&text=A%20procedure%20call%20is%20also,uses%20the%20client%2Dserver%20model.
#https://www.tutorialspoint.com/python_network_programming/python_remote_procedure_call.htm






