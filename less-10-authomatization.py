import MySQLdb
import peewee


def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


db = MySQLdb.connect(host='localhost', user='dbuser', db='imdb', connect_timeout=5, charset='utf8')
cursor = db.cursor() # represent a database cursor, which is used to manage the context of fetch operation
cursor.execute("SELECT VERISION()")
data = cursor.fetchone()
print("Database verdion: ", data)
cursor.execute('SELECT * FROM Reviewer')
print(dictfetchall(cursor))
cursor.close()
db.close()

def query(self, sql):
    try:
        self.conn.ping()
    except:
        self.connect()
        with closing(self.conn.cursor()) as cursor:
            cursor.execute(sql)
            return self.dictfetchall(cursor)