#!/usr/bin/python -tt

import MySQLdb
import re
from moni import moni

def connect_db():
  connector = MySQLdb.connect(host="IP", user="USER", passwd="PASS", db="DB")
  return {"db":connector,"cur":connector.cursor()}
  
def get_list_pid():
  list=[]
  connector=connect_db()
  sql="show full processlist"
  mycur=connector["cur"]
  mycur.execute(sql)
  for row in mycur.fetchall():
    mon=moni(row)
    if mon.valkill():
      mon.killem(mycur)
      list.append(mon)
  connector["cur"].close()
  connector["db"].close()
  return list

def main():
  list=get_list_pid()
  
  
if __name__ == "__main__":
  main()
