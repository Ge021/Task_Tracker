import sqlite3

def add_task():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    task = input("What task would you like to add? ")
    search = c.execute('SELECT * FROM tasks WHERE taskDescription = ?', (task,)).fetchone()

    if search:
        if task.lower() == search[1].lower():
            print("Task already exists")

    else:
        c.execute('INSERT INTO tasks (taskDescription, taskStatus) VALUES (?, ?)', (task, "To be done"))
        print("Task added successfully")
        conn.commit()

    conn.close()

def see_all_tasks():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    tasks = c.execute('SELECT * FROM tasks').fetchall()

    for task in tasks:
        print(f"ID: {task[0]}\nTask Description: {task[1]}\nTask Status: {task[2]}\n")

    conn.close()

def delete_task():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    task = input("Please enter the ID of the task you wish to delete? ")
    search = c.execute('SELECT * FROM tasks WHERE taskID = ?', (task,)).fetchone()


    if search:
        if task == str(search[0]):
            c.execute('DELETE FROM tasks WHERE taskID = ?', (task,))
            print("Task deleted successfully")
            conn.commit()

        else:
            print("Task does not exist")

    conn.close()





if __name__ == '__main__':

    while True:
        choice = input('''A. Add a task\nB. Delete a task\nC. See all tasks\nD. Exit\nWhat would you like to do? ''')

        if choice.upper() == 'A':
            add_task()

        if choice.upper() == 'B':
            delete_task()

        if choice.upper() == 'C':
            see_all_tasks()

        if choice.upper() == 'D':
            break



