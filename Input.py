import sqlite3

class Input:
    def __init__(self, action):
        self.action = action

    def setting(self):
        self.action["state"] = "disabled"
        conn = sqlite3.connect('daily_earning.db')
        print("Opened database successfully")
        try:
            conn.execute('''CREATE TABLE DAILY_EARNING_CHART
                 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 DESCRIPTION    TEXT (50)   NOT NULL,
                 EARNING    TEXT  NOT NULL,
                 TYPE TEXT NOT NULL,
                 LOCATION TEXT NOT NULL,
                 TIME   TEXT NOT NULL);''')
        except:
            pass

        self.action["state"] = "enable"

        conn.close()

    def submit(self,description, earning): # Insert values into earning table
        self.action["state"] = "disabled"
        self.description = description
        self.earning = earning
        try:
            sqliteConnection = sqlite3.connect('daily_earning.db')
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")

            sqlite_insert_query = "INSERT INTO DAILY_EARNING_CHART (DESCRIPTION,EARNING,TIME) VALUES ('" + self.description + "','"+ self.earning + "',datetime('now', 'localtime'))"

            count = cursor.execute(sqlite_insert_query)
            sqliteConnection.commit()
            print("Record inserted successfully into DAILY_EARNING_CHART table", cursor.rowcount)
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert earning data into sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()
            self.action["state"] = "enable"