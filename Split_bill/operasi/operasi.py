from time import sleep
from title.title import title

pesanan = []
nama = []
simbol = title()

def split_bill():
    pesanan.clear() 
    nama.clear()
    
    while True :
        try: 
            user = int(input("Split bill dengan berapa orang: "))
            if user == 1:
                print("Split bill hanya bisa dilakukan jika lebih dari satu orang!!")
            elif user > 1:
                for i in range(user):
                    user = input(f"Masukkan nama orang ke-{i+1}: ")
                    nama.append(user)
                for user in nama:
                    print(simbol)
                    kuantitas = int(input(f"{user} memesan berapa jenis barang: "))
                    for i in range(kuantitas):
                        barang = input(f"Barang {user} yang ke-{i+1}: ")
                        kuantitas = int(input(f"Beli berapa {barang}: "))
                        harga = float(input(f"Harga {barang}: "))
                        print(simbol)
                        pesanan.append({
                            "nama": user, 
                            "barang": barang,
                            "kuantitas":kuantitas, 
                            "harga": harga})
                
                total_harga = sum(item["harga"] * item["kuantitas"] for item in pesanan)
            break 
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
        
    while True: 
        split = total_harga / len(nama)
        print(f"Totalnya: Rp{total_harga:,.2f}")
        print(simbol)
        data = f"{'No':<4}|{'Nama':<10}|{'Barang':<16}|{'Harga & Kuantitas':<16}|{'Total/barang'}"
        print(data)
        print('-' * len(data))
        for i, item in enumerate (pesanan, start=1):
            barang_kuantitas = item['harga'] * item['kuantitas']
            harga_x_qty = f"{item['harga']:,.2f} x{item['kuantitas']}"
            print(f"{i:<4}|{item['nama']:<10}|{item['barang']:<16}|{harga_x_qty:<16}|{barang_kuantitas:,.2f}")  
        print(simbol) 
        print(f"{'Totalnya:':} Rp{total_harga:,.2f}")
        print(f"{'Bayar/org:'} Rp{split:,.2f}")
        validasi = input("Apakah ingin hitung ulang? (y/n): ")
        if validasi.lower() == "n":
            print("Program dihentikan!")
            for hitung in [3, 2, 1]:
                sleep(1)
                print(f"...{hitung}")
            print("Thanks🙌")
            exit()
        elif validasi.lower() == "y":
            return split_bill()
        else:
            print("Hanya input y/n")
             
split_bill()