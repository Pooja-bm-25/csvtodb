import psycopg2
import pandas as pd
import re
from datetime import date

# cursor = config.conn.cursor()
df = pd.read_csv('Emp-details.csv')
print(df)

hostname = 'localhost'
database = 'Emp-details'
username = 'postgres'
pwd = 'password'
port_id = '5432'

conn = psycopg2.connect(
    host=hostname,
    dbname=database,
    user=username,
    password=pwd,
    port=port_id
)
print(conn)
cursor = conn.cursor()
print("database opened successfully")


def readData(df):
    for i, row in df.iterrows():
        name = row.Name.split()
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(pat, row.Email):
            email_id = row.Email
        else:
            email_id = ""

        # date_of_birth = datetime.strptime(i.DateofBirth, "%m/%d/%Y")
        today = date.today()
        age = today.year - today.year - ((today.month, today.day) < (today.month, today.day))
        address = row.Address.split(" ")
        cursor.execute(
            '''INSERT INTO employee (firstname, lastname,email,age,city,state) VALUES (%s,%s,%s,%s,%s,%s); ''',
            (name[0], name[1], email_id, age, address[-2], address[4]))
        conn.commit()


data = readData(df)
print("details inserted successfully")
