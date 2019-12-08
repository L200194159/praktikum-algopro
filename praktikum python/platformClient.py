import socket

hostname = 'locket'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50011))
print("Mesiin penjawab otomatis sudah siap")
while pesan.lower() != 'quit' :
    pesan = raw_input("Pertanyaan")
    s.send(pesan)
    if pesan.lower() != 'quit' :
        response = s.recv(1024)
        print("Jawaban :", response)
s.close()
