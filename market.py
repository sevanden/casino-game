# coding=utf-8

import collections
import csv

from assets import House


class Market():
    def __init__(self, level, xp):
        self.available_products = []
        self._load_products()
        self.update_product_list(level, xp)

    def _load_products(self):
        a_product = collections.namedtuple('a_product', 'asset unlock_xp unlock_level')
        self._product_list = []
        a_file = open('data/market.csv', 'r')
        for line in csv.DictReader(a_file, delimiter=','):
            if line['type'] == 'house':
                asset = House(line['name'], line['description'], line['value'], line['image'], line['rentable'], line['rent'])
            self._product_list.append(a_product(asset=asset, unlock_xp=line['unlocked_at_xp'], unlock_level=line['unlocked_at_level']))
        a_file.close()

    def update_product_list(self, level, xp):
        for product in self._product_list:
            if int(product.unlock_level) == level:      # Does our current level allow us to access this product?
                if int(product.unlock_xp) == xp:        # Does our player have the required experience to access this product?
                    self.available_products.append(product)

    def get_product_list(self):
        return self.available_products

    def get_product_details(self, product_id):
        # elif product_to_purchase >= available_products.count():
        #    self._status_message = 'The selected product ID does not exist.'
        return self.available_products[product_id].asset

    def buy_product(self, product_id):
        # elif product_to_purchase >= available_products.count():
        #    self._status_message = 'The selected product ID does not exist.'
        bought_product = self.available_products[product_id].asset
        self.available_products.pop(product_id)
        return bought_product