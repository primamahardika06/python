#fata list (array dalam bahasa pemrograman lain)

# hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]
# hari.append("hari libur")
# print(len(hari)) #panjang data list
# print(hari[6]) #muncul hari minggu (seuai urutan list mulai dari 0)
# print(hari[1*2]) #hasinya 2 muncul value ke 2 dari variabel hari yaitu rabu


#grade berdasarkan nilai

# #dengan berdasakan value yang ada
# def grade(nilai) :
#     if nilai >= 90:
#         print(f"Nilai {nilai} termasuk dalam grade A")
#     elif nilai >=80 and nilai <=89:
#         print(f"Nilai {nilai} termasuk dalam grade B")
#     elif nilai >=70 and nilai <=79:
#         print(f"Nilai {nilai} termasuk dalam grade C")
#     else:
#         print(f"Nilai {nilai} termasuk dalam grade D")
# nilai = 80       
# grade(nilai)


# #dengan input sendiri
# def grade(nilai) :
#     if nilai >= 90:
#         print(f"Nilai {nilai} termasuk dalam grade A")
#     elif nilai >=80 and nilai <=89:
#         print(f"Nilai {nilai} termasuk dalam grade B")
#     elif nilai >=70 and nilai <=79:
#         print(f"Nilai {nilai} termasuk dalam grade C")
#     else:
#         print(f"Nilai {nilai} termasuk dalam grade D")
        
# input_nilai = int(input("Berapa nilai yang kamu dapatkan: "))       
# grade(input_nilai)



# Sesi 2
# hobi = ["musik", "game", "ngoding"]
# tmp_hobi = hobi #untuk mengubah value dari varabel hobi jika tidak diinginkan misal merubah "game" menjadi "lari"

# output data terakhir
# length_data = len(hobi) - 1
# print(hobi[length_data -1])
# print (hobi[len(hobi) - 1])

# print(f"hobi = {hobi}")
# print(f"tmp_hobi = {tmp_hobi}") 

# # misal
# tmp_hobi[1] = "lari" #game berada di baris ke 1, merubah game menjadi lari
# print(f"tmp_hobi = {tmp_hobi}") #berubah menjadi lari




# latihan cuyuniversity python #2  
import random  
welcome_message = "WELCOME TO PRIMA GAMES!"

print("****************************")
print (f"** {welcome_message}**")
print("****************************")

while True :
    benar = random.randint(1,4)

    bentuk_kotak = "|_|"
    kotak_kosong = [bentuk_kotak] * 4
    kotak = kotak_kosong.copy()
    kotak[benar - 1] = "|😺|"


    nama = input("Masukkan namamu: ")
    print (f'''
    Hallo {nama}! Coba Perhatikan Kotak di Bawah!
    {"".join(kotak_kosong)} 
    ''')

    while True:
        tebakan = int(input("Menurutmu dimana aku berada? 1/2/3/4: "))

    
        while True :
            tanya = input(f"Apakah kamu yakin memilih nomor {tebakan} [y/n]: ")
            if tanya.lower() == 'n':
                break
            elif tanya.lower() == 'y':
                if tebakan == benar:
                    print(f" hore kamu menemukan aku \n {"".join(kotak)} \n Selamat {nama} kamu benar, aku berada di nomor {benar}! ")
                else :
                    print(f" yah salah, coba tebak lagi \n {"".join(kotak)}  \n Salah! Aku berada di nomor {benar}")
                    break
            else:
                print("input salah")
                
        if tanya.lower() == 'n':
            continue
        else:
            break
    
            
    while True :  
        reset = input("Apakah kamu mau mengulangin permainan, jika iya ketika 'yes', jika tidak ketik 'no': ")
        if reset.lower() == 'yes' :
            break 
        elif reset.lower() == 'no' :
            print("Game Selesai")
            exit()
        else:
            print("Masukkan perintah dengan benar 'Yes' atau 'No' ")
        




    
    

        

        
    