class Item:

    def __init__(self):
        self.id=None
        self.descr=None
        self.quantity=None
        self.price=None

    def print_discount_price(self):
        if self.quantity==2:
            self.finalprice=(self.price-self.price*10/100)*self.quantity
            return self.finalprice
        elif self.quantity>=3 and self.quantity<=5:
            self.finalprice=(self.price-self.price*15/100)*self.quantity
            return self.finalprice
        elif self.quantity>5:
            self.finalprice=(self.price-self.price*25/100)*self.quantity
            return self.finalprice
        else:
            return "sry, you are not eligible for discount"



