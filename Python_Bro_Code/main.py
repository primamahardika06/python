import os
import math

if __name__ == "__main__":
    sistem_operasi = os.name
    
    
    match sistem_operasi:
        case "nt": os.system("cls")


# Projek kalkulator
# operasi = input("Pilih operasi perhitungan: (+ - / *): ")
# num1 = int(input("Angka pertama: "))
# num2 = int(input("Angka kedua: "))

# if operasi == "+":
#     hasil = num1 + num2
#     print(hasil)
# if operasi == "-":
#     hasil = num1 - num2
#     print(hasil)
# if operasi == "/":
#     hasil = num1 / num2
#     print(hasil)
# if operasi == "*":
#     hasil = num1 * num2
#     print(hasil)

#Projek converter panjang (km > m, m > km )
# panjang = float(input("Masukkan panjang: "))
# tipe = input("Ingin ubah dari apa(km/m): ")

# if tipe == "m":
#     panjang = panjang / 1000
#     tipe = "km"
#     print(f"{round(panjang)} {tipe}")
# elif tipe == "km":
#     panjang = panjang * 1000
#     tipe = "m"
#     print(f"{round(panjang)} {tipe}")
# else:
#     print("eror")

# Converter suhu 
# suhu = float(input("Masukkan suhu nya: "))
# tipe = input("Suhu bertipe apa (C/R/F): ")

# if tipe == "c" or tipe == "C":
#     opsi = input("Ingin convert menjadi apa (R/F): ")
#     if opsi == "r" or opsi == "R":
#         suhu = (suhu * 4) / 5
#         print(f"suhu berhasil di convert menjadi {round(suhu)}°R")
#     elif opsi == "f" or opsi == "F":
#         suhu = (suhu * 9) / 5 + 32
#         print(f"suhu berhasil di convert menjadi {round(suhu)}°F")
#     else:
#         print("eror")
# if tipe == "r" or tipe == "R":
#     opsi = input("Ingin convert menjadi apa (C/F): ")
#     if opsi == "c" or opsi == "C":
#         suhu = (suhu * 5) / 4
#         print(f"suhu berhasil di convert menjadi {round(suhu)}°C")
#     elif opsi == "f" or opsi == "F":
#         suhu = (suhu * 9) / 4 + 32
#         print(f"suhu berhasil di convert menjadi {round(suhu)}°F")
#     else:
#         print("eror")
# if tipe == "f" or tipe == "F":
#     opsi = input("Ingin convert menjadi apa (R/C): ")
#     if opsi == "r" or opsi == "R":
#         suhu = (suhu - 32) * 4 / 9
#         print(f"suhu berhasil di convert menjadi {round(suhu)}°R")
#     elif opsi == "c" or opsi == "C":
#         suhu = (suhu - 32) * 5 / 9
#         print(f"suhu berhasil di convert menjadi {round(suhu)}°C")
#     else:
#         print("eror")


# exercise #1
username = input("masukkan username kamu: ")

if len(username) > 30:
    print("minimal 12 charachter")
elif not username.find(" ") == -1:
    print("tidak boleh ada spasi") 
elif not username.isalpha():
    print("tidak boleh ada angka") 
else:
    print(f"welcomed {username}")

    
    
