from OrderManager import OrderManager
from HAPIExecutionServer import HAPIExecutionServer

class HydraOrderManager(OrderManager):

    def __init__(self, autostart = True):
        super(HydraOrderManager, self).__init__()
        self.es_server = 0
        if autostart:
            self.open_socket()

    def open_socket(self):
        self.es_server = HAPIExecutionServer()

    def close_socket(self):
        self.es_server.close_es_socket()

    def send_order(self, order):
        self.es_server.submit_order(order)

    def cancel_order(self, order):
        self.es_server.cancel_order(order)

    def cancel_all_orders(self):
        self.es_server.cancel_all_orders()