import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3 as sql

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append((task_string, 0))
        the_cursor.execute('INSERT INTO tasks (title, completed) VALUES (?, ?)', (task_string, 0))
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task, completed in tasks:
        display_text = f"[{'✔' if completed else ' '}] {task}"
        task_listbox.insert('end', display_text)

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        selected_task = tasks[selected_index]
        tasks.pop(selected_index)
        the_cursor.execute('DELETE FROM tasks WHERE title = ?', (selected_task[0],))
        list_update()
    except IndexError:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box:
        tasks.clear()
        the_cursor.execute('DELETE FROM tasks')
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def update_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task, completed = tasks[selected_index]
        tasks[selected_index] = (task, 1 - completed)
        the_cursor.execute('UPDATE tasks SET completed = ? WHERE title = ?', (1 - completed, task))
        list_update()
    except IndexError:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Update.')

def retrieve_database():
    tasks.clear()
    for row in the_cursor.execute('SELECT title, completed FROM tasks'):
        tasks.append((row[0], row[1]))

def close():
    the_connection.commit()
    the_cursor.close()
    guiWindow.destroy()

if __name__ == "__main__":
    guiWindow = tk.Tk()
    guiWindow.title("To-Do App")
    guiWindow.geometry("500x450+750+250")
    guiWindow.resizable(False, False)
    guiWindow.configure(bg="black")

    the_connection = sql.connect('listofTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT, completed INTEGER)')
    tasks = []

    header_frame = tk.Frame(guiWindow, bg="black")
    functions_frame = tk.Frame(guiWindow, bg="black")
    listbox_frame = tk.Frame(guiWindow, bg="black")

    header_frame.pack(fill="both")
    functions_frame.pack(side="left", expand=True, fill="both")
    listbox_frame.pack(side="right", expand=True, fill="both")

    header_label = ttk.Label(
        header_frame,
        text="To-Do List",
        font=("Brush Script MT", 30),
        background="black",
        foreground="white",
    )
    header_label.pack(padx=20, pady=20)

    task_label = ttk.Label(
        functions_frame,
        text="Enter The Task:",
        font=("Consolas", 11, "bold"),
        background="black",
        foreground="white",
    )
    task_label.place(x=30, y=40)

    task_field = ttk.Entry(
        functions_frame,
        font=("Consolas", 12),
        width=18,
    )
    task_field.place(x=30, y=80)

    add_button = ttk.Button(
        functions_frame,
        text="Add Task",
        width=24,
        command=add_task,
    )
    add_button.place(x=30, y=120)

    del_button = ttk.Button(
        functions_frame,
        text="Delete Task",
        width=24,
        command=delete_task,
    )
    del_button.place(x=30, y=160)

    del_all_button = ttk.Button(
        functions_frame,
        text="Delete All Tasks",
        width=24,
        command=delete_all_tasks,
    )
    del_all_button.place(x=30, y=200)

    update_button = ttk.Button(
        functions_frame,
        text="Mark as Completed",
        width=24,
        command=update_task,
    )
    update_button.place(x=30, y=240)

    exit_button = ttk.Button(
        functions_frame,
        text="Exit",
        width=24,
        command=close,
    )
    exit_button.place(x=30, y=280)

    task_listbox = tk.Listbox(
        listbox_frame,
        width=26,
        height=13,
        selectmode='SINGLE',
        background="#1c1c1c",
        foreground="white",
        selectbackground="gray",
        selectforeground="black",
    )
    task_listbox.place(x=10, y=20)

    retrieve_database()
    list_update()

    guiWindow.mainloop()



