class Product:
  title: str
  content: str
  price: int
  
  def __init__(self, title: str, content:str, price:int):
    self.title = title
    self.content = content
    self.price = price
    
  def print_product_inf(self):
    return f"producto: {self.title} \nContenido: {self.content} \nPrecio: {self.price}"