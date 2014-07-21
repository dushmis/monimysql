class MoniError:    
  def __init__(self,msg):
    self.message = msg
    
  def __repr__(self):
    return "MoniError: %s" % self.message