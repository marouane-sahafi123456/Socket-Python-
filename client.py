import socket

host,port=('localhost',5000)# le client est la machine locale connect� au port 5000
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # la connexion  est net de type TCP

try: # lever des exceptions
    socket.connect((host,port)) # d�marrer la connexion
    print("client connect�")
except: # si la connexion est �chou�e
    print("connexion au serveur �chou�e")
finally: # apr�s le traitement de tous les cas on ferme la connexion
    socket.close()








 
