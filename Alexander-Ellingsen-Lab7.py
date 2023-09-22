def main():
    menu = '''
    ***** MENU *****
    Brewed     $2.75
    Americano   3.25
    Cappuccino  3.50
    Latte       4.00
    Extra shot  0.75
    *****************
    '''
    drinks = { 'brewed':2.75, 'americano': 3.25, 'cappuccino':3.50, 'latte':4.00, 'extra shot':0.75 }
    print(menu)
    
    order = []
    total = 0.00
    coffee = input("What would you like to order? ")
    while coffee != "no":
        if coffee.lower() not in drinks:
            coffee = input("Please choose from the menu. Something else?")
        else:
            order.append(coffee.lower())
            total += drinks[coffee.lower()]
            coffee = input("Got it. What else? ('no' for nothing else):")
    dollars = format(total, '.2f')
    print("Great! Your order is:")
    for i in order:
        print("1 - ", order[order.index(i)])
    print("Your total is: $" + str(dollars))


main()
