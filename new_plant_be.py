import sqlite3

connection = sqlite3.connect('jardinero.db')
cursor = connection.cursor()

class NewplantBE:
    # create main table
    main_table = """CREATE TABLE IF NOT EXISTS
            main(plant_id INTEGER PRIMARY KEY,
            name TEXT,
            main_catagory TEXT,
            sub_catagory TEXT,
            quantity INTEGER NOT NULL,
            date_of_birth TEXT NOT NULL,
            classification TEXT,
            per_ann TEXT,
            seed_class TEXT)"""

    #cursor.execute(main_table)
    #connection.commit()

    # function read from frontend
    def new_plant_save_data(name, main_catagory, sub_catagory, quantity, date_of_birth, classification, per_ann, seed_class):
        """Save the data in the database from GUI entries."""
        connection = sqlite3.connect("jardinero.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO \
                main (name, main_catagory, sub_catagory, quantity, date_of_birth, classification, per_ann, seed_class) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (name, main_catagory, sub_catagory, quantity, date_of_birth, classification, per_ann, seed_class))
        connection.commit()

        
