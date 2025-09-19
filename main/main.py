from library import welcome_message, exit_program
from games import pygame 
from tools import pywarung
import os


if __name__ == "__main__":
    sistem_operasi = os.name    

    match sistem_operasi:
       case "nt" : os.system("cls")

def menu():
    while True:
        pilihan_user = int(input("\n Silahkan pilih menu program dibawah: \n 1). PYGAME \n 2). PYWARUNG \n 3). Keluar Program \n\n Silahkan pilih: "))
        if pilihan_user == 1:
            pygame.start()
            while True:  
                continue_game = input("Apakah ingin melanjutkan program? (y/n): ")
                if continue_game == "y":
                    pygame.start()
                elif continue_game == "n":
                    break
                else:
                    print("Masukkan perintah dengan benar!")
        elif pilihan_user == 2:
            pywarung.start()
            while True:  
                continue_game = input("Apakah ingin melanjutkan program? (y/n): ")
                if continue_game == "y":
                    pywarung.start()
                elif continue_game == "n":
                    break
                else:
                    print(" Masukkan perintah dengan benar!")
        elif pilihan_user == 3:
            exit_program()
        else:
            print(" Hanya dapat memilih opsi diatas")

def main():
    welcome_message() 
    menu()

if __name__ == "__main__":
    main()
    
 
            