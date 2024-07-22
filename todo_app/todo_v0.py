tasks=[]
while True:
    print("Perintah: add, delete, show, exit")
    command = input("Masukkan perintah: ")
    if command =="add":
        task = input("Masukkan tugas: ")
        tasks.append(task)
    elif command == "delete":
        task_index=int(input("Masukkan nomor tugas yang akan dihapus: "))
        if 0<=task_index <len(tasks):
            tasks.pop(task_index)
    elif command == "show":
        for idx, task in enumerate(tasks):
            print(f"{idx+1}. {task}")
    elif command == "exit":
        break
    else:
        print("Perintah tidak valid")

