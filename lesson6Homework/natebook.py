import json
import os
from tabulate import tabulate
from datetime import datetime

class NoteBook():
    def __init__(self,NOTES_FILE):
        self.filename = NOTES_FILE
        if os.path.exists(NOTES_FILE):
            try:
                with open(NOTES_FILE, 'r') as f:
                    self.notes = json.load(f)
            except Exception as e:
                print(f"Error while loading notes: {e}")
                self.notes = []
        else:
            self.notes = []

    def load_notes(self):
        try:
            with open(self.filename, 'r') as f:
                self.notes = json.load(f)
        except Exception as e:
            print(f"Error while loading notes: {e}")
            self.notes = []

    def get_datetime(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def save_notes(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.notes, f, indent=4)
                print("QUIT!", end="")
        except Exception as e:
            print(f"Error while saving notes: {e}")
        


    def shorten_text(self,onedict: dict,length:int = 10):
        """if len(onedic["text"]) <= length:
            return onedic["text"]
        else:
            return onedic["text"][:length-3] + "..." + onedic["text"][len(onedic["text"])-5]"""
        return onedict["text"] if len(onedict["text"]) <= length else onedict["text"][:length-3] + "..." + onedict["text"][len(onedict["text"])-5]
        

    def show_menu(self):
        print("--------------------------")
        print("CHOOSE OPTION")
        print("1: SHOW ALL NOTES")
        print("2: SHOW NOTE DETAILS")
        print("3: CREATE NOTE")
        print("4: UPDATE NOTE")
        print("5: DELETE NOTE")
        print("Q: QUIT THE APPLICATION")
        print("M: SHOW MENU AGAIN")
        print("--------------------------")


    def show_all_notes(self):
        if self.notes:
            table = [[note["id"], self.shorten_text(note,13),str(note["Date"])] for note in self.notes]
            print(tabulate(table, headers=["id", "text","Creation_Date"], tablefmt="grid"))
        else:
            print("No notes found")

    def show_note_details(self):
        try:
            note_id = int(input("Enter note ID: "))
            note = next((note for note in self.notes if note["id"] == note_id), None)
            if note:
                print(f"ID: {note['id']}")
                print(f"Text: {note['text']}")
                print(f"Creation Date: {note['Date']}")
            else:
                print("Note not found.")
        except ValueError:
            print("Invalid ID. Please enter a valid integer.")

    def create_note(self):
        text = input("Enter note text: ")
        new_id = max([note["id"] for note in self.notes], default=0) + 1
        self.notes.append({"id": new_id, "text": text,"Date":self.get_datetime()})
        print("Note added")

    def update_note(self):
        try:
            note_id = int(input("Enter note ID to update: "))
            note = next((note for note in self.notes if note["id"] == note_id), None)
            if note:
                new_text = input("Enter new text: ")
                self.notes[note_id]["text"] = new_text
                self.notes[note_id]["Date"] = self.get_datetime()
                print("Note updated.")
            else:
                print("Note not found.")
        except ValueError:
            print("Invalid ID. Please enter a valid integer.")

    def delete_note(self):
        note_id = int(input("Enter note ID to delete: "))
        self.notes = [note for note in self.notes if note["id"] != note_id]
        print("Note deleted")


    def __str__(self):
        self.load_notes()
        self.show_menu()
        while True:
            choice = input("Choice: ").strip().upper()
            if choice == "1":
                self.show_all_notes()
            elif choice == "2":
                self.show_note_details()
            elif choice == "3":
                self.create_note()
            elif choice == "4":
                self.update_note()
            elif choice == "5":
                self.delete_note()
            elif choice == "Q":
                self.save_notes()
                return ""
            elif choice == "M":
                self.show_menu()
            else:
                print("Invalid, try again")

birinchi = NoteBook("notes.json")
print(birinchi)

ikkinchi = NoteBook("notes2.json")
print(ikkinchi)