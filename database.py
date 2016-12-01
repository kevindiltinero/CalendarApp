import sqlite3

def calendartable():
    #Set up the connection to the database and the cursor
    conn = sqlite3.connect('calendar.db')
    c = conn.cursor()

    #Creating the table for the ABT
    c.execute('CREATE TABLE IF NOT EXISTS calendarevents (id INT, title TEXT, start TEXT, end TEXT)')

def event_writting(id, title, start, end):
    #Set up the connection.
    conn = sqlite3.connect('calendar.db')
    c = conn.cursor()
    #Consolidate into an array
    theevent = [id, title, start, end]
    # Write ABT into the Database
    c.execute('INSERT INTO calendarevents (id, title, start, end)'\
              'VALUES (?, ?, ?, ?)', theevent)
    conn.commit()

# calendartable()

event_writting(1, 'end of term', '123', '456')
