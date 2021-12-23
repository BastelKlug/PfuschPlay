import websocket
import threading
from time import sleep


def on_message(ws, message):
    print(message)


def on_close(ws):
    print("### closed ###")


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "ws://localhost/websocket", on_message=on_message, on_close=on_close)
    ws = threading.Thread(target=ws.run_forever)
    ws.daemon = False
    ws.start()

    conn_timeout = 5
    while not ws.sock.connected and conn_timeout:
        sleep(1)
        conn_timeout -= 1

    msg_counter = 0
    while ws.sock.connected:
        ws.send('Hello world %d' % msg_counter)
        print("Hello World!")
        sleep(1)
        msg_counter += 1
