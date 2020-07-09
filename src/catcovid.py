import requests
import json
import coviddb
import sqlite3


def main():
    urlremote = "https://analisi.transparenciacatalunya.cat/resource/xuwf-dxjd.json"
    req = requests.get(urlremote)
    print("HTTP Status Code: " + str(req.status_code))
    print(req.headers)
    json_array = json.loads(req.content)

    conn = sqlite3.connect("catcovid.db")
    coviddb.createtable(conn)
 
    for i in json_array:
       coviddb.addrecord(conn,i)
    

if __name__ == '__main__':
    main()

