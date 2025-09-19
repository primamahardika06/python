from time import sleep        

def menu():
    while True: 
        opsi = int(input("Pilih opsi berikut \n 1). Penjumlahan \n 2). Pengurangan \n 3). Perkalian \n 4). Pembagian \n Opsi pilihan: "))
        
        if opsi == 1:
            number = int(input("Angka pertama: "))
            number2 = int(input("Angka kedua: "))
            hasil = number + number2
            print(f"{number} + {number2} = {hasil}")
        elif opsi == 2:
            number = int(input("Angka pertama: "))
            number2 = int(input("Angka kedua: "))
            hasil = number - number2
            print(f"{number} - {number2} = {hasil}")
        elif opsi == 3:
            number = int(input("Angka pertama: "))
            number2 = int(input("Angka kedua: "))
            hasil = number * number2
            print(f"{number} x {number2} = {hasil}")
        elif opsi == 4:
            number = int(input("Angka pertama: "))
            number2 = int(input("Angka kedua: "))
            if number2 == 0:
                print("Tidak bisa membagi dengan nol!")
            else:
                hasil = number / number2
                print(f"{number} / {number2} = {hasil}")
        elif opsi == 5:
            print("Program dihentikan.")
            break
        else:
            print("Masukkan perintah dengan benar!")
            
        while True:
            ulang = input("Ingin mengulangi program (y/n): ").lower()
            if ulang == "y":
                break 
            elif ulang == "n":
                print("Program akan dihentikan")
                sleep(1)
                print("3️⃣")
                sleep(1)
                print("2️⃣")
                sleep(1)
                print("1️⃣")
                sleep(1)
                print("Terima kasih telah menggunakan program.")
                return 
            else:
                print("Masukkan perintah dengan benar (y/n)!!!")

menu()
