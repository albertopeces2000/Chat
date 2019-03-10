import socket
import sys



cliente_chat = socket.socket()
cliente_chat.connect( ('192.168.1.45',8080) ) #Se conecta con el servidor_chat




repetir = True
while repetir:
    try:
##################################################

        msg = input('>>: ')

        if msg == 'salir':

            mensaje = str.encode(msg)
                # We must write bytes, not a string
            cliente_chat.send(mensaje)

            sys.exit(1)
        else:
            mensaje = str.encode(msg)
    # We must write bytes, not a string
            cliente_chat.send(mensaje)
#Aquí envías un primer mensaje al servidor_chat a la espera de una respuesta.
#necesitmaos convertir el tipo string en bytes para que pueda ser enviada al servidor.
##################################################
        mensaje_server = cliente_chat.recv(1024)#Aquí puedes obtener el mensaje que has escrito en el servidor.

        exit = str.encode("salir")
        if mensaje_server is exit:
            #cliente_chat.close()
            print('Usted acaba de salir del chat. Pulse el enter para salir.')
            sys.exit(1)
            #repetir = False
        else:

            print(mensaje_server)

        repetir = True
    except KeyboardInterrupt:

        cliente_chat.close()
        print('El chat se está cerrando...')
        repetir = False
    except ConnectionAbortedError:
        cliente_chat.close()
        print('El chat se está cerrando...')
        repetir = False
