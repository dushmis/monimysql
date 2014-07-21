from error import MoniError

try:
    import MySQLdb
except:
    raise MoniError("Missing Package: MySQLdb")

class connection:

  def __init__(self,myhost,myuser,mypasswd,mydb):
    try:
      self.db = MySQLdb.connect(host=myhost,user=myuser,passwd=mypasswd,db = mydb)
    except MySQLdb.OperationalError, oe:
      raise MoniError("Database error %s" % str(oe))
    self.cursor = self.db.cursor()

  def executeQuery(self,qstring):
    self.cursor.execute(qstring)
    return self.cursor.fetchall()
    
  def close(self):
    self.cursor.close()
    self.db.close()
    