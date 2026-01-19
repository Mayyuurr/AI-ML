import sqlite3

conn=sqlite3.connect('youtube_manager.db')

cur=conn.cursor()

cur.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
            )
''')

def list_video():
    cur.execute("SELECT * FROM videos")
    for row in cur.fetchall():
        print(row)

def add_video(name,time):
    cur.execute("INSERT INTO videos (name,time) VALUES (?,?)",(name,time))
    conn.commit()

def update_video(id,new_name,new_time):
    cur.execute("UPDATE videos SET name=?, time=? WHERE id=?",(new_name,new_time,id))
    conn.commit()

def del_video(id):
    cur.execute("DELETE FROM videos WHERE id=?",(id,))
    conn.commit()

def main():

    while True:

        
        print("Enter the Choice: ")
        print("1. list videos")
        print("2. add videos")
        print("3. update videos")
        print("4. delete videos")
        print("5. Exit ")
        choice=input("Enter the option: ")
        
        if choice=="1":
            list_video()
        elif choice=="2":
            name=input("Enter the name: ")
            time=input("Enter time duration for video: ")
            add_video(name, time)
        elif choice=="3":
            id=input("Enter Id to update")
            name=input("Enter the new name: ")
            time=input("Enter time duration for updtaed video: ")
            update_video(id,name,time)
        elif choice=="4":
            id=input("Enter the Id to delete: ")
            del_video(id)
        elif choice=="5":
            break
        else:
            print("Enter valid option!")


    conn.close()

if __name__=="__main__":
    main()