from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
from threading import Thread

PORTS = [9000,9002,9004,9006,9100]

def handle(addr,*args): print(f"[RECEIVED]{addr}{args}")

if __name__=='__main__':
    for p in PORTS:
        d = Dispatcher(); d.map('/chatbox/input', handle)
        srv = osc_server.ThreadingOSCUDPServer(('0.0.0.0',p), d)
        Thread(target=srv.serve_forever, daemon=True).start()
    input('Listening... Enter to exit')