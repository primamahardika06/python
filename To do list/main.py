import os

if __name__ == "__main__":
    system_os = os.name
    
    match system_os:
        case "nt":
            os.system("cls")
            


def menu():
    tasks= []
    while True:
        opsi = int(input("Chose option below: \n 1). Create task \n 2). Show task \n 3). Delete task \n 4). Quit \n Your option: "))
        if opsi == 1:
            task = input("Input your task: ")
            time = (input("Deadline: "))
            tasks.append({
                "task":task,
                "time": time
            })
        elif opsi == 2:
            if not tasks:
                print("data not found")
            else:
                header = f"{'No':<4}|{'Task':<14}|{'Deadline'}" 
                print(header)
                for i,  item in enumerate (tasks, start=1):
                    print(f"{i:<4}|{item['task']:<14}|{item['time']}")
        elif opsi == 3:
            task = int(input("Delete task number: "))
            if 1 <= task <= len(tasks):
                delete = tasks.pop(task - 1)
                print(f"Delete has been deleted")
            else:
                print("Invalid task number!")

        elif opsi == 4:
            print("Bye!")
            break

        else:
            print("Invalid option, try again!")
        
        
menu()
