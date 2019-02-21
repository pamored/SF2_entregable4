import socket
from _thread import *
import sys

#Se crea la conexion del servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Lo parametros para saber por donde se conectaran los cliente al servidor
server = 'localhost'
port = 5555
#obtener el hostname
#server_ip = socket.gethostbyname(server)

#Si la conexion de los clientes hga sido la correcta
try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))
#Esperando la cantidad de conexiones
s.listen(2)
print("Esperando conexion")

#Primer cliente en conectarsed
cliente = "0"

#primera posicion de los objetos
pos = ["0:0,400,,no,0,100", "1:737,400,,si,0,100"]
def threaded_client(conn):
    global cliente, pos
    conn.send(str.encode(cliente))
    cliente = "1"
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("No se logro"))
                break
            else:
                #recibe lo enviado al hsot de los dos lados
                print("Recebido: " + reply)

                #Lo separa para asi poder tener de que host a que host es
                arr = reply.split(":")
                id = int(arr[0])
                pos[id] = reply

                #invierte el envio para responderle a cada host
                if id == 0: nid = 1
                if id == 1: nid = 0
                #junta al reply con el id invertgido para enviarlo a cada host
                reply = pos[nid][:]
                print("Enviado: " + reply)
            #Envia el mensaje a cada host
            conn.sendall(str.encode(reply))
        except:
            break

    print("Conexion Terminada")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Conectado a: ", addr)

    start_new_thread(threaded_client, (conn,))