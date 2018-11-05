#!/usr/bin/env python3
import asyncio

metrics_list = []


def run_server(host='127.0.0.1', port=8888):

    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, int(port))

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class ClientServerProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):

        resp = data.decode().split("\n", 1)[0]

        decoted_data = resp.split()

        method = decoted_data[0]

        query_data = decoted_data[1:]

        if method == 'get':
            resp = self._get(query_data)
        elif method == 'put':
            resp = self._put(query_data)
        else:
            resp = 'error\nwrong command\n\n'

        self.transport.write(resp.encode())

    def _get(self, get_data):

        try:
            key = get_data[0]

            if key == "*":
                data = list(map(lambda i: ' '.join(i), metrics_list))

            else:
                iter_obj = filter(lambda i: i[0] == key, metrics_list)

                data = list(map(lambda i: ' '.join(i), iter_obj))

            result = '\n'.join(['ok'] + data)

            return f'{result}\n\n'

        except Exception:

            return 'error\nwrong command\n\n'

    def _put(self, put_data):

        try:

            data = list(filter(lambda info: info == put_data, metrics_list))
            if len(data) == 0:
                metrics_list.append(put_data)

            return 'ok\n\n'

        except Exception:

            return 'error\nwrong command\n\n'


if __name__ == "__main__":
    run_server()
