#!/usr/bin/python -tt

import re
from moni import moni
from connection import connection

def connect_db():
<<<<<<< HEAD
  return connection(myhost="myhost", myuser="myuser", mypasswd="mypasswd", mydb="mydb")
=======
  connector = MySQLdb.connect(host="IP", user="USER", passwd="PASSWORD", db="DB")
  return {"db":connector,"cur":connector.cursor()}
>>>>>>> 04caad04b0abd3b8a279d25358b4ab035c26817d
  
def get_list_pid():
  connector=connect_db()
  sql="show full processlist"
  for row in connector.executeQuery(sql):
    mon=moni(row)
    if mon.valkill():
      mon.killem(connector)
  connector.close()
  return list

def main():
  list=get_list_pid()
  
  
if __name__ == "__main__":
  main()
