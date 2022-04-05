


class Cliente(object):
  name = None
  last_name = None
  age = 0
  balance = 0.0
  
  def __init__(self, name: str = "N/A", last_name: str= "N/A", age: int = 0, balance: float = 0.0):
    self.name = name
    self.last_name = last_name
    self.age = age
    self.balance = balance
    
  def __str__(self):
    return "({0}) ({1}) ({2}) ({3})".format(self.name, self.last_name, self.age, self.balance)