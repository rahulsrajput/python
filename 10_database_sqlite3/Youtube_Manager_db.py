import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')


def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name,time):
    cursor.execute('INSERT INTO videos (name,time) VALUES(?,?)',(name,time))
    conn.commit()



def update_video(video_id,name,time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    conn.commit()


def delete_video(video_id):
    cursor.execute('DELETE FROM videos WHERE id = ?', (video_id,))
    conn.commit()


def main():
    while True:
        print('\nYoutube Manager App DB')
        print('1. List all videos')
        print('2. Add videos')
        print('3. Update videos')
        print('4. Delete videos')
        print('5. Exit App')
        choice = input('Enter your choice: ')
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input('enter video name: ')
            time = input('enter video time: ')
            add_video(name,time)
        elif choice == '3':
            video_id = input('enter video id to update: ')
            name = input('enter video name: ')
            time = input('enter video time: ')
            update_video(video_id,name,time)
        elif choice == '4':
            video_id = input('Enter video ID to delete: ')
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print('Invalid choice')

    conn.close()

if __name__ == '__main__':
    main()
