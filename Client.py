# coding: utf-8
import json
class Client:
    n_c = 0
    list_clients = []
    with open('c_file.json', 'r') as cfile:
        list_clients = json.load(cfile)
    current_client = list_clients[0]


    def __init__(self,n,a):
        self.nom = n
        self.age = a
        if self.nom != "0":
            Client.list_clients.append({"nom": self.nom, "age": self.age})
            with open('c_file.json', 'w') as cfile:
                json.dump(Client.list_clients, cfile)
    def choice_client(self,c):
        Client.current_client = Client.list_clients[c-1]
        return Client.list_clients[c-1]
    def show_clients(self):
        Client.n_c = 0
        for c in Client.list_clients:
            Client.n_c += 1
            print "N° %d:" % Client.n_c, c

client = Client("0", 0)