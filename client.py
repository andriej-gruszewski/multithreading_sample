import random


class Client:

    def __init__(self, name, no_shop_list_items, shop):
        self.name = name
        self.no_shop_list_items = no_shop_list_items
        self.shopping_list = []
        self.shopping_list_product_number = []
        self.shop = shop
        self.receipt = None

    def create_product_list(self):
        available_products = self.shop.get_products_list()
        product_list = random.sample(available_products, k=self.no_shop_list_items)
        return product_list

    def create_shopping_list(self):
        product_list = self.create_product_list()
        for product in product_list:
            product_quantity_stock = self.shop.get_quantity_by_product(product)
            product_dict = {"product": product, "quantity": random.randint(1, 3)}
            if int(product_dict["quantity"]) >= product_quantity_stock:
                if product_quantity_stock == 0:
                    continue
                else:
                    product_dict = {"product": product, "quantity": product_quantity_stock}
                    self.shopping_list.append(product_dict)
                    self.shop.set_quantity_by_product(product_dict["product"], 0)
            else:
                self.shopping_list.append(product_dict)
                shop_left_quantity = product_quantity_stock - product_dict["quantity"]
                self.shop.set_quantity_by_product(product_dict["product"], shop_left_quantity)
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
