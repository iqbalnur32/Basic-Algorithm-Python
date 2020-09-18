# Alur Program
"""
1. Mulai
2. Users Memasukan Inputan 1
3. Users Memasukan Inputan 2
4 .Jika angka pertama lebih besar daripada angka kedua: cetak angka pertama sebagai angka terbesar
5. Selain itu, jika angka pertama lebih kecil daripada angka kedua: cetak angka kedua sebagai angka terbesar
6. Selain itu, jika angka pertama sama dengan angka kedua: cetak pemberitahuan bahwa tidak ada angka terbesar karena sama
7 .Selain itu, cetak pemberitahuan bahwa ada kesalahan masukan 
8. Selesai
"""

input1 = input("Masukan Inputan 1 : ")
input2 = input("Masukan Inputan 2 : ")

if input1 > input2:
	print("Angka terbesar: ", input1)
elif input1 < input2:
	print('Angka terbesar: ', input2)
elif input1 == input2:
	print('Tidak ada angka yang sama ' + 'karena angka ' + input1 + ' dan ' + input2 + ' sama')
else:
	print("Error data salah Memasukan !")