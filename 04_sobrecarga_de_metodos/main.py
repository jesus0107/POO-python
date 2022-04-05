from app.sobrecarga_metds import Cliente

clientel = Cliente()
cliente2 = Cliente("Jose", "Aldama")
cliente3 = Cliente("Jose", "Aldama", 20,450.00)
cliente4 = Cliente("Jose","Aldama",300.00)
cliente5 = Cliente("Jose", "Aldama", 18)
cliente6 = Cliente(None, None, None, 500)


print(clientel)
print(cliente2)
print(cliente3)
print(cliente4)
print(cliente5)
print(cliente6)