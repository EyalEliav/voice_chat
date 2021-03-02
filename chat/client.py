import socket
import threading
from connection import Connection


class Client(Connection):

    def __init__(self, name, addr, port):
        super().__init__(name)
        try:
            print('trying to connect...')
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
                connection.connect((addr, port))
                print('connection succeed.')
                threading.Thread(target=self.read, args=(connection,)).start()
                self.write(connection)
        except Exception as e:
            print(e)

    def close(self):
        super().close()

# this is where the object is created and the constructor is called
