from flask import render_template
from clothes_donation.clothes_donation import *

class Fooddonation(object):
    def accept(self,visitor):
        #Interface to accept a visitor
        return visitor.visit(self)

    def gets_buy_food():
        return render_template("buyFood.html")
    def gets_donate_food():
        dropdown_dictionary = {}
        facade = Facade()
        dropdown_dictionary = facade.getDropdownDetails()
        print("Inside factory",dropdown_dictionary)
        return render_template("donateFood.html")
    def gets_party_leftovers():
        return render_template("partyLeftovers.html")



class Visitor(object):
    pass

class BuyFood(Visitor):
    def visit(self):
        return Fooddonation.gets_buy_food()

class Donate_Food(Visitor):
    def visit(self):
        return Fooddonation.gets_donate_food()

class Party_leftovers(Visitor):
    def visit(self):
        return Fooddonation.gets_party_leftovers()   





