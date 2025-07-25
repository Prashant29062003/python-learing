import json
import time

path = "work_manager.txt"
def load_data():
    try:
        with open(path, 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(work_data):
    with open(path, 'w') as file:
        json.dump(work_data,file)


def list_all_data(work_data):
    print('\n')
    print("*" * 70)
    for index, work in enumerate(work_data, start=1):
        print(f"{index}. {work['time_alter']} ==> {work['name']}, {work['time']}")
    print("\n")
    print("*" * 70)

def add_work(work_data):
    curr_time = time.ctime()
    name = input("Enter the work name: ")
    time_to_complete = input("Enter time to complete: ")
    work_data.append({'time_alter': curr_time, 'name': name, 'time': time_to_complete})
    save_data_helper(work_data)

def update_work(work_data):
    list_all_data(work_data)
    index = int(input("Enter work number to update: "))
    if 1 <= index <= len(work_data):
        curr_time = time.ctime()
        name = input(f"Enter your 'new' name of work-{index}: ")
        time = input(f"Enter your 'new' time of work-{index}: ")
        work_data[index-1] = {'time_alter': curr_time, 'name': name, 'time': time}
        save_data_helper(work_data)
    else:
        print("Invalid work number!")

def delete_work(work_data):
    list_all_data(work_data)
    index = int(input("Enter work number to delete: "))
    if 1 <= index <= len(work_data):
        del work_data[index-1]
    else:
        print("Invalid work number!")
        


def main():
    work_data = load_data()
    while True:
        print("\nWork Manager Choose onpe option: ")
        print("1. Display all tasks ")
        print("2. Add today's task ")
        print("3. Update any task ")
        print("4. Delete any task ")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_data(work_data)
            case '2':
                add_work(work_data)
            case '3':
                update_work(work_data)
            case '4':
                delete_work(work_data)
            case '5':
                break
            case _:
                print("Invalid Choice!")

if __name__ == '__main__':
    main()
