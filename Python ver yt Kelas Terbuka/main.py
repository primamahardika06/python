import os
import CRUD as CRUD


if __name__ == "__main__":
    sistem_operasi = os.name
    
    
    match sistem_operasi:
        case "nt": os.system("cls")

    title = "SELAMAT DATANG DI PY PERPUSTAKAAN"
    simbol = "=" * len(title)

    print(simbol)
    print(title)
    print(simbol)
    
    
    # Check database
    CRUD.init_console()
    
    
    while True:
        match sistem_operasi:
            case "nt": os.system("cls")

        title = "SELAMAT DATANG DI PY PERPUSTAKAAN"
        simbol = "=" * len(title)

        print(simbol)
        print(title)
        print(simbol)

        user_option = int(input("Pilih Opsi berikut: \n 1). Read data \n 2). Create data \n 3). Update data \n 4). Delete data \n Masukkan opsi: "))
        
        
        match user_option:
            case 1: CRUD.read_console()
            case 2: CRUD.create_console()
            case 3: CRUD.update_console()
            case 4: CRUD.delete_console()

        
        while True:    
            is_done = input("Apakah sudah selesai? (y/n): ")
            
            if is_done.lower() == "y":
                print("Terima kasih")
                exit()
            elif is_done.lower() == "n":
                break
            else: 
                print("masukkan input yang sesuai!")