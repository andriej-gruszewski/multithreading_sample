class Receipt:

    def __init__(self, shop, client):
        self.checkout_list = []
        self.shop = shop
        self.client = client
        self.total_cost = 0

    def print_receipt(self):
        receipt_string = f"Thank you for shopping in {self.shop.get_name()} \n"
        for item_dict in self.checkout_list:
            receipt_string += item_dict["product"] + " : " + str(item_dict["price"]) + "\n"
        print(receipt_string + f"Total cost: {self.total_cost}")

    def add_product_dict_to_receipt(self, product_dict):
        self.checkout_list.append(product_dict)
        return self.checkout_list

    def add_to_total_cost(self, product_price):
        self.total_cost += product_price
        return self.total_cost
