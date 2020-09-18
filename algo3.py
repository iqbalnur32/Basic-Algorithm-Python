# Menghitung Kecepatan Rata Rata

jarak = 10000
waktu = int(input("Masukan Waktu: "))
kecepatan = int(input("Masukan Kecepatan: "))

if waktu == 0:
	kecepatan = 0
else:
	kecepatan = jarak / waktu

print("Kecepatan = ", kecepatan);
