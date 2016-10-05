# coding: utf-8
from __future__ import unicode_literals
import time
import os
import json
from Client import Client
from Product import Product
from Invoice import Invoice
client = Client("0", 19)
product_instance = Product(0,30,20000,0)
invoice = Invoice()
print "-----------------------------------".encode('utf-8')
no = int(raw_input("N° Facture : ".encode('utf-8')))
Invoice.inv_no = no
print "-----------------------------------"
print "Choix du client :\n> 1: Selection\n> 2: Nouveau"
new_old = int(raw_input("Votre choix ? 1 / 2 :"))
if new_old == 1:
    print "----------------- Clients -----------------"
    client.show_clients()
    print "-----------------------------------"
    y_choice = int(raw_input('N° du client souhaité :'.encode('utf-8')))
    client.current_client = client.choice_client(y_choice)
elif new_old == 2:
    print '----------------- Nouveau Client ------------------'
    new_client = raw_input("Nom du nouveau client :")
    new_client_age = raw_input("l'age :")
    client_instance = Client(new_client, new_client_age)
    print "> Nouveau client ajouté <"
print '\n-----------------------------------'
autre_prod = True
while autre_prod == True:
    print "Saisie des produits\n> 1: Nouveau produit ?\n> 2: Choisir un produit existant"
    product_new_old = int(raw_input("Votre choix ? 1 / 2 :"))

    if product_new_old == 1:
        prod_name = raw_input("> Nom Produit :")
        stock_q = int(raw_input("> Quantité Stock :".encode('utf-8')))
        price = int(raw_input("> Prix Unitaire :"))
        invoice_q = int(raw_input("> Quantité Facture :".encode('utf-8')))
        product_instance = Product(prod_name, stock_q, price, invoice_q)
        s_autre_prod = raw_input("Saisir un autre produit ? oui/non :")
        if s_autre_prod == "oui" or s_autre_prod == "o":
            autre_prod = True
        else:
            autre_prod = False
    elif product_new_old == 2:
        print "---------- Stock ----------"
        product_instance.show_products_stock()
        no_prod = int(raw_input("N° du produit :".encode('utf-8')))
        qte_prod = int(raw_input("Quantité :".encode('utf-8')))
        product_instance.choice_product(no_prod, qte_prod)
        s_autre_prod = raw_input("Saisir un autre produit ? oui/non :")
        if s_autre_prod == "oui" or s_autre_prod == "o":
            autre_prod = True
        else:
            autre_prod = False
invoice.total_HT()
tva = int(raw_input("> La Taxe (%) :".encode('utf-8')))


