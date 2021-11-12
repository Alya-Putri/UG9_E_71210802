nama = []
TL = []
nama = [item for item in input("Nama : ").split()]
TL = [item for item in input("Tempat Tanggal Lahir : ").split()]
jumlahKataNama = len(nama) - 1
jumlahkataTL = len(TL) -1

sisa_nama = ""
for i in range(0,jumlahKataNama):
    sisa_nama = sisa_nama + nama[i] + " "
tanggal = ""
for i in range(jumlahkataTL-(jumlahkataTL-1),jumlahkataTL+1):
    tanggal = tanggal + TL[i] + " "


print("Haloo!",nama[jumlahKataNama],",",sisa_nama)
print("Anda lahir di",TL[0],"pada tanggal", tanggal)
