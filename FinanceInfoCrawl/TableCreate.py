import psycopg2

def create_tables(tab):
    """ create tables in the PostgreSQL database"""
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
        conn = psycopg2.connect(database='postgres', user='postgres', port=5433, password='1234')
        cur = conn.cursor()
        # create table one by one
        cur.execute(commands % tab)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables('test')