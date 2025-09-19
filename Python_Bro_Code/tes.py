import os


if __name__ == "__main__":
    sistem = os.name
    
    match sistem:
        case "nt" : os.system("cls")


# #latihan #1 (Luas Persegi Panjang)
# length = int(input("Masukkan panjang: "))
# width = int(input("Masukkan lebar: "))
# result = length * width
# print(f"hasilnya adalah {result}cm²")


# latihan #2 ( keliling lingkaran)
# radius = float(input("Masukkan jari-jari lingkaran: "))

# kll = 2 * math.pi * radius

# print (f"kelilingnya adalah : {round(kll , 2)}cm")


#latihan #3 (Luas Lingkaran)
# radius = float(input("Masukkan jari-jari: "))

# luas = math.pi * pow(radius, 2)

# print(f"Luas lingkaran adalah {round(luas , 2)}cm²")


# latihan #4
# a = int(input("Nila A: "))
# b = int(input("Nila B: "))

# c = math.sqrt(pow(a, 2) + pow(b, 2))

# print(f"Hasilnya adalah {int(c)}")


# x = 3.14

# print(round(x))

# input = input("Masukkan inputan: ")
# hasil = input.find(" ")
# hasil = input.rfind("r")
# hasil = input.capitalize()
# hasil = input.lower()
# hasil = input.isdigit()
# hasil = input.isalpha()
# hasil = input.count("-")
# hasil = input.replace(" ")
# print(hasil)


# [start : end : step]
# number = "0859-6033-6954"
# last_number = number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_number}")
# print(number[0])
# print(number[:5])
# print(number[5:9])
# print(number[0:9:2])


# price1 = 3.1234
# price2 = -986.345
# price3 = 12.45
# print(f"Price 1: {price1:+,.2f}")
# print(f"Price 2: {price2:+,.2f}")
# print(f"Price 3: {price3:+,.2f}")

food = input("Makanan favorit (ketik n untuk keluar): ")

while not food.lower() == "n":
    print(f"Kamu suka {food}")
    food = input("Makanan favorit lainnya (ketik n untuk keluar): ")    
    
print("Terima Kasih")