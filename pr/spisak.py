import sqlite3

con = sqlite3.connect('music_db.sqlite')

cur = con.cursor()

result = cur.execute(
    f"""select name from artist where artistid in (select artistid from album where
     albumid in (select albumid from track where genreid in(select genreid from genre where name = '{input()}'))) 
     order by name""").fetchall()
for elem in result:
    print(elem[0])
con.close()
