import socket

host,port=('',5000) #déterminer le port auquel on va se connecter et l'adresse IP du serveeur dans notre cas une machine distante 192.168.0.10

socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)# déterrminet le type de connexion qui est TCP
socket.bind((host,port))                               # lancer la connexion
print("le serveur est démarré")

while True:
      socket.listen(5)# déterminer le nombre de clients qu'on ne doit pas dépasser dans ce cas c'est 5 clients
      conn,address=socket.accept()# accepter la connexion
      print("En écoute...")

conn.close()# fermer la connexion
socket.close() # fermer la socket
