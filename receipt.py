class Receipt:

    def __init__(self, shop, client):
        self.checkout_list = []
        self.shop = shop
        self.client = client
        self.total_cost = 0

    def print_receipt(self):
        receipt_string = f"Thank you for shopping in {self.shop.get_name()} \n"
        for item_dict in self.checkout_list:
            receipt_string += item_dict["product"] + " : " + str(item_dict["quantity"]) + " x " + str(item_dict["price"]) + "$" + "\n"
        print(receipt_string + f"Total cost: {self.total_cost}$")

    def add_product_dict_to_receipt(self, product_dict):
        product_price = self.shop.get_price_by_product(product_dict["product"])
        product_dict["price"] = product_price
        self.checkout_list.append(product_dict)
        self.add_to_total_cost(product_price, product_dict["quantity"])
        return self.checkout_list, self.total_cost

    def add_to_total_cost(self, product_price, quantity):
        self.total_cost += product_price * quantity
        return self.total_cost
