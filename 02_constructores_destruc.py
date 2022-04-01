
class Computer:
  ram: int = 0
  capacity: int = 0
  brand: str = None
  
  def __init__(self, brand, capacity, ram):
    print(f"Accediendo a constructor de la pc {brand}")
    self.ram = ram
    self.capacity = capacity
    self.brand = brand
  
  def print_info_pc(self):
    print(
      f"La marca de la computadora es: {self.brand} \nLa capacidad de almacenamiento es: {self.capacity} \nLa capacidad de la ram es: {self.ram}"
      )
  
  def __del__(self):
    print(f"Eliminamos a la pc {self.brand}")
  
class Person:
  first_name: str = None
  last_name: str = None
  age: int = 0
  addres: str = None
  computer: Computer = None
  
  def __init__(self, first_name:str, last_name:str, age:int, addres:str, brand:str, capacity:int, ram:int):
    print(f"---- Accediendo al constructor de la persona {first_name}")
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.addres = addres
    self.computer = Computer(brand, capacity, ram)
  
  def print_info(self):
    print(f"Mi nombre es: {self.first_name} {self.last_name} \n Mi edad es de {self.age} anos")
    self.computer.print_info_pc()
  
  def __del__(self):
    print(f"---- Eliminando el objeto... {self.first_name}")

def main():
  my_person = Person("Jesus", "Cruz", 27, "Nuestra seniora de la paz", "Asus", 256, 16)
  print("\n")
  my_person.print_info()
  print("\n")
  
  print("---Instruccion antes de destruir objetos")
  
if __name__ == "__main__":
  main()
  print("---instruccion despues de destruir objetos")
  