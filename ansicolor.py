class ansicolor:
  header = '';okblue = '';okgreen = '';warning = '';fail = '';endc = ''
  
  def __init__(self):
    self.header = '\033[95m'
    self.okblue = '\033[94m'
    self.okgreen = '\033[92m'
    self.warning = '\033[93m'
    self.fail = '\033[91m'
    self.endc = '\033[0m'
  
  def _header(self):
    return self.header;
    
  def _okblue(self):
    return self.okblue;
    
  def _okgreen(self):
    return self.okgreen;
    
  def _warning(self):
    return self.warning;
    
  def _fail(self):
    return self.fail;
    
  def _endc(self):
    return self.endc;