import sqlite3
conn = sqlite3.connect('catcovid.db')


def createtable(conn: sqlite3.Connection):
    conn.execute('''
            CREATE TABLE IF NOT EXISTS catcovid  
            (data text, regiosanitariacodi text, regiosanitariadescripcio text, sectorsanitaricodi text, sectorsanitaridescripcio text, abscodi text
            , absdescripcio text, sexecodi text, sexedescripcio, resultatcoviddescripcio text, numcasos real )

        ''')

def addrecord(conn: sqlite3.Connection, region):
    print("en metodo addrecord")
    sql = "INSERT INTO %s (%s) VALUES(%s)" % (
            "catcovid", ",".join(region.keys()), ",".join(region.values()))

    sql = '''
            INSERT INTO catcovid 
            (data , regiosanitariacodi , regiosanitariadescripcio , sectorsanitaricodi , sectorsanitaridescripcio , abscodi, 
            absdescripcio , sexecodi , sexedescripcio, resultatcoviddescripcio , numcasos )
            VALUES 
            (:data , :regiosanitariacodi , :regiosanitariadescripcio , :sectorsanitaricodi , :sectorsanitaridescripcio , :abscodi, 
            :absdescripcio , :sexecodi , :sexedescripcio, :resultatcoviddescripcio , :numcasos )
    '''
    print("imprimim data %s", region["data"])
    print(sql)
    cur = conn.cursor()
    cur.execute(sql, region)
    conn.commit()
    return cur.lastrowid

# if __name__ == '__main__':
#     main()
