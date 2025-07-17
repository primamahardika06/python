import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'pywarung'
)

def reset_barang():
    cursor = db.cursor()
    cursor.execute("DELETE FROM tbl_barang")
    cursor.execute("ALTER TABLE tbl_barang AUTO_INCREMENT = 1")
    db.commit()
    print("\n Semua barang berhasil dihapus dan ID direset.")
  
  
    
def delete_item(id_barang):
    cursor = db.cursor()
    cursor.execute("DELETE FROM tbl_barang WHERE id = %s", (id_barang,))
    db.commit()
    if cursor.rowcount > 0:
        print("\n Barang berhasil dihapus.")
    else:
        print("\n Barang dengan ID tersebut tidak ditemukan.")
        


def insert_item (kode_barang, nama_barang, harga_barang, stok_barang):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl_barang (kode_barang, nama_barang, harga_barang, stok_barang) VALUES (%s, %s, %s, %s)", (kode_barang, nama_barang, harga_barang,  stok_barang))
    db.commit()
    if cursor.rowcount > 0:
        print("\n Data berhasil ditambahkan!")
    else:
        print("\n Data gagal ditambahkan!")
       
       
        
def fetch_item():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tbl_barang")
    return cursor.fetchall()