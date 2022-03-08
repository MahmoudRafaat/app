import sqlite3

conn = sqlite3.connect('patient.db')
query = (''' CREATE TABLE PATIENT
            (NAME           TEXT    NOT NULL,
            AGE            INT     NOT NULL,
            EMAIL        CHAR(50));''')
conn.execute(query)
conn.close()
