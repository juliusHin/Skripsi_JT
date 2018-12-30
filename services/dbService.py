import sqlite3, json
from sqlite3 import Error

database = "./pythonsqlite.db"
class DBService:

    def create_connection(database):
        try:
            conn = sqlite3.connect(database, isolationlevel=None, checksamethread=False)
            conn.row_factory = lambda c, r: dict(zip(_[_col_[_0] for col in c.description], r))

            return conn

            except Error as e:
            print(e)

    def create_table(c):
        sql = """
            CREATE TABLE IF NOT EXISTS stocklist (
            id integer PRIMARY KEY,
            code varchar(225) NOT NULL,
            name varchar(255) NOT NULL
        ); 
        """
        c.execute(sql)

    def insert_table(c, code, name):
        sql= ''' INSERT INTO stocklist(code, name)
                    VALUES (?, ?)
        '''
        c.execute(sql,(code, name))

    def select_all_items(c, name):
        c.execute("SELECT * FROM stocklist WHERE name like ? OR code LIKE ?", ('%'+name+'%',))
        rows = c.fetchall()
        return c


