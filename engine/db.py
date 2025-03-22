# use for those apps which cannot directly open on it

import sqlite3   # sqlite3 is a package which is directly stored in python package

con=sqlite3.connect("jarvis.db")
cursor=con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)


#we comment it bcoz if we again run it,then it will create the duplicate entries in our db 

# query = "INSERT INTO sys_command VALUES (null,'powerpoint', 'C:\Program Files\Microsoft Office\root\Office16.POWERPNT.exe')"
# cursor.execute(query)
# con.commit()

# query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# cursor.execute(query)

# query = "INSERT INTO web_command VALUES (null,'notessolve', 'https://notesolves.hideandseekapps.com/material')"
# cursor.execute(query)
# con.commit()

# testing module
# app_name = "one note"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
# results = cursor.fetchall()
# print(results[0][0])
# Create a table with the desired columns
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')