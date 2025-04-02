import sqlite3

connection = sqlite3.connect('jardinero.db')
cursor = connection.cursor()

class PotsizeBE:
        # create pot size table
    pot_size_table = """CREATE TABLE IF NOT EXISTS
            pot_size(pot_size_id INTEGER PRIMARY KEY,
            pot_size TEXT NOT NULL,
            pot_material TEXT NOT NULL,
            pot_shape TEXT NOT NULL,
            date_completed TEXT NOT NULL,
            plant_id INTEGER NOT NULL, 
            FOREIGN KEY(plant_id) REFERENCES main(plant_id)
            )"""

    # cursor.execute(pot_size_table)
    # connection.commit()

    # function read from frontend
    def pot_size_save_data(self, pot_size, pot_material, pot_shape, date, plant_id):
        """Save the data in the database from GUI entries."""
        connection = sqlite3.connect("jardinero.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO \
                pot_size(pot_size, pot_material, pot_shape, date_completed, plant_id) \
                VALUES (?, ?, ?, ?, ?)", (pot_size, pot_material, pot_shape, date, plant_id))
        connection.commit()

        
