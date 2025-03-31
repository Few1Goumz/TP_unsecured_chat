import pickle
import zmq
import logging

class BigBrother:
    def __init__(self, recv_port: int) -> None:
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.SUB)
        self._socket.connect(f"tcp://localhost:{recv_port}")
        self._socket.setsockopt_string(zmq.SUBSCRIBE, "")  # Écouter tous les messages
        self._log = logging.getLogger(self.__class__.__name__)

    def listen(self):
        print("Big Brother is listening...")
        try:
            while True:
                packet = self._socket.recv()  # Recevoir les données brutes
    
                print(f"Intercepted: {packet}")  # Afficher le message
        
        except KeyboardInterrupt:
            print("Stopping Big Brother...")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    bigbrother = BigBrother(6667)  # Port du serveur
    bigbrother.listen()
