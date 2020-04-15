from flask import render_template

class Fooddonation(object):
    def accept(self,visitor):
        #Interface to accept a visitor
        print("Visitor is",visitor)
        return visitor.visit(self)

    def buy_food():
        print("Hitting the html now")
        return render_template("buyFood.html")
    def donate_food():
        return render_template("donateFood.html")
    def party_leftovers():
        return render_template("partyLeftovers.html")



class Visitor(object):
    pass

class BuyFood(Visitor):
    def visit(self):
        return Fooddonation.buy_food()

class Donate_Food(Visitor):
    def visit(self):
        return Fooddonation.donate_food(self)

class Party_leftovers(Visitor):
    def visit(self):
        return Fooddonation.party_leftovers(self)   





