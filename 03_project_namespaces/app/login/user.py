
from app.login.role import Role
from app.inventory.product import Product

class User:
  purchase_products = []
  role: Role
  username: str
  password: str
  
  def __init__(self, username:str, password:str):
    self.username = username
    self.password = password
    self.purchase_products = []
    self.role = Role("Client")
    
  def purchased_products(self, product: Product):
    self.purchase_products.append(product)
    # print(product.print_product_inf())

  def print_info(self):
    info = f"El usuario {self.username} con role {self.role.print_role()}, tiene los siguientes productos:\n"
    for product in self.purchase_products :
      info = info + f"Producto: \n{product.print_product_inf()}\n"
    return info
    
    

    