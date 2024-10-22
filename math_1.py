import math #Library untuk operasi matematika

luas_lingkaran = lambda r: math.pi * r*r #Menggunakan fungsi lambda untuk menghitung luas lingkaran

#contoh penggunaan
jari_jari = 7 # Menentukan jari-jari lingkaran
area = luas_lingkaran(jari_jari) #Menghitung luas lingkaran menggunakan fungsi lambda yang sudah dibuat

print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area: .2f}") #Mencetak hasil perhitungan dengan format dua angka di belakang koma
