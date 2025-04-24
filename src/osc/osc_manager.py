from pythonosc.udp_client import SimpleUDPClient
import ipaddress

class OSCManager:
    def __init__(self, settings):
        self.settings = settings

    def send_message(self, character, text):
        ip   = self.settings.get('OSC', f'{character}_ip')
        port = int(self.settings.get('OSC', f'{character}_port', fallback=0))
        try:
            ipaddress.ip_address(ip)
            client = SimpleUDPClient(ip, port)
            client.send_message('/chatbox/input', [text, True, False])
        except Exception as e:
            print(f"[ERROR] OSC send failed: {e}")