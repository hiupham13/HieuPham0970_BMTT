import tornado.ioloop
import tornado.websocket

class WebSocketClient:
    def __init__(self, io_loop, url):
        self.connection = None
        self.io_loop = io_loop
        self.url = url  # Configurable WebSocket URL

    def start(self):
        self.connect_and_read()

    def stop(self):
        self.io_loop.stop()

    def connect_and_read(self):
        print(f"Connecting to {self.url}...")
        tornado.websocket.websocket_connect(
            url=self.url,
            callback=self.maybe_retry_connection,
        )

    def maybe_retry_connection(self, future) -> None:
        try:
            self.connection = future.result()
            print("Connected successfully.")
            self.connection.read_message(callback=self.on_message)
        except Exception as e:
            print(f"Connection failed ({e}), retrying in 3 seconds...")
            self.io_loop.call_later(3, self.connect_and_read)

    def on_message(self, message):
        if message is None:
            print("Disconnected, reconnecting...")
            self.connect_and_read()
            return
        print(f"Received message: {message}")
        self.connection.read_message(callback=self.on_message)

def main():
    io_loop = tornado.ioloop.IOLoop.current()
    websocket_url = "ws://localhost:8888/websocket/"  # Ensure this matches the server's URL
    client = WebSocketClient(io_loop, websocket_url)
    io_loop.add_callback(client.start)
    io_loop.start()

if __name__ == "__main__":
    main()


