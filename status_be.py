import sqlite3

connection = sqlite3.connect('jardinero.db') 
cursor = connection.cursor()

class StatusBE:
    # create status table # add after set up goes in the gap # 
    # status_table = """CREATE TABLE IF NOT EXISTS
    #         status(status_id INTEGER PRIMARY KEY,
    #         date_completed TEXT NOT NULL,
    #         plant_id INTEGER NOT NULL, 
    #         FOREIGN KEY(plant_id) REFERENCES main(plant_id),
    #         rooting INTEGER NOT NULL,
    #         sprouting INTEGER NOT NULL,
    #         growing INTEGER NOT NULL,
    #         flowering INTEGER NOT NULL,
    #         harvesting INTEGER NOT NULL,
    #         dormant INTEGER NOT NULL,
    #         quarantine INTEGER NOT NULL,
    #         dead INTEGER NOT NULL,
    #         rating INTEGER NOT NULL)"""

    # cursor.execute(status_table)
    # connection.commit()

    # function read from frontend
    def status_save_data(self, date_ver, plant_id_ver, rooting, sprouting, growing, flowering, harvesting, dormant, quarantine, dead, rating_ver_int):
        """Save the data in the database from GUI entries."""
        connection = sqlite3.connect("jardinero.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO \
            status(date_completed, plant_id, rooting, sprouting, growing, flowering, harvesting, dormant, quarantine, dead, rating) \
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (date_ver, plant_id_ver, rooting, sprouting, growing, flowering, harvesting, dormant, quarantine, dead, rating_ver_int))
        connection.commit()
