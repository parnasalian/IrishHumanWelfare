class Fooddonation(object):
    def accept(self,visitor):
        #Interface to accept a visitor
        print("Visitor is",visitor)
        visitor.visit(self)

    def buy_food():
        print("Hitting the html now")
        return render_template("buyFood.html")
    def donate_food():
        return render_template("donateFood.html")
    def party_leftovers():
        return render_template("partyLeftovers.html")

class Visitor(object):
    def visit(self,fooddon):
        pass

class BuyFood(Visitor):
    def visit(self,fooddon):
        print("From Food donation got ",fooddon)
        fooddon.buy_food(self)

class Donate_Food(Visitor):
    def visit(self,fooddon):
        fooddon.donate_food(self)

class Party_leftovers(Visitor):
    def visit(self,fooddon):
        fooddon.party_leftovers(self)   





