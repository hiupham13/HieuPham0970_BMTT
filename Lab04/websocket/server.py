import random
import tornado.ioloop
import tornado.web
import tornado.websocket
class WebSocketServer(tornado.websocket.WebSocketHandler):
    clients = set()
    def open(self):
        WebSocketServer.clients.add(self)
    def on_close(self):
        WebSocketServer.clients.remove(self)
    @classmethod
    def send_message(cls, message: str):
        print (f"Sending message to {len(cls.clients)} clients(s)")
        for client in cls.clients:
            client.write_message(message)
class RandomWordSelector:
    def __init__(self, words):
        self.words = words
    def sample(self):
        return random.choice(self.words)
def main():
    app = tornado.web.Application([
        (r"/websocket/", WebSocketServer),
        websocket_ping_interval=10,
         websocket_ping_timeout=30,
    ])
    app.listen(8888)
    io_loop = tornado.ioloop.IOLoop.current()
    words = RandomWordSelector(["apple", "banana", "cherry"])
    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketServer.send_message(words.sample()), 3000
    )
    periodic_callback.start()
    io_loop
if __name__ == "__main__":
    main()