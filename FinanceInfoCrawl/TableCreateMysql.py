import pymysql

def create_tables(tab):
    """ create tables in the SQL database"""
    commands ="""
        CREATE TABLE %s (
            date DATE PRIMARY KEY NOT NULL,
            Open INT,
            High INT,
            Low INT,
            Close INT,
            Volume INT,
            Adj_Close FLOAT
            )
        """
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = pymysql.connect(database='kospi', user='root', port=3306, password='1234')
        cur = conn.cursor()
        # create table one by one
        cur.execute(commands % tab)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, pymysql.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def showtable(db):
    pass



if __name__ == '__main__':
    create_tables('test')