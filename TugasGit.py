nama = input("Masukkan Nama Anda : ")
print("Halo ",nama )

for huruf in nama:
    print(huruf)

if len(nama)> 5:
    print("Nama Anda cukup panjang!")
else:
    print("Nama Anda cukup pendek!")