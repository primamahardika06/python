import random
from library import exit_program

def start():
    while True:
        random_chose = random.randint(1, 4)
        
        kotak = "|📦|"
        kotak_kosong = [kotak] * 4
        kotak_isi = kotak_kosong.copy()
        kotak_isi [random_chose - 1] = "|😺|"
        kotak_kosong ="".join(kotak_kosong)
        kotak_isi = "".join(kotak_isi)
        
        print(f'\nSelamat datang di permainan, sekarang coba tebak dimanakah aku berada?\n\n{kotak_kosong}\n\n' )

        player_chose = int(input("Silahkan pilih kotak tempatku berada (1/2/3/4): "))
        while True:
            if 1 <= player_chose  <= 4:
                break
            else: 
                player_chose = int(input("\nInput angka dengan benar: "))
            
    
        if player_chose == random_chose:
            print(f"\nSelamat kamu menang, aku berada di kotak {random_chose} \n\n {kotak_isi} ") 
        else:
            print(f"\nKamu kalah aku berada di kotak {random_chose} \n\n {kotak_isi}")

        break
        
         
        
                
if __name__ == "__main__":
    start()