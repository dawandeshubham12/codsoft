import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("520x400+550+250")
        self.root.resizable(0, 0)
        self.root.configure(bg="#f2f59a")

        self.tasks = []

        self.functions_frame = tk.Frame(root, bg="#f2f59a")
        self.functions_frame.pack(side="top", expand=True, fill="both")

        self.task_label = tk.Label(
            self.functions_frame,
            text="Add a Task:",
            font=("Arial", "14", "bold"),
            bg="#f2f59a",
            fg="black"
        )
        self.task_label.place(x=20, y=30)

        self.task_field = tk.Entry(
            self.functions_frame,
            font=("Arial", "14"),
            width=30,
            fg="black",
            bg="#d2def7",
        )
        self.task_field.place(x=160, y=30)

        self.add_button = tk.Button(
            self.functions_frame,
            text="Add Task",
            width=12,
            bg='#CD5C5C',
            font=("Arial", "13", "bold"),
            command=self.add_task,
        )
        self.del_button = tk.Button(
            self.functions_frame,
            text="Remove Task",
            width=12,
            bg='#CD5C5C',
            font=("Arial", "12", "bold"),
            command=self.remove_task,
        )
        self.del_all_button = tk.Button(
            self.functions_frame,
            text="Remove All",
            width=12,
            font=("Arial", "12", "bold"),
            bg='#CD5C5C',
            command=self.delete_all_tasks
        )

        self.exit_button = tk.Button(
            self.functions_frame,
            text="Exit",
            width=12,
            bg='#CD5C5C',
            font=("Arial", "12", "bold"),
            command=self.close
        )
        self.add_button.place(x=20, y=100)
        self.del_button.place(x=20, y=172)
        self.del_all_button.place(x=20, y=245)
        self.exit_button.place(x=20, y=320)

        self.task_listbox = tk.Listbox(
            self.functions_frame,
            width=36,
            height=12,
            font=("Arial", "12"),
            selectmode='SINGLE',
            bg="#d2def7",
            fg="black",
            selectbackground="#CD853F",
            selectforeground="black"
        )
        self.task_listbox.place(x=160, y=110)

        root.mainloop()

    def add_task(self):
        task_string = self.task_field.get()
        if len(task_string) == 0:
            messagebox.showinfo('Error', 'Field is Empty.')
        else:
            self.tasks.append(task_string)
            self.list_update()
            self.task_field.delete(0, 'end')

    def list_update(self):
        self.clear_list()
        for task in self.tasks:
            self.task_listbox.insert('end', task)

    def remove_task(self):
        try:
            the_value = self.task_listbox.get(self.task_listbox.curselection())
            if the_value in self.tasks:
                self.tasks.remove(the_value)
                self.list_update()
        except:
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

    def delete_all_tasks(self):
        message_box = messagebox.askyesno('Delete All', 'Are you sure?')
        if message_box:
            while(len(self.tasks) != 0):
                self.tasks.pop()
            self.list_update()

    def clear_list(self):
        self.task_listbox.delete(0, 'end')

    def close(self):
        self.root.destroy()

if __name__ == "__main__":
    guiWindow = tk.Tk()
    app = ToDoApp(guiWindow)
