


def get_class(name):
    print('inside get class query')
    cur.execute("select * from public.classes")
    records = cur.fetchall()
    return records

def get_all_classes():
    print('inside get all classes query')
    cur.execute("select * from public.classes")
    records = cur.fetchall()
    return records




        

