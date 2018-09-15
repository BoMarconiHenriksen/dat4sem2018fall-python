# Brug socket til netværk.
import socket
#socket.recv
# Hent din egen ip addresse.
this_host = socket.gethostname()
print(this_host)
this_ip = socket.gethostbyname(this_host)
print(this_ip)
