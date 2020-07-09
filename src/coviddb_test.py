import sqlite3
import json
import unittest
import coviddb

class TestStringMethods(unittest.TestCase):

    

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_insert(self):
        jsonvar  = '''
 {"data":"2020-07-04:00:00.000","regiosanitariacodi":"7801","regiosanitariadescripcio":"Metropolità Sud","sectorsanitaricodi":"7866","sectorsanitaridescripcio":"Baix Llobregat Centre-Litoral i l'Hospitalet de Llobregat","abscodi":"261","absdescripcio":"Vallirana","sexecodi":"0","sexedescripcio":"Home","resultatcoviddescripcio":"Sospitós","numcasos":"3"}
        '''
        jsonobj = json.loads(jsonvar)
        print(jsonobj)
        coviddb.addrecord(self.conn, jsonobj)
        self.assertEqual("261",jsonobj["abscodi"], "miramos el abscodi")
        

    def test_createtabe(self):
        coviddb.createtable(self.conn)
        self.assertTrue(self.conn)
        
    
    def setUp(self):
        self.conn = sqlite3.connect('catcovidtest.db')
        


if __name__ == '__main__':
    unittest.main()
