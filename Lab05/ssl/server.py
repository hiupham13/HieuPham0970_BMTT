import socket
import ssl
import threading

server_address = ('localhost', 12345)
clients = []

def handle_client(client_socket):
    clients.append(client_socket)
    print("da ket noi voi client: ", client_socket.getpeername())
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(data)
                    except:
                        clients.remove(client)
    except:
        clients.remove(client_socket)
    finally:
        print("Da ngat ket noi voi client: ", client_socket.getpeername())
        clients.remove(client_socket)
        client_socket.close()

server