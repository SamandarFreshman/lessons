import json
import os
from tabulate import tabulate
from datetime import datetime

NOTES_FILE = "notes.json"
notes = []

def get_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def load_notes():
    global notes
    if os.path.exists(NOTES_FILE):
        try:
            with open(NOTES_FILE, 'r') as f:
                # Debugging: Print loaded notes
                notes = json.load(f)
                return notes
        except Exception as e:
            print(f"Error while loading notes: {e}")
            return []
    else:
        return []
def save_notes(notes):
    try:
        with open(NOTES_FILE, 'w') as f:
            json.dump(notes, f, indent=4)
    except Exception as e:
        print(f"Error while saving notes: {e}")
def shorten_text(text, length=10):
    return text if len(text) <= length else text[:length-3] + "..." + text[len(text)-5]

def show_menu():
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


def show_all_notes():
    if notes:
        table = [[note["id"], shorten_text(note["text"]),str(note["Date"])] for note in notes]
        print(tabulate(table, headers=["id", "text","Creation_Date"], tablefmt="grid"))
    else:
        print("No notes found")

def show_note_details():
    try:
        note_id = int(input("Enter note ID: "))
        note = next((note for note in notes if note["id"] == note_id), None)
        if note:
            print(f"ID: {note['id']}")
            print(f"Text: {note['text']}")
            print(f"Creation Date: {note['Date']}")
        else:
            print("Note not found.")
    except ValueError:
        print("Invalid ID. Please enter a valid integer.")

def create_note():
    text = input("Enter note text: ")
    new_id = max([note["id"] for note in notes], default=0) + 1
    notes.append({"id": new_id, "text": text,"Date":get_datetime()})
    print("Note added")

def update_note():
    try:
        note_id = int(input("Enter note ID to update: "))
        note = next((note for note in notes if note["id"] == note_id), None)
        if note:
            new_text = input("Enter new text: ")
            note["text"] = new_text
            note["Date"] = get_datetime()  # Update the timestamp
            save_notes(notes)
            print("Note updated.")
        else:
            print("Note not found.")
    except ValueError:
        print("Invalid ID. Please enter a valid integer.")

def delete_note():
    note_id = int(input("Enter note ID to delete: "))
    global notes
    notes = [note for note in notes if note["id"] != note_id]
    print("Note deleted")


def main():
    load_notes()
    show_menu()
    while True:
        choice = input("Choice: ").strip().upper()
        if choice == "1":
            show_all_notes()
        elif choice == "2":
            show_note_details()
        elif choice == "3":
            create_note()
        elif choice == "4":
            update_note()
        elif choice == "5":
            delete_note()
        elif choice == "Q":
            save_notes(notes)
            print("QUIT!")
            break
        elif choice == "M":
            show_menu()
        else:
            print("Invalid, try again")

main()