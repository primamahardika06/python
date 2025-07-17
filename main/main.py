from library import welcome_message, exit_program
from games import pygame 
from tools import pywarung

def menu():
    while True:
        pilihan_user = int(input(" Silahkan pilih menu program dibawah: \n 1). PYGAME \n 2). PYWARUNG \n 3). Keluar Program \n\n Silahkan pilih: "))
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
                    print("Masukkan perintah dengan benar!")
        elif pilihan_user == 3:
            exit_program()
        else:
            print("Hanya dapat memilih opsi diatas")

def main():
    welcome_message() 
    menu()
    
if __name__ == "__main__":
    main()


            