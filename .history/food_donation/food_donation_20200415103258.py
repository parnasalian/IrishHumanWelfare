class Fooddonation(object):
    def accept(self,visitor):
        #Interface to accept a visitor
        visitor.visit(self)

    def buy_food():
        return render_template("buyFood.html")
    def donate_food():
        return render_template("donateFood.html")
    def party_leftovers():
        return render_template("partyLeftovers.html")

class Visitor(object):
    def visit(self,fooddon):

class BuyFood(Visitor):
    def visit(self,fooddon):
        fooddon.buy_food(self)

class Donate_Food(Visitor):
    def visit(self,fooddon):
        fooddon.donate_food(self)

class Party_leftovers(Visitor):
    def visit(self,fooddon):
        fooddon.party_leftovers(self)   

