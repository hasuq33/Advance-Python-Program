import socket

#host = socket.gethostbyname(socket.gethostbyname()) # You can get your privite ip address usinh this gethostbyname

HOST = '192.168.0.4'  
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #This socket is just for the accepting the connections not for the communication
server.bind((HOST,PORT))

server.listen(5)

while True:
    commuication_socket ,address = server.accept()
    print(f"connected to {address}")
    message = commuication_socket.recv(1024).decode('utf-8')
    print(f"Message from client is: {message}")
    commuication_socket.send(f"We got your message! Thank you!".encode('utf-8'))
    commuication_socket.close()
    print(f"Connection with {address} ended!")
