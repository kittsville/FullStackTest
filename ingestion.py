import sqlite3
conn = sqlite3.connect('recipes.db')

c = conn.cursor()

# Create table
c.execute('CREATE TABLE recipes (name text, url text, preptime integer)')

# Insert a rows of data
c.execute("INSERT INTO recipes VALUES ('Lasagne', 'lasagne', 120)")
c.execute("INSERT INTO recipes VALUES ('Toast', 'toast', 12)")
c.execute("INSERT INTO recipes VALUES ('Bacon', 'bacon', 90)")

# Save (commit) the changes
conn.commit()

print 'Saved 3 recipes to the database'

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
