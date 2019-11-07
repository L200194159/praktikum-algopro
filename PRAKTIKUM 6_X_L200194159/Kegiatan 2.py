import random
angka = random.randint(0,1000)

Nama = "Juniar Darma Yati"
TTL = "14 Juni 2001"
NamaSingkat = Nama[0] + '.' + Nama[7] + '.' + Nama[13]
UserName = Nama[0] + TTL[0:2] + TTL[8:12]
Password = Nama[0:3] + str(angka)
