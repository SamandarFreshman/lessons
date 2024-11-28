import pandas as pd
from create_table import create_table
from recording import recording

def is_it_new(file_path,table_name,notes):
    try:
        if not table_name in [name["table_name"] for name in notes]:
            recording(f"New table {table_name} was detected")
            df = pd.read_csv(file_path, on_bad_lines='skip')
            num_of_rows = df.shape[0]
            create_table(file_path, table_name)

            new_id = max([note["id"] for note in notes], default=0) + 1
            notes.append({"id": new_id,"table_name":table_name,"number_of_rows": num_of_rows})
            recording(f"Table {table_name} added to created tables\n\n\n")
    except Exception as e:
        recording(f"Error: {e}")

    return notes


def should_it_be_updated(file_path,table_name,notes):
    df = pd.read_csv(file_path,on_bad_lines='skip')
    num_of_rows = df.shape[0]

    for name in notes:
        try:
            if name["table_name"] == table_name and name["number_of_rows"] != num_of_rows:
                recording(f"Table {table_name} has been updated. Updating the database")
                create_table(df, table_name)
                note_id = name["id"]
                notes[note_id]["number_of_rows"] = num_of_rows
        except Exception as e:
            recording(f"Error: {e}")
    return notes