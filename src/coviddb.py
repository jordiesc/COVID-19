import sqlite3
conn = sqlite3.connect('catcovid.db')

def createtable():
    conn.execute('''
            CREATE TABLE catcovid 
            (data text, tregiosanitariacodi text, regiosanitariadescripcio text, sectorsanitaricodi text, sectorsanitaridescripcio text, abscodi text
            , absdescripcio text, sexecodi text, sexedescripcio, resultatcoviddescripcio text, numcasos real )

        ''')

def addrecord(conn: sqlite3.Connection,**region):
        sql = '''
            INSERT INTO catcovid 
            (data , tregiosanitariacodi , regiosanitariadescripcio , sectorsanitaricodi , sectorsanitaridescripcio , abscodi 
            absdescripcio , sexecodi , sexedescripcio, resultatcoviddescripcio , numcasos l )
        '''

        cur = conn.cursor()
        cur.execute(sql, region)
        return cur.lastrowid

if __name__ == '__main__':
    main()
