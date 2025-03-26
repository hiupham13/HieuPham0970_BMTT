import tornado.ioloop
import tornado.websocket

class WebSocketClient:
    def __init__(self, io_loop):
        self.connection = None
        self.io_loop = io_loop
    def start(self):
        self.connect_and_read()
    def stop(self):
        self.io_loop.stop()
    def connect_and_read(self):
        print("Reading..")
        tornado.websocket.websocket_connect(
            url="ws://localhost:8888/websocket/",
            callback=self.maybe_retry_connection,
            on_message_callback=self.on_message,
            ping_interval=10,
            ping_timeout=30,
        )

