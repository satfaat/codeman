import sqlite3

sqlite3.version
sqlite3.version_info
sqlite3.sqlite_version
sqlite3.sqlite_version_info

conn = sqlite3.connect('ssi.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM protek_samara ORDER BY full_name'):
    print(row)
