import os
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("All Files", "*.*")])
    listbox.delete(0, tk.END)
    for file_path in file_paths:
        listbox.insert(tk.END, file_path)

def delete_files():
    selected_items = listbox.curselection()
    if not selected_items:
        messagebox.showwarning("Warning", "No files selected!")
        return

    for index in selected_items:
        file_path = listbox.get(index)
        try:
            os.remove(file_path)
            listbox.delete(index)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete file: {e}")

app = tk.Tk()
app.title("File Deleter")

frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE, width=40, height=10)
listbox.pack(side=tk.LEFT, padx=10, pady=10)

scrollbar = tk.Scrollbar(frame, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

browse_button = tk.Button(app, text="Browse Files", command=browse_files)
browse_button.pack(padx=20, pady=10)

delete_button = tk.Button(app, text="Delete Selected Files", command=delete_files)
delete_button.pack(pady=10)

app.mainloop()
