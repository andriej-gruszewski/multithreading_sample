import time
import threading
from receipt import Receipt


class Cashier(threading.Thread):

    def __init__(self, cashier_id, service_time, customer_list, shop):
        threading.Thread.__init__(self)
        self.cashier_id = cashier_id
        self.service_time = service_time
        self.worker = Worker(service_time, shop)
        self.worker.set_customer_list(customer_list)

    def run(self):
        print(f'Starting {self.cashier_id}')
        self.worker.customer_service(self.cashier_id)
        print(f'Exiting {self.cashier_id}')


class Worker:

    def __init__(self, service_time, shop):
        self.customer_list = []
        self.service_time = service_time
        self.shop = shop

    def get_service_time(self):
        return self.service_time

    def set_customer_list(self, customer_list):
        self.customer_list = customer_list
        return self.customer_list

    def get_customer_list(self):
        return self.customer_list

    def customer_service(self, cashier_id):
        customer_list = self.get_customer_list()
        for customer in customer_list:
            print(f'Cashier {cashier_id} handling customer: {customer.get_name()}\n\n')
            customer_receipt = Receipt(shop=self.shop, client=customer)
            customer_receipt.scan_items()
            time.sleep(self.get_service_time())
            customer_receipt.print_receipt()
            print(f'Customer {customer.get_name()} has been served by Cashier {cashier_id}\n')
        return

