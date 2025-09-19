import os
from operasi import operasi
from title.title import title

if __name__ == "__main__":
    system_os = os.name

    match system_os:
        case "nt": 
            os.system("cls")
               
def main():
    title()
    operasi.split_bill()

if __name__ == "__main__":
    main()