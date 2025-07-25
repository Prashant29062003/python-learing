import json

path = 'youtube_videos.txt'
def load_data():
    try:
        with open(path, 'r') as file:
            test = json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(path, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print('\n')
    print("*" * 70)
    print('\n')
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print('\n')
    print("*" * 70)

def add_video(videos):
    name = input("Enter the video name: ")
    time = input("Enter the video name: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the video new name : ")
        time = input("Enter the video new time : ")
        videos[index - 1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid video Index.")


def delete_video(video):
    list_all_videos(videos)
    index = int(input("Enter video number to delete: "))

    if 1 <= index <= len(videos):
        del videos[index - 1]
    else: 
        print("Invalid Video index.")
def main():
    videos = load_data()

    # Ask questions continously until user selects exit
    while True:
        print("\n Youtube Manager | Choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")

        choice = input("Enter your choice: ")
        # print(videos)
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice.")

if __name__ == "__main__":
    main()
