import sqlite3

conn = sqlite3.connect('Inclass.db')
c = conn.cursor()

# c.execute("""
#           CREATE TABLE IF NOT EXISTS Students (
#               id INTEGER PRIMARY KEY,
#               name TEXT NOT NULL,
#               age INTEGER NOT NULL,
#               grade INTEGER NOT NULL
#           )""")

# c.execute("""CREATE TABLE IF NOT EXISTS Phon_numbers (
#             student_id INTEGER,
#             number TEXT NOT NULL,
#             FOREIGN KEY (student_id) REFERENCES Students(id)
#             )""")

# c.executemany("INSERT INTO Students (name, age, grade) VALUES (?,?,?)", [
#     ('John Doe', 18, 12),
#     ('Jane Smith', 17, 11),
#     ('Bob Johnson', 19, 10)
#     ])

# c.executemany("INSERT INTO Phon_numbers (student_id, number) VALUES (?,?)", [
#     (1, '123-456-7890'),
#     (2, '987-654-3210'),
#     (3, '555-555-5555')
#     ])

c.execute("SELECT * FROM Phon_numbers")
print(c.fetchmany(2))
# print(c.fetchall())

conn.commit()
conn.close()