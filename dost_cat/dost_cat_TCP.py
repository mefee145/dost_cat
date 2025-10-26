import socket
import random

class TCPSendTo:
    def __init__(self, IP="127.0.0.1", Port=12345):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((IP, Port))
        print(f"Bağlantı kuruldu: {IP}:{Port}")

    def send(self):
        try:
            for i in range(1, 100_000):  # 100 x 1000 = 100000
                data = random._urandom(10) * 1000  # 10,000 byte
                self.s.sendall(data)
                print(f"Gönderildi: {i}")
        except Exception as e:
            print(f"Hata oluştu: {e}")
        finally:
            self.s.close()
            print("Bağlantı kapatıldı.")