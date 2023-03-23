from tkinter import END, messagebox
import sqlite3


class ToDoList:

    def __init__(self, frame):
        self.frame = frame
        self.scroll_list = self.frame.add_scroll_list_on_frame(25, 7, 3, 0, 0)
        self.entry = self.frame.add_entry_on_frame(20, 2, 9, 1)
        self.add_button = self.frame.add_button_on_frame("ADD TASK", lambda: self.add_item(), 11, 1)
        self.delete_button = self.frame.add_button_on_frame("DELETE TASK", lambda: self.delete_item(), 11, 2)

        # initialize SQLITE database
        self.init_sql()
        self.execute_query(0, None)

    @staticmethod
    def init_sql():
        # if database present: connect to db, else: create db first, then connect
        connector = sqlite3.connect('TaskPlanner.db')

        # a "middleman" which executes the queries
        cursor = connector.cursor()

        # create a table in the db (if it does not exist)
        # in this case: Table with only one row named Task
        table_create_query = '''CREATE TABLE IF NOT EXISTS Tasks (Name TEXT)'''

        # execute a certain query
        cursor.execute(table_create_query)

        # commit before closing, to save changes
        connector.commit()

        # connection must be closed
        connector.close()

    def execute_query(self, query_option, task):
        connector = sqlite3.connect('TaskPlanner.db')
        cursor = connector.cursor()
        value = (task,)  # iterable

        try:
            # depending on what query_option was chosen, execute it; 0= read, 1= create, 2= delete
            if query_option == 0:
                read_query = ''' SELECT * FROM Tasks'''
                cursor.execute(read_query)
                result = cursor.fetchall()
                for res in result:
                    self.scroll_list.insert(END, res)
            elif query_option == 1:
                insert_query = '''INSERT INTO Tasks(Name) Values(?)'''
                cursor.execute(insert_query, value)
            elif query_option == 2:
                delete_query = '''DELETE FROM Tasks WHERE Name=(?)'''
                cursor.execute(delete_query, value)
            else:
                pass

            connector.commit()
            connector.close()

        except:
            messagebox.showerror("Faulty SQLite", "Something went wrong! ")
            connector.commit()
            connector.close()

    def add_item(self):
        entry_text = self.entry.get()
        if len(entry_text) < 3:
            messagebox.showwarning("Invalid Input", "At least 3 Letters!")
        else:
            self.scroll_list.insert(END, entry_text)
            self.entry.delete(0, END)
            self.execute_query(1, entry_text)

    def delete_item(self):
        selection = self.scroll_list.curselection()
        if len(selection) == 0:
            messagebox.showwarning("Invalid Action", "Please select Task to delete first!")
        else:
            task = self.scroll_list.get(selection[0])
            self.scroll_list.delete(selection)
            self.execute_query(2, task[0])
