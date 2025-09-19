from . import db
from .util import random_string
import time
import os

def delete(no_buku):
    print(no_buku)
    try:
        with (open(db.DB_NAME, 'r')) as file:
            counter = 0
            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with open("data_temp.txt" , 'a', encoding="utf-8") as temp_file:
                        temp_file.write(content)
                content += 1
    except:
        print("database eror")
        
    os.rename("data_temp.txt", db.DB_NAME)



def update(no_buku,pk,date_add,penulis,judul,tahun_terbit):
    data = db.TEMPLATE.copy()
    
    data["pk"] = pk
    data["date_add"] = date_add
    data["penulis"] = penulis + db.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + db.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun_terbit)
    
    data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, { data["tahun"]}\n'
    
    data_length = len(data_str)
    
    try:
        with(open(db.DB_NAME, 'r+', encoding="utf-8")) as file:
            file.seek(data_length*(no_buku-1))  
            file.write(data_str)   
    except:
        print("eror dlm update data")



def create(penulis,judul,tahun_terbit):
    data = db.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + db.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + db.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun_terbit)
    
    data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, { data["tahun"]}\n'
    print(data_str)
    
    try:
        with open(db.DB_NAME,'a', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("gagal menambahkan data!")



def create_first_data():
    
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while True:
            try:
                tahun_terbit = int(input("Tahun terbit: "))
                if len(str(tahun_terbit)) == 4:
                    break
                else: 
                    print("Tahun harus menggunakan angka (yyyy)!!")    
            except:
                print("Tahun harus menggunakan angka (yyyy)!!")
        
    
    data = db.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis + db.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + db.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun_terbit)
    
    data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, { data["tahun"]}\n'
    print(data_str)
    
    try:
        with open(db.DB_NAME,'w', encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("gagal")
 
 
        
def read(**kwargs):
    try:
        with open (db.DB_NAME, 'r') as file:
            content = file.readlines() 
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"] - 1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else: 
                    return content[index_buku]
            else:
                return content
    except:
        print("database eror")
        return False
  
    
   