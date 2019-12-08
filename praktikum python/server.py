import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 50001))
s.listen(5)
print("Server penjawab otomatis sudah siap")
data = ''
kamus = {'nama' : 'Juniar Darma Yati',
         'NIM' : 'L200194159',
         'angkatan' : '2019',
         'keluar' : 'siap'}
while data.lower() != 'keluar' :
    komm, addr = s.accept()
    while data.lower() != 'keluar' :
        data = komm.recv(1024)
        if data.lower() == 'keluar' :
            s.close()
            break
        print ("Pertanyaan :" , data)
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send("Pertanyaan anda tidak relevan")
        
