tasks=[]

def get_user_command():
    print("Perintah: add, delete, show, exit")
    command = input("Masukkan perintah: ")
    return command

def get_task_detail():
    task = input("Masukkan tugas: ")
    return task

def display_tsaks(tasks):
    for idx, task in enumerate(tasks):
        print(f"{idx+1}. {task}")

def add_task(task):
    tasks.append(task)

def delete_task(task_index):
    if 0<=task_index <len(tasks):
        tasks.pop(task_index)

def get_all_tasks():
    return tasks

def main():
    while True:
        command=get_user_command()
        if command =="add":
            task = get_task_detail()
            add_task(task)
        elif command == "delete":
            task_index=int(input("Masukkan nomor tugas yang akan dihapus: "))
            delete_task(task_index)
        elif command == "show":
            tasks = get_all_tasks()
            display_tsaks(tasks)
        elif command == "exit":
            break
        else:
            print("Perintah tidak valid")

if __name__ == "__main__":
    main()