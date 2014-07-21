import re
import time
import ansicolor;

class moni:

  pid="";user="";host="";db="";command="";time="";state="";query="";
  color=ansicolor.ansicolor()
  
  def __log__(self,log):
    print '[ ' + time.strftime("%d-%b-%Y %r") + ' ] ' + self.color._okgreen() + log.__str__() + self.color._endc()

  def __warn__(self,log):
    print '[ ' + time.strftime("%d-%b-%Y %r") + ' ] ' + self.color._warning() + log.__str__() + self.color._endc()

  def __error__(self,log):
    print '[ ' + time.strftime("%d-%b-%Y %r") + ' ] ' + self.color._fail() + log.__str__() + self.color._endc()

  def get_time(self):
    return str(time.strftime("%d-%b-%Y--%r"))
    
  def __init__(self,row):
    self.pid      =   row[0]
    self.user     =   row[1]
    self.host     =   row[2]
    self.db       =   row[3]
    self.command  =   row[4]
    self.time     =   row[5]
    self.state    =   row[6]
    if row[7]:
      self.query    =   re.sub(r'[\s\r\t]+',' ',row[7])
    else:
      self.query = None
    
  def knownhost(self):
    return ( re.search("webcast:[0-9]*",self.host) or re.search("www.youbroadband.in:[0-9]*",self.host))
    
  def isselectquery(self):
    return (re.search("select.*",self.query)) 
    
  def valkill(self):
    return self.time > 25 and self.knownhost() and self.command=="Query" and self.isselectquery()
    
  def killem(self,connection):
    if self.valkill():
      self.__error__(self)
      #print "must kill %s" % (self.pid)
    
  def __str__(self):
    return "{ %s, %s, %s, %s, %s, %s, %s, %s }" % ( self.pid, self.user, self.host, self.db, self.command, self.time, self.state, self.query );
    
  #without query
  def string(self):
    return "{ %s, %s, %s, %s, %s, %s, %s}" % ( self.pid, self.user, self.host, self.db, self.command, self.time, self.state);
    
