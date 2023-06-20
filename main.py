import pickle
import random
import uuid

class Note():
    def __init__(self, title,content):
        self.title = title
        self.content = content
        self.id = uuid.uuid4()
    
    def __repr__(self):
        return f"The contents of this note are title: '{self.title}', content: '{self.content}'."
      
      
      
      
 class Notebook():
    
    def __init__(self):
        self.notes = []
    
    def __repr__(self):
        return f"This is a simple Python program that use built to explore the pickle library. The premise here is that you can create notes, delete them, store them on your local disk, and load them when necessary."
    
    def __len__(self):
        return len(self.notes)
    
    def add_note(self,title,content):
        note = Note(title,content)
        self.notes.append(note)
    
    def show_ids(self):
        for note in self.notes:
            print({"id":note.id})
    
    def find_note(self, target_id):
        lookup_id = uuid.UUID(target_id)
        for note in self.notes:
            if note.id == lookup_id:
                obj = {"title":note.title, "content":note.content}
                return obj
        return None
    
    ''' Save Notes to your local Disk'''
    def save_notes(self):
        with open("notes.pickle", 'wb') as file:
            pickle.dump(self.notes,file)
    
    def load_notes(self):
        try:
            with open("notes.pickle", "rb") as file:
                self.notes = pickle.load(file)
            print("Notes loaded successfully.")
        except FileNotFoundError:
            print("No saved notes file found.")
        except Exception as e:
            print("Error occurred while loading notes:", str(e))
            
    def find_saved_notes(self,path):
        import os
        files = os.listdir(path)
        for file in files:
            if file.endswith(".pickle"):
                return f"a saved note file exists in this directory"
            
    def delete_note(self, target_id):
        lookup_id = uuid.UUID(target_id)
        for note in self.notes:
            if note.id == lookup_id:
                return f"note id: {note.id} with the properties title: {note.title} and {note.content} has been deleted successfully!"
        return None


