"""
Day 10 - Websocket Command Line Chat
Server
"""

import socket
import threading

HOST = "localhost"
PORT = 777

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []


def broadcast(message, client):
    for c in clients:
        if c != client:
            c.send(message)


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f"{username} has left the chat.".encode("utf-8"), client)
            usernames.remove(username)
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("USERNAME".encode("utf-8"))
        username = client.recv(1024).decode("utf-8")
        usernames.append(username)
        clients.append(client)

        print(f"Username of the client is {username}")
        broadcast(f"{username} has joined the chat!".encode("utf-8"), client)
        client.send("Connected to the server!".encode("utf-8"))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


print("Server is listening...")
receive()
