import socket

hostname = 'locket'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50001))
print("Mesin penjawab otomatis sudah siap")
while pesan.lower() != 'keluar' :
    pesan = raw_input("Pertanyaan")
    s.send(pesan)
    if pesan.lower() != 'keluar' :
        response = s.recv(1024)
        print("Jawaban :", response)
s.close()
