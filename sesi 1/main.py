#variabel : tempat penampungan data sementara
# nama = "PRIMA"
# usia = 19


# #menggunakan tanda +
# print("*********")
# print("**" +nama + "**")
# print("*********")

# #menggunakan format (f)
# print(f''' 
# nama saya adalah {nama} 
# usia saya adalah {usia}
# ''')

#contoh pengguaan if sederhana
# nomor_input = int(input("masukkan nomor anda: "))
# nomor_benar = 10
# if nomor_input == nomor_benar:
#     print(f"Betul nomor saya adalah {nomor_benar}")
# else :
#     print(f"nomor saya bukan {nomor_input}")
#     print("masukkan angka yang benar")
 
 
#  menambahkan sistem loop (while) 
# import random  
# welcome_message = "WELCOME TO PRIMA GAMES!"

# print("****************************")
# print (f"** {welcome_message}**")
# print("****************************")


# while True:
#     nama = input("Masukkan namamu: ")
    
#     benar = random.randint(1,4)
    
#     print (f'''
#     Hallo {nama}! Coba Perhatikan Kotak di Bawah!
#     |1| |2| |3| |4|
#     ''')

#     tebakan = int(input("Menurutmu dimana aku berada? 1/2/3/4: "))

#     if tebakan == benar :
#         print(f"Selamat {nama} kamu benar aku, aku berada di nomor {benar}! ")
#     else :
#         print(f"Salah! Aku berada di nomor {benar}")
        
#     ulang = input("Ketik 'Ulang' jika kamu ingin mencoba lagi :")
#     if ulang.lower() != 'ulang' :
#         print ("Game Over")
#         break 
    
    
# tugas cuyuniversity python #1  
import random  
welcome_message = "WELCOME TO PRIMA GAMES!"


print("****************************")
print (f"** {welcome_message}**")
print("****************************")

   
while True :
    nama = input("Masukkan namamu: ")
    print (f'''
    Hallo {nama}! Coba Perhatikan Kotak di Bawah!
    |1| |2| |3| |4|
    ''')
    benar = random.randint(1,4)
    tebakan = int(input("Menurutmu dimana aku berada? 1/2/3/4: "))
        
    while True :
        tanya = input(f"Apakah kamu yakin memilih nomor {tebakan} [y/t]: ")
        if tanya != 'y':
            tebakan = int(input("Menurutmu dimana aku berada? 1/2/3/4: "))
        else:
            break
            
    if tebakan == benar:
        print(f"Selamat {nama} kamu benar aku, aku berada di nomor {benar}! ")
        
    else :
        print(f"Salah! Aku berada di nomor {benar}")
        
    reset = input("Apakah kamu mau mengulangin permainan, jika iya ketika 'Ulang': ")
    if reset.lower() != 'ulang' :
        print("Game Selesai")
        break





    
    