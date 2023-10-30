import math
print("Menghitung Luas dan Keliling Lingkaran")
print("---------------------------------------")

r = float(input("Masukkan jari-jari lingkaran: "))
math.pi= 22/7
luas = math.pi * r * r
keliling = 2 * math.pi * r

print("Luas lingkaran:", luas)
print("Keliling lingkaran:", keliling)