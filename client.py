import socket

host,port=('localhost',5000)# le client est la machine locale connecté au port 5000
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # la connexion  est net de type TCP

try: # lever des exceptions
    socket.connect((host,port)) # démarrer la connexion
    print("client connecté")
except: # si la connexion est échouée
    print("connexion au serveur échouée")
finally: # après le traitement de tous les cas on ferme la connexion
    socket.close()








 
