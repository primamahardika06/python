import socket
from time import sleep
PC_NAME = socket.gethostname()

def welcome_message():
    star = "*" * (len(PC_NAME) + 6)
    print(star)
    print(f"***{PC_NAME}***")
    print(star)
    
def exit_program():
    print(" Program akan dihentikan")
    sleep(1)
    print(" ...3")
    sleep(1)
    print(" ...2")
    sleep(1)
    print(" ...1")
    sleep(1)
    print(" Program Dihentikan")
    exit()
       
    
            
if __name__ == "__main__":
    welcome_message()
    exit_program()
    
