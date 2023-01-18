# pyuic5 -x ui_chat.ui -o ui_chat.py # pyQt5 version

import socket
import threading

IP = '127.0.0.1'
PORT = 9999

clients = []

# Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Keep port always open
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind socket to IP address and port
server.bind((IP, PORT)) # Notice tuple
# Start listening on defined port
server.listen()

def broadcast(msg):
    for client in clients:
        client.send(msg)

def handle_connection(client):
    stopped = False
    while not stopped:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            stopped = True
            print("Exceptiin mentiin")
            # Jos käyttäjä poistuu esim. sulkemalla ikkunan

def start_server():
    print("Server is running.")
    while True:
        # Accept all connections
        client, port = server.accept() #kun käyttäjä connectaa
        client.send("USERNAME".encode('utf-8'))
        # Seuraava viesti sisältää uernamen:
        username = client.recv(1024).decode('utf-8') # Username saadaan
        clients.append(client)
        # print(f"{username} has joined")
        # client.send(f"{username} joined the chat.".encode('utf-8'))
        broadcast(f"{username} joined the chat.".encode('utf-8'))

        thread = threading.Thread(target=handle_connection, args=(client,))
        thread.start

# Run start_server -function only if this file is being run.
if __name__ == '__main__':
    start_server()