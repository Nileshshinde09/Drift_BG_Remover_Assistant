

import sqlite3
import random
import string
from constants.ano_names import ANO_NAMES

class ImageNameGenerator:
    def __init__(self, db_path='database/names.db'):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()
# ----------------------------------------------------------------------------------------------------------------------------------
    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS unique_names (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE,
                is_original INTEGER
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS used_names (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE
            )
        ''')
        self.conn.commit()
# ----------------------------------------------------------------------------------------------------------------------------------
    def delete_unique_names_table(self):
        self.cursor.execute("DELETE FROM unique_names")

    def delete_used_names_table(self):
        self.cursor.execute("DELETE FROM used_names")
# ----------------------------------------------------------------------------------------------------------------------------------
    def add_unique_name(self, name, is_original):
        try:
            self.cursor.execute('INSERT INTO unique_names (name, is_original) VALUES (?, ?)', (name, is_original))
            self.conn.commit()
            print(f"Added '{name}' to unique names successfully.")
        except sqlite3.IntegrityError:
            print(f"'{name}' already exists in unique names.")

    def add_used_name(self, name):
        try:
            self.cursor.execute('INSERT INTO used_names (name) VALUES (?)', (name,))
            self.conn.commit()
            print(f"Added '{name}' to unique names successfully.")
        except sqlite3.IntegrityError:
            print(f"'{name}' already exists in unique names.")
# ----------------------------------------------------------------------------------------------------------------------------------
    def show_all_original_names(self):
        self.cursor.execute('SELECT name FROM unique_names WHERE is_original = 1')
        original_names = self.cursor.fetchall()
        return [name[0] for name in original_names] if original_names else []

    def show_all_used_names(self):
        self.cursor.execute('SELECT name FROM used_names')
        used_names = self.cursor.fetchall()
        return [name[0] for name in used_names] if used_names else []
# ----------------------------------------------------------------------------------------------------------------------------------
    def generate_random_string(self, length=5):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))
# ----------------------------------------------------------------------------------------------------------------------------------
    def is_name_unique(self, name):
        self.cursor.execute('SELECT name FROM used_names WHERE name = ?', (name,))
        result = self.cursor.fetchone()
        if result:
            return False  # Name is not unique
        else:
            return True   # Name is unique
# ----------------------------------------------------------------------------------------------------------------------------------
    def get_random_unique_name(self):
        original_names = self.show_all_original_names()
        if original_names:
            while True:
                random_name = random.choice(original_names)
                if self.is_name_unique(random_name):
                    self.add_used_name(random_name)
                    return random_name + '.png'
                else:
                    random_name = random_name + '_' + self.generate_random_string()
                    if self.is_name_unique(random_name):
                        self.add_used_name(random_name)
                        return random_name + '.png'
                    else:
                        continue
# ----------------------------------------------------------------------------------------------------------------------------------
    def insert_unique_ano_names(self):
        for name in ANO_NAMES:
            try:
                self.add_unique_name(name, 1)
            except Exception as e:
                print(e)
                continue

    def __del__(self):
        self.conn.close()

# # ----------------------------------------------------------------------------------------------------------------------------------
## Testing Code
generator = ImageNameGenerator()

"""
for _ in range(200): 
    print(generator.get_random_unique_name())
print(generator.show_all_used_names())
"""

## Delete table data    
"""
generator.delete_unique_names_table()
generator.delete_used_names_table()
"""    
## Insert Unique Ano_Names in to the Table
"""
generator.insert_unique_ano_names()
"""

# Show all Tables
"""
print("*************************Unique Names*************************")
print(generator.show_all_used_names())
print("**************************Used Names**************************")
print(generator.show_all_original_names())
"""

# # ----------------------------------------------------------------------------------------------------------------------------------
# Code with functions


# import sqlite3
# import random
# import string
# from constants.ano_names import ANO_NAMES
# # Connect to the SQLite database
# conn = sqlite3.connect('database/names.db')
# cursor = conn.cursor()

# # Create table if not exists
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS unique_names (
#         id INTEGER PRIMARY KEY,
#         name TEXT UNIQUE,
#         is_original INTEGER
#     )
# ''')
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS used_names (
#         id INTEGER PRIMARY KEY,
#         name TEXT UNIQUE
#     )
# ''')
# conn.commit()

# # ----------------------------------------------------------------------------------------------------------------------------------
# #Function to delete data from the tables
# def delete_unique_names_table():
#     cursor.execute("DELETE FROM unique_names")
# def delete_used_names_table():
#     cursor.execute("DELETE FROM used_names")
# # ----------------------------------------------------------------------------------------------------------------------------------
# # Function to add unique names to the database
# def add_unique_name(name, is_original):
#     try:
#         cursor.execute('INSERT INTO unique_names (name, is_original) VALUES (?, ?)', (name, is_original))
#         conn.commit()
#         print(f"Added '{name}' to unique names successfully.")
#     except sqlite3.IntegrityError:
#         print(f"'{name}' already exists in unique names.")
# # ----------------------------------------------------------------------------------------------------------------------------------
# # Function to add name which is used by the image
# def add_used_name(name):
#     try:
#         cursor.execute('INSERT INTO used_names (name) VALUES (?)', (name,))
#         conn.commit()
#         print(f"Added '{name}' to unique names successfully.")
#     except sqlite3.IntegrityError:
#         print(f"'{name}' already exists in unique names.")

# # ----------------------------------------------------------------------------------------------------------------------------------

# # Function to show all original names in the database
# def show_all_original_names():
#     cursor.execute('SELECT name FROM unique_names WHERE is_original = 1')
#     original_names = cursor.fetchall()
#     return [name[0] for name in original_names] if original_names else []

# def show_all_used_names():
#     cursor.execute('SELECT name FROM used_names')
#     original_names = cursor.fetchall()
#     return [name[0] for name in original_names] if original_names else []

# # ----------------------------------------------------------------------------------------------------------------------------------

# # Function to generate a random string
# def generate_random_string(length=5):
#     letters = string.ascii_letters
#     return ''.join(random.choice(letters) for _ in range(length))
# # ----------------------------------------------------------------------------------------------------------------------------------
# # Function to check whether provided name is unique or not from the database
# def is_name_unique(name):
#     cursor.execute('SELECT name FROM used_names WHERE name = ?', (name,))
#     result = cursor.fetchone()
#     if result:
#         return False  # Name is not unique
#     else:
#         return True   # Name is unique

# # ----------------------------------------------------------------------------------------------------------------------------------    
# # Function to get a random original name from the database
# def get_random_unique_name():
#     original_names = show_all_original_names()
#     if original_names:
#         while 1:
#             random_name =  random.choice(original_names)
#             if(is_name_unique(random_name)):
#                 add_used_name(random_name)
#                 return random_name+'.png'
#             else:
#                 random_name = random_name + '_'+ generate_random_string()
#                 if(is_name_unique(random_name)):
#                     add_used_name(random_name)
#                     return random_name+'.png'
#                 else:
#                     continue
# # ----------------------------------------------------------------------------------------------------------------------------------
# # Function to insert unique anonymous values from constants/ano_names
# def insert_unique_ano_names():
#     for i in ANO_NAMES:
#         try:
#             add_unique_name(i, 1)
#         except Exception as e:
#             print(e)
#             continue

# # ----------------------------------------------------------------------------------------------------------------------------------

# ## Testing Code
# """
# for _ in range(200): 
#     print(get_random_unique_name())
# print(show_all_used_names())
# """

# ## Delete table data    
# """
# delete_unique_names_table()
# delete_used_names_table()
# """    

# # Show all Tables
# """
# print("*************************Unique Names*************************")
# print(show_all_used_names())
# print("**************************Used Names**************************")
# print(show_all_original_names())
# """

# conn.close()

