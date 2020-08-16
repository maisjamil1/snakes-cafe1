print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**')
print('** To quit at any time, type "quit" **')
print('*'*38)
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**')
print('** To quit at any time, type "quit" **')
print('*'*38)

menu="""
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
"""
print(menu)

print('*'*38)
print('What would you like to order?')
print('*'*38)
# while input()!='quit':
#   print(input())
foodli=['wings','cookies','spring Rolls','salmon','steak','meat tornado','a Literal garden','ice cream','cake','pie','coffee','tea','unicorn tears']
odersli=[]
while True:
    order=input()
    if order.lower()=='quit':
        break
    elif order.lower() in foodli:
        odersli.append(order.lower())
        # print(odersli)
        orderCount=odersli.count(order.lower())
        print(f"** {orderCount} order of {order} have been added to your meal **")
    else:
        print('sorry,this order is not exist')






