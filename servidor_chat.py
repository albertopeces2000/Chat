import socket
import sys

def IP_PORT():
    IP = input('Introduce una IP: ')
    PORT = int(input('Introduce un PORT: '))
    return IP,PORT

IP,PORT = IP_PORT()

##############################################################
servidor_chat = socket.socket()
servidor_chat.bind( (IP, PORT) )
servidor_chat.listen(5) #He puesto un número arbitrario.

conexion, addr = servidor_chat.accept()# devuelve dos tuplas. Una la IP y la otra el puerto correspondiente.
print('Nueva conexión establecida. Se ha iniciado un chat.')
print('Esta es la IP de tu compañer@ de chat:',addr)
#De la línea 12-19 es solo la inicialización del servidor.
###############################################################

repetir = True
while repetir:
    try:
#####################################################
        message_client = conexion.recv(1024)#Aquí recibes el mensaje escrito y enviado por el cliente.
        exit = str.encode("salir")#Al estar en modo byte es necesario codificarlo para que el programa lo entienda.
#####################################################

        if message_client == exit: # si el mensaje recibido por el cliente es 'salir', el servidor se quedará a la espera de un próximo cliente.
            conexion.close() #Cerramos la conexion de la IP
            servidor_chat.close() #Cerramos el servidor
            print('Has introducido el comando "salir".','\n','El chat se cerrará en breve a la espera de otro cliente...')

#############################################################################################
            servidor_chat = socket.socket()
            IP,PORT = IP_PORT()

            servidor_chat.bind( (IP, PORT) )
            servidor_chat.listen(5) #He puesto un número arbitrario.

            conexion, addr = servidor_chat.accept()# devuelve dos tuplas. Una la IP y la otra el puerto correspondiente.
            print('Nueva conexión establecida. Se ha iniciado un chat.')
            print('Esta es la IP de tu compañer@ de chat:',addr)
            repetir = True
#De la línea 32-41 repetimos el ecódigo de inicialización del servidor.
##########################################################################################
        else:
            print(message_client)

            msg = input('>>')
            if msg == "salir":
                conexion.close() #Cerramos la conexion de la IP
                servidor_chat.close() #Cerramos el servidor
                print('Has introducido el comando "salir".','\n','El chat se cerrará en breve a la espera de otro cliente...')

#############################################################################################
                servidor_chat = socket.socket()
                IP,PORT = IP_PORT()

                servidor_chat.bind( (IP, PORT) )
                servidor_chat.listen(5) #He puesto un número arbitrario.

                conexion, addr = servidor_chat.accept()# devuelve dos tuplas. Una la IP y la otra el puerto correspondiente.
                print('Nueva conexión establecida. Se ha iniciado un chat.')
                print('Esta es la IP de tu compañer@ de chat:',addr)
                repetir = True
#De la línea 58-68 repetimos el ecódigo de inicialización del servidor.
################################################################################################
            else:
                message_server = str.encode(     msg     )

                conexion.send(message_server)#Aquí envías un mensaje de respuesta una vez recibido el que proviene del cliente.
                repetir = True

    except KeyboardInterrupt:
        conexion.close() #Cerramos la conexion de la IP
        servidor_chat.close() #Cerramos el servidor
        print('El chat se está cerrando...')

        repetir = False
