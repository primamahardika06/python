import main
from service import db

def add():
    kode_barang = input(" Masukkan kode barang: ")
    nama_barang = input(" Masukkan nama barang: ")
    harga_barang= int(input(" Masukkan harga barang: "))
    stok_barang = int(input(" Masukkan stok barang: "))
    
    db.insert_item(kode_barang, nama_barang, harga_barang, stok_barang)
    
def check():
    items = db.fetch_item()
    for item in items:
        id_barang = item[0]
        kode_barang = item[1]
        nama_barang = item[2]
        harga_barang = item[3]
        stok_barang = item[4]
        print(f'''
 Barang ke-{id_barang}
 Kode ({kode_barang})
 {nama_barang} | Rp. {harga_barang}
 Stok: {stok_barang}          
''')
        
def reset():
    db.reset_barang()
    
def delete():
    id_barang = int(input("\n Masukkan id brang yang ingin dihapus: "))
    db.delete_item(id_barang)

def update():
    id_barang = int(input("\n Masukkan ID barang yang ingin di-update: "))
    kode_baru = input(" Masukkan kode barang baru: ")
    nama_baru = input(" Masukkan nama barang baru: ")
    harga_baru = int(input(" Masukkan harga barang baru: "))
    stok_baru = int(input(" Masukkan stok barang baru: "))

    db.update_barang(kode_baru, nama_baru, harga_baru, stok_baru, id_barang)
    
    
def start(): 
    while True: 
        menu = int(input("\n Opsi pilihan: \n 1). Tambah barang \n 2). Cek barang \n 3). Reset Barang \n 4). Delete Barang \n 5). Update \n 6). Kembali \n Silahakan pilih: "))
        if menu == 1:
            add()
        elif menu == 2:
            check()
        elif menu == 3:
            reset()
        elif menu == 4:
            delete()
        elif menu == 5:
            update()
        elif menu == 6:
            main.menu()
        else:
            print("Hanya dapat memilih opsi diatas")
        
if __name__ == "__main__":
    start()