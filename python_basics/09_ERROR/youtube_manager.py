import json

def load_data():
    try:
        with open("youtube.txt",'r') as file:
            test=json.load(file)
            print(test)
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_of_videos(videos):
    print("\n")
    print("*"*50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, duration: {video['time']}")
    print("\n")
    print("*"*50)

def add_video(videos):
    name=input("enter name :")
    time=input("enter time: ")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_of_videos(videos)
    index=int(input("Enter the index for which you want to update: "))
    if 1<= index <= len(videos):
        new_name=input("enter new name of video: ")
        new_time=input("Enter new time duration for video: ")
        videos[index-1]={'name':new_name,'time':new_time}
        save_data_helper(videos)
    else:
        print("Invalid index. Enter valid index! ")


def delete_video(videos):
    list_of_videos(videos)
    index=int(input("Enter index to delete index: "))

    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Enter valid index! ")

def main():
    videos=load_data()
    while True:
        print("\n YouTube Manager ")
        print("1 list a fav video")
        print("2 Add a youtube video")
        print("3 update youtube video")
        print("4 delete video from list")
        print("5 Exit app")
        choice=input("Enter your choice")
        print(videos)

        match choice:
            case "1":
                list_of_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Enter valid option: ")

    
if __name__=="__main__":
    main()