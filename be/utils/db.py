import psycopg2


db = psycopg2.connect(host=app.config['DB_ADDRESS'], port=app.config['DB_PORT'] ,dbname=app.config['DB_NAME'], user=app.config['DB_USER'], password=app.config['DB_PASSWORD'])
cur = db.cursor()


def get_query_all(table):
    print('inside get query')
    cur.execute("select * from public.{}".format(table))
    records = cur.fetchall()
    return records

def get_query(table, name):
    print('inside get query')
    cur.execute("select * from public.{}".format(table, name))
    records = cur.fetchall()
    return records

def insert_query():
    cur.execute("insert to public.classes () values ()")
    records = cur.fetchall()
    return records