import socket
import time


class ClientError(socket.error):
    pass


class Client():

    def __init__(self, server_host, server_port, timeout=None):
        self.server_host = server_host
        self.server_port = server_port
        self.timeout = timeout

    def __server_answer(self):
        pass

    def get(self, key):

        my_dict = {}

        with socket.create_connection((self.server_host, self.server_port),
                                      self.timeout) as sock:
            try:
                sock.sendall(
                    f"get {key}\n".encode()
                )

                data = sock.recv(1024)

            except socket.error as ex:
                raise ClientError("send data error", ex)

        decoded_data = data.decode()

        # delete the \n\n
        decoded_data = decoded_data.split("\n\n", 1)[0]

        if decoded_data == "":
            return my_dict

        try:
            status, parametrs = decoded_data.split("\n", 1)
            parametrs = parametrs.strip()

        except ValueError:
            return my_dict

        if status == "error":
            raise ClientError()

        for row in parametrs.split("\n"):
            key, value, timestamp = row.split()
            if key not in my_dict:
                my_dict[key] = []
            my_dict[key].append((int(timestamp), float(value)))

        return my_dict

    def put(self, metric_name, metric_value, timestamp=None):

        if timestamp is None:
            timestamp = int(time.time())

        with socket.create_connection((self.server_host, self.server_port),
                                      self.timeout) as sock:
            try:
                sock.sendall(f"put {metric_name} {metric_value} \
                             {timestamp}\n".encode())

                data = sock.recv(1024)
            except socket.error as ex:
                raise ClientError("send data error", ex)

            decoded_data = data.decode()
            # delete the \n\n
            decoded_data = decoded_data.split("\n\n", 1)[0]

            try:
                status, parametrs = decoded_data.split("\n", 1)
                if status == "error":
                    raise ClientError()
            except ValueError:
                pass
