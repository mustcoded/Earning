import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

class Input:
    def __init__(self):
        pass

    def setting(self):

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

        conn.close()

    def submit(self,description, earning, location, cc): # Insert values into earning table

        self.description = description
        self.earning = earning
        self.location = location
        self.cc = cc
        try:
            sqliteConnection = sqlite3.connect('daily_earning.db')
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            sqlite_insert_query = "INSERT INTO DAILY_EARNING_CHART (DESCRIPTION,EARNING,TYPE, LOCATION, TIME) VALUES ('" + self.description + "','"+ self.earning +  "','" + self.cc +  "','" + self.location + "',datetime('now', 'localtime'))"
            count = cursor.execute(sqlite_insert_query)
            sqliteConnection.commit()
            print("Record inserted successfully into DAILY_EARNING_CHART table", cursor.rowcount)
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert earning data into sqlite table", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()

    def plot(self, location, cc, month): # plotting the bar chart
        plt.clf() #this is uses to clear the previous graph plot
        # dictionary uses to print out the month within header of the graph
        monthdict = {'01':'January', '02':'Febuary', '03':'March', '04':'April', '05':'May', '06' : 'June', '07':'July', '08':'August', '09':'September', '10':'October', '11':'November', '12':'December'}
        try:
            shoe_dict = {'Baby Girl' : 0.00, 'Baby Boy' : 0.00, 'Boy':0.00, 'Girl':0.00, 'Man':0.00, 'Woman':0.00}
            shirt_dict = {'T-Shirt':0.00, 'School Uniform':0.00, 'Baby Cloth':0.00, 'Jacket':0.00, 'Blouse':0.00, 'Pajamas':0.00}
            sqliteConnection = sqlite3.connect('daily_earning.db')
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
            if cc=='All Items':
                cursor.execute("SELECT * FROM DAILY_EARNING_CHART WHERE LOCATION=?", (location,))
            else:
                cursor.execute("SELECT * FROM DAILY_EARNING_CHART WHERE TYPE=? AND LOCATION=?", (cc, location))
            rows = cursor.fetchall()

            for row in rows:
                if(row[5].split('-')[1]) == month:

                    if cc=="Shoe":
                        shoe_dict[row[1]] += float(row[2])
                    elif cc=="Shirt":
                        shirt_dict[row[1]] += float(row[2])
                    elif cc=="All Items":
                        if row[1] in shoe_dict:
                            shoe_dict[row[1]] += float(row[2])
                        else:
                            shirt_dict[row[1]] += float(row[2])
            # dictionary for the graph axis
            label_x = []
            label_y = []

            if cc=="Shoe":
                for key, value in shoe_dict.items():
                    label_x.append(key)
                    label_y.append(value)
            elif cc=="Shirt":
                for key, value in shirt_dict.items():
                    label_x.append(key)
                    label_y.append(value)
            else:
                for key, value in shirt_dict.items():
                    label_x.append(key)
                    label_y.append(value)
                for key, value in shoe_dict.items():
                    label_x.append(key)
                    label_y.append(value)
            # begin plotting the bar chart
            s = pd.Series(index=label_x, data=label_y)
            s.plot(color="green", kind="bar", title = cc + " Sales for " + monthdict[month] +  " at " + location)
            plt.show()

        except sqlite3.Error as error:
            print("Failed to plot earning data", error)
        finally:
            if (sqliteConnection):
                sqliteConnection.close()