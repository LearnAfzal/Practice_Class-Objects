from item_package.item_module import Item


item1=Item()
item2=Item()

item1.descr="Description1"
item2.descr="Description2"

print(item1.descr)
print(item2.descr)

"""item2=item1

print(item1.descr)
print(item2.descr)"""

item1.quantity=2
item1.price=100

print(item1.print_discount_price())

print(type(item1.finalprice))

#class ShoppingCart:
