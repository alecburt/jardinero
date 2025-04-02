import sqlite3

connection = sqlite3.connect('jardinero.db')
cursor = connection.cursor()

class LocationBE:
        # create location table
    location_table = """CREATE TABLE IF NOT EXISTS
            location(loc_id INTEGER PRIMARY KEY,
            location TEXT NOT NULL,
            date_completed TEXT NOT NULL,
            plant_id INTEGER NOT NULL, 
            FOREIGN KEY(plant_id) REFERENCES main(plant_id)
            )"""

    # cursor.execute(location_table)
    # connection.commit()

    # function read from frontend
    def location_save_data(self, location, date, plant_id):
        """Save the data in the database from GUI entries."""
        connection = sqlite3.connect("jardinero.db")
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO location (location, date_completed, plant_id)
                       VALUES (?, ?, ?)''', (location, date, plant_id))
        connection.commit()

        
