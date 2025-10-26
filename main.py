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



if __name__ == '__main__':

    while True:
        choice = input('''A. Add a task\nB. Delete a task\nC. See all tasks\nD. Exit\nWhat would you like to do? ''')

        if choice.upper() == 'A':
            add_task()

        if choice.upper() == 'B':
            pass

        if choice.upper() == 'C':
            pass

        if choice.upper() == 'D':
            break



