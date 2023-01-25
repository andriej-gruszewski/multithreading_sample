import json
import unittest


class Shop:

    def __init__(self, filename, name):
        file = open(filename)
        self.products = json.load(file)
        file.close()
        self.name = name

    def get_name(self):
        return self.name

    def get_products_list(self):
        products_dict = self.products["products"]
        products_list = [list["product"] for list in products_dict]
        return products_list

    def get_price_by_product(self, product_name):
        products_dict = self.products["products"]
        for product_item in products_dict:
            if product_item["product"] == product_name:
                return product_item["price"]

    def set_quantity_by_product(self, product_name, quantity):
        products_dict = self.products["products"]
        for product_item in products_dict:
            if product_item['product'] == product_name:
                product_item['quantity'] = quantity
                return product_item

    def get_quantity_by_product(self, product_name):
        products_dict = self.products["products"]
        for product_item in products_dict:
            if product_item['product'] == product_name:
                return product_item['quantity']




class UnitTest(unittest.TestCase):

    def setUp(self):
        self.shop = Shop("products_list.json", "Aldi")

    def test_get_products_list(self):
        products_list = self.shop.get_products_list()
        self.assertEqual(len(products_list) != 0, True)

    def test_get_empty_products_list(self):
        shop2 = Shop("products_list2.json", "Aldi")
        products_list = shop2.get_products_list()
        self.assertEqual(len(products_list) != 0, False)

    def test_if_list_contains_strings(self):
        products_list = self.shop.get_products_list()
        for product in products_list:
            self.assertIsInstance(product, str)

    def test_type_of_list(self):
        products_list = self.shop.get_products_list()
        self.assertIsInstance(products_list, list)
