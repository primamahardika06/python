from . import operasi


def delete_console():
    read_console()
    while True:
        print("Silahkan pilih buku yang ingin di delete")
        no_buku = int(input("Masukkan nomor buku: "))
        data_buku = operasi.read(index=no_buku)
        
        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break [3]
            tahun_terbit = data_break[4][:-1]
            
            print("\n"+"="*105)
            print("Silahkan Pilih data yang ingin dihapus")
            print(f"1. Penulis: {penulis:.40}")    
            print(f"2. Judul: {judul:.40}")    
            print(f"3. Tahun terbit: {tahun_terbit:4}")
            is_done = input("Apakah yakin ingin menghapus data(y/n)? ")
            if is_done == "y" or is_done == "Y":
                operasi.delete(no_buku)
                break
        else:
            print("Masukkan nomor buku yang tersedia")
            
  
        
        

def update_console():
    read_console()
    while True:
        print("Silahkan pilih buku yang ingin di update")
        no_buku = int(input("Masukkan nomor buku: "))
        data_buku = operasi.read(index=no_buku)
        
        if data_buku:
            break
        else:
            print("Masukkan nomor buku yang tersedia")
            
    data_break = data_buku.split(',')
    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break [3]
    tahun_terbit = data_break[4][:-1]

    while True:   
        # Data yang akan diupdate
        print("\n"+"="*105)
        print("Silahkan Pilih data yang ingin diubah")
        print(f"1. Penulis: {penulis:.40}")    
        print(f"2. Judul: {judul:.40}")    
        print(f"3. Tahun terbit: {tahun_terbit:4}")


        # Data yang dipilih utk diupdate
        user_option = int(input("Pilih opsi 1/2/3: ")) 
        print("\n"+"="*105)   
        match user_option: 
            case 1: penulis = input("Penulis: ")  
            case 2: judul = input("Judul: ")  
            case 3: 
                while True:
                    try:
                        tahun_terbit = int(input("Tahun terbit: "))
                        if len(str(tahun_terbit)) == 4:
                            break
                        else: 
                            print("Tahun harus menggunakan angka (yyyy)!!")    
                    except:
                        print("Tahun harus menggunakan angka (yyyy)!!")
            case _:
                print("index tidak cocok")
         
        print("Data baru anda")
        print(f"1. Penulis: {penulis:.40}")    
        print(f"2. Judul: {judul:.40}")    
        print(f"3. Tahun terbit: {tahun_terbit:4}")
        is_done = input("Apakah data sudah sesuai(y/n)? ")
        if is_done == "y" or is_done == "Y":
            break
                       
    operasi.update(no_buku,pk,date_add,penulis,judul,tahun_terbit)


    
def create_console():
    print("\n"+"="*50)
    print("Silahkan Create Data\n")
    penulis = input("Penulis: ")
    judul= input("Judul: ")
    while True:
        try:
            tahun_terbit = int(input("Tahun terbit: "))
            if len(str(tahun_terbit)) == 4:
                break
            else: 
               print("Tahun harus menggunakan angka (yyyy)!!")    
        except:
            print("Tahun harus menggunakan angka (yyyy)!!")
     
     
    operasi.create(penulis,judul,tahun_terbit)    
    print("\nberikut adalah data baru")   
    read_console()           
            

def read_console():
    data_file = operasi.read()
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun_terbit = "Tahun Terbit"
    
    
    # Header
    print("\n"+"="*105)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun_terbit:5}")
    print("-"*105 + "\n")
    
    
    # Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break [3]
        tahun_terbit = data_break[4]
        print(f"{index+1:4} | {judul:40} | {penulis:40} | {tahun_terbit:4}", end="")
    
    # Footer
    print("="*105+"\n")