import sqlite3

connection = sqlite3.connect('jardinero.db')
cursor = connection.cursor()

class HarvestBE:
        # create harvest table
    harvest_table = """CREATE TABLE IF NOT EXISTS
            harvest(harvest_id INTEGER PRIMARY KEY,
            harvest_units INTEGER,
            harvest_weights INTEGER,
            harvest_weight_unit TEXT,
            date_completed TEXT NOT NULL,
            plant_id INTEGER NOT NULL, 
            FOREIGN KEY(plant_id) REFERENCES main(plant_id)
            )"""

    # cursor.execute(harvest_table)
    # connection.commit()

    # function read from frontend
    def harvest_save_data(self, harvest_units, harvest_weights, harvest_weight_unit, date, plant_id):
        """Save the data in the database from GUI entries."""
        connection = sqlite3.connect("jardinero.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO \
                harvest(harvest_units, harvest_weights, harvest_weight_unit, date_completed, plant_id) \
                VALUES (?, ?, ?, ?, ?)", (harvest_units, harvest_weights, harvest_weight_unit, date, plant_id))
        connection.commit()
        
