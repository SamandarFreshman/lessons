import os
from dotenv import load_dotenv
from checker import is_it_new,should_it_be_updated
from recording import recording
from storing_created_tables import load_from_file,save_to_file

load_dotenv()

sql_source = os.environ.get('SQL_SOURCE')
notes = load_from_file()
try:
    for file in os.listdir(sql_source):
        try:
            if file.endswith('.csv'):

                file_path = os.path.join(sql_source, file)
                table_name = os.path.splitext(file)[0].replace('-', '_').replace(' ', '_')
                notes = is_it_new(file_path, table_name,notes)

        except Exception as e:
            recording(f"Error: {e}")
except FileNotFoundError:
    recording(f"file {sql_source} not found")
except Exception as e:
    recording(f"Error: {e}")
save_to_file(notes)