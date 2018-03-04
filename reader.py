import sqlite3
conn = sqlite3.connect('recipes.db')

c = conn.cursor()

for recipe in c.execute('SELECT * FROM recipes'):
    print recipe
