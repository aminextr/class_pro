# coding: utf-8
import json
class Product:
    choiced_products = []
    n_p = 0
    products_stock = []
    with open('p_file.json', 'r') as pfile:
        products_stock = json.load(pfile)

    def __init__(self,n,q,p,i_q):
        self.nom = n
        self.qty = q
        self.price = p
        self.choiced_q = i_q
        self.qty -= self.choiced_q
        if self.nom != 0:
            Product.choiced_products.append({"nom": self.nom, "qty choisi": self.choiced_q, "prix unitaire": self.price})
            Product.products_stock.append({"nom": self.nom, "qty": self.qty, "prix unitaire": self.price})
            with open('p_file.json', 'w') as pfile:
                json.dump(Product.products_stock, pfile)
    def choice_product(self,p_n,p_q):
        Product.choiced_products.append({"nom": Product.products_stock[p_n -1]["nom"], "qty choisi": p_q, "prix unitaire": Product.products_stock[p_n -1]["prix unitaire"]})
        Product.products_stock[p_n -1]["qty"] -= p_q
        with open('p_file.json', 'w') as pfile:
            json.dump(Product.products_stock, pfile)
    def show_products_stock(self):
        Product.n_p = 0
        for p in Product.products_stock:
            Product.n_p += 1
            print "N° %d:" % Product.n_p, p
product = Product(0, 0, 0, 0)
