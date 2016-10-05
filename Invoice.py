# coding: utf-8
import time
import json
from Client import Client
from Product import Product
class Invoice:
    inv_no = 0
    client_name = Client.current_client["nom"]
    client_age = Client.current_client["age"]
    Date = time.strftime("%d/%m/%Y %H:%M")
    total_h = 0
    Taxe = 0
    total_ttc = 0
    n = 0

    def total_HT(self):
        for p in Product.choiced_products:
            Invoice.total_h += p["prix unitaire"]
            Invoice.n += 1
