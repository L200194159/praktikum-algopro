print("<!DOCTYPE html>\n")
print("""<html>""")
print("""<head><title>Akses dengan SimpleHTTPServer</title></head>
<body><h3>Bangun Geometri</h3>""")
panjang = 8
lebar = 4
tinggi = 4
luas = panjang*lebar*tinggi
print("""<table><tr><td>Nama Bangunan</td><td>:</td><td>Prisma Segiempat</td></tr>
		<tr><td>Dimensi</td><td>:</td><td>3D</td></tr>
		<tr><td>Rumus luas</td><td>:</td><td>panjang x lebar x tinggi</td></tr>""")
print("""<tr><td>Parameter 1</td><td>:</td><td>{0}</td></tr>""".format(panjang))
print("""<tr><td>Parameter 2</td><td>:</td><td>{0}</td></tr>""".format(lebar))
print("""<tr><td>Parameter 3</td><td>:</td><td>{0}</td></tr>""".format(tinggi))
print("""<tr><td>Luas</td><td>:</td><td>{0}</td></tr></table>""".format(luas))
print("""<script>var c = document.getElementById("myCanvas")</script></body></html>""")
