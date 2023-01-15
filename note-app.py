import tkinter as tk
import sqlite3

class NoteApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Note App")
        self.root.geometry('620x300')
        



if __name__ == "__main__":
    # create app instance
    app = NoteApp()
    # run app
    app.root.mainloop()