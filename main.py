from cashier import Cashier
from shop import Shop
from client import Client


# creating new shop
shop = Shop("products_list.json", "NewShop")

# creating new clients separated in 2 lists
client1 = Client("John", 3, shop=shop)
client1.create_shopping_list()

client2 = Client("Andrew", 2, shop=shop)
client2.create_shopping_list()

client3 = Client("Patricia", 4, shop=shop)
client3.create_shopping_list()

client4 = Client("Mary", 6, shop=shop)
client4.create_shopping_list()

client5 = Client("Ashley", 2, shop=shop)
client5.create_shopping_list()

client6 = Client("Mark", 10, shop=shop)
client6.create_shopping_list()

customer_list1 = [client1, client2, client3]
customer_list2 = [client4, client5, client6]

# creating 2 cashiers
cashier1 = Cashier(1, 3, customer_list1, shop=shop)
cashier2 = Cashier(2, 2, customer_list2, shop=shop)

cashier1.start()
cashier2.start()



