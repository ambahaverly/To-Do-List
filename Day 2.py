import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime


def add_task():
    task_text = entry_task.get().strip()
    if task_text:
        priority = combo_priority.get()
        due_date = entry_due_date.get().strip()

        if due_date:
            try:
                due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
            except ValueError:
                messagebox.showerror("Error", "Invalid due date format. Please use YYYY-MM-DD.")
                return

        task = f"{priority} Priority: {task_text}"
        if due_date:
            task += f" (Due: {due_date})"

        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        entry_due_date.delete(0, tk.END)


def delete_task():
    try:
        selection = listbox_tasks.curselection()
        if selection:
            listbox_tasks.delete(selection)
    except tk.TclError:
        pass


root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")
root.configure(background='#FFC0CB')

style = ttk.Style()
style.configure('TButton', background='#FF69B4', foreground='white', font=("Helvetica", 10))
style.map('TButton', background=[('active', '#FF8C00')])

frame = ttk.Frame(root)
frame.pack(pady=20)

label_title = ttk.Label(frame, text="To-Do List", font=("Helvetica", 18), background='#FFC0CB')
label_title.grid(row=0, column=0, columnspan=3, pady=10)

listbox_tasks = tk.Listbox(frame, height=10, width=40, font=("Helvetica", 12), background='#FFE4E1', selectbackground='#FF8C00', foreground='black')

listbox_tasks.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox_tasks.yview)
scrollbar.grid(row=1, column=3, sticky=(tk.W, tk.N, tk.S))
listbox_tasks.config(yscrollcommand=scrollbar.set)

entry_task = ttk.Entry(frame, width=30, font=("Helvetica", 12))
entry_task.grid(row=2, column=0, padx=5, pady=10, sticky=(tk.W, tk.E))

label_priority = ttk.Label(frame, text="Priority:", font=("Helvetica", 12), background='#FFC0CB')
label_priority.grid(row=2, column=1, padx=5, pady=10, sticky=tk.E)

combo_priority = ttk.Combobox(frame, values=["High", "Medium", "Low"], width=8, font=("Helvetica", 12))
combo_priority.grid(row=2, column=2, padx=5, pady=10, sticky=tk.W)
combo_priority.current(1)

label_due_date = ttk.Label(frame, text="Due Date (YYYY-MM-DD):", font=("Helvetica", 12), background='#FFC0CB')
label_due_date.grid(row=3, column=1, padx=5, pady=10, sticky=tk.E)

entry_due_date = ttk.Entry(frame, width=15, font=("Helvetica", 12))
entry_due_date.grid(row=3, column=2, padx=5, pady=10, sticky=tk.W)

button_add_task = ttk.Button(frame, text="Add Task", width=10, command=add_task)
button_add_task.grid(row=4, column=0, padx=5, pady=10, sticky=(tk.W, tk.E))

button_delete_task = ttk.Button(frame, text="Delete Task", width=10, command=delete_task)
button_delete_task.grid(row=4, column=1, padx=5, pady=10, sticky=(tk.W, tk.E))

button_add_task.bind("<Enter>", lambda event: button_add_task.config(background='#FF8C00'))
button_add_task.bind("<Leave>", lambda event: button_add_task.config(background='#FF69B4'))
button_delete_task.bind("<Enter>", lambda event: button_delete_task.config(background='#FF8C00'))
button_delete_task.bind("<Leave>", lambda event: button_delete_task.config(background='#FF69B4'))

root.mainloop()
