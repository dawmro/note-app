import tkinter as tk
import sqlite3

class NoteApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Note App")
        self.root.geometry('620x300')
        
        # create database connection
        self.conn = sqlite3.connect('notes.db')
        self.cursor = self.conn.cursor()
        



if __name__ == "__main__":
    # create app instance
    app = NoteApp()
    # run app
    app.root.mainloop()