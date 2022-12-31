class Receipt:

    def __init__(self, shop, client):
        self.checkout_list = []
        self.shop = shop
        self.client = client
        self.total_cost = 0

    def scan_items(self):
        client_shopping_list = self.client.get_shopping_list()
        for product in client_shopping_list:
            product_dict = {
                "product": product,
                "price": self.shop.get_price_by_product(product)
            }
            self.checkout_list.append(product_dict)
            self.total_cost += product_dict["price"]

    def print_receipt(self):
        receipt_string = f"Thank you for shopping in {self.shop.get_name()} \n"
        for item_dict in self.checkout_list:
            receipt_string += item_dict["product"] + " : " + str(item_dict["price"]) + "\n"
        print(receipt_string + f"Total cost: {self.total_cost}")

    def add_product_to_receipt(self, product):
        self.checkout_list.append(product)
        return self.checkout_list
