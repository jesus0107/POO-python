class Role:
  role: str = ""
  
  def __init__(self, role):
    self.role = role
    
  def print_role(self):
    return f"Role: {self.role} "