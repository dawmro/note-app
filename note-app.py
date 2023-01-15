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
        
        # create the "notes" table if it doesn't exist
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS notes 
                            (topic TEXT, note TEXT, timestamp TEXT)''')
        self.conn.commit()
        



if __name__ == "__main__":
    # create app instance
    app = NoteApp()
    # run app
    app.root.mainloop()