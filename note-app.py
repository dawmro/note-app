import tkinter as tk
from tkinter import ttk
import sqlite3
from datetime import datetime



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
        
        # create buttons
        self.topic_label = tk.Label(self.root, text="Topic:")
        self.topic_entry = tk.Entry(self.root)
        self.note_label = tk.Label(self.root, text="Note:")
        self.note_entry = tk.Entry(self.root)
        self.add_button = tk.Button(self.root, text="Add Note", command=self.add_note)
        
        # add GUI elements for results
        self.result_tree = ttk.Treeview(self.root, columns=('Timestamp','Topic', 'Note'), show='headings')
        self.result_tree.heading('Timestamp', text='Timestamp')
        self.result_tree.heading('Topic', text='Topic')
        self.result_tree.heading('Note', text='Note')
        self.result_tree.column('Timestamp', stretch=tk.YES)
        self.result_tree.column('Topic', stretch=tk.YES)
        self.result_tree.column('Note', stretch=tk.YES)
        self.result_tree.grid(row=6, column=0, columnspan=2)        
        
        # add GUI elements to the root window
        self.topic_label.grid(row=0, column=0, sticky='e')
        self.topic_entry.grid(row=0, column=1)
        self.note_label.grid(row=1, column=0, sticky='e')
        self.note_entry.grid(row=1, column=1)
        self.add_button.grid(row=2, column=1)
        
        # serach for notes at app start
        self.search_notes()

        
    # method for adding notes to database    
    def add_note(self):
        topic = self.topic_entry.get()
        note = self.note_entry.get()
        timestamp = datetime.now()

        # insert note and timestamp into "notes" table
        self.cursor.execute("INSERT INTO notes (topic,note,timestamp) VALUES (?, ?,?)", (topic, note,timestamp))
        self.conn.commit()

        # clear entry fields
        self.topic_entry.delete(0, tk.END)
        self.note_entry.delete(0, tk.END)
        
        
    def search_notes(self):
        # Delete all the existing rows in the Treeview
        for i in self.result_tree.get_children():
            self.result_tree.delete(i)

        # Retrieve all the notes and timestamps from the "notes" table
        self.cursor.execute("SELECT * FROM notes")
        notes = self.cursor.fetchall()

        # Insert each note and timestamp into the result_tree
        for note in notes:
            
            self.result_tree.insert("", tk.END, values = (note[2], note[0], note[1]))
        



if __name__ == "__main__":
    # create app instance
    app = NoteApp()
    # run app
    app.root.mainloop()