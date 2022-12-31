import random

class Client:

    def __init__(self, name, no_shop_list_items, shop):
        self.name = name
        self.no_shop_list_items = no_shop_list_items
        self.shopping_list = []
        self.shopping_list_product_number = []
        self.shop = shop
        self.receipt = None

    def create_shopping_list(self):
        available_products = self.shop.get_products_list()
        self.shopping_list = random.sample(available_products, k=self.no_shop_list_items)
        return self.shopping_list

    def get_shopping_list(self):
        return self.shopping_list

    def get_shopping_list_product_number(self):
        return self.shopping_list_product_number

    def get_receipt(self):
        return self.receipt

    def set_receipt(self, receipt):
        self.receipt = receipt
        return self.receipt

    def get_name(self):
        return self.name
