class logger:
  self.f=None
  def __init__(self,file):
    //nothing
    self.f=open(file,"a")
    
  def log(