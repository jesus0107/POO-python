from app.login.user import User
# from app.login.role import Role
from app.inventory.product import Product

user = User("Jesus", "passwors")

user.purchased_products(Product("Pelota", "descrpcion", 234))
user.purchased_products(Product("Pelota2", "descrpcion2", 134))

print(user.print_info())