import socket

TARGET = "127.0.0.1"
PORTS = [22, 21, 23, 80, 443, 3306, 5432, 3389, 445, 5900]
TIMEOUT = 0.5

for port in PORTS:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)

    result = s.connect_ex((TARGET, port))
    s.close
    
    if result == 0:
        print(f"{port}: Open")
    else:
        print(f"{port}: closed")