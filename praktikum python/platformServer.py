import socket
import platform

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 50011))
s.listen(5)
print("Server penjawab otomatis sudah siap")
data = ''
kamus = {'machine' : platform.machine(),
         'release' : platform.release(),
         'system' : platform.system(),
         'version' : platform.version(),
         'node' : platform.node(),}
while data.lower() != 'quit' :
    komm, addr = s.accept()
    while data.lower() != 'quit' :
        data = komm.recv(1024)
        if data.lower() == 'quit' :
            s.close()
            break
        print ("Pertanyaan :" , data)
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("Pertanyaan anda tidak relevan")
        
