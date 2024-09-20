# For DEBUG
debugging = False

def readMenu(fn='CoffeeMenu01.txt'): 
    with open(fn) as fd:
        return fd.read()

class CupOfCoffee:
    pass
class CustomerBill:
    pass

class CupOfCoffee():
    def __init__(self, coffee_type, drinking_type, price):
        self.coffee_type = coffee_type
        self.drinking_type = drinking_type
        self.price = price
        self.add_on = []

    def set_add_on(self, one_add_on, one_add_on_price):
        if one_add_on not in self.add_on:
            self.add_on.append(one_add_on)
            self.price += one_add_on_price

    def get_add_on_list(self):
        return self.add_on
        
    def __repr__(self) -> str:
        if len(self.add_on) == 0:
            return f' This cup is {self.drinking_type.lower()} {self.coffee_type} with no add on, {self.price} baht.'
        elif len(self.add_on) == 1:
            return f' This cup is {self.drinking_type.lower()} {self.coffee_type} with {self.add_on[0]}, {self.price} baht.'
        elif len(self.add_on) > 1:
            return f' This cup is {self.drinking_type.lower()} {self.coffee_type} with {", ".join(self.add_on[:-1])} and {self.add_on[-1]}, {self.price} baht.'
        
class CustomerBill():
    def __init__(self, name) -> None:
        self.customer_name = name
        self.add_ordered_coffee_list = []

    def add_ordered_coffee(self, aCupOfCoffeeObject):
        self.add_ordered_coffee_list.append(aCupOfCoffeeObject)

    def get_ordered_coffee(self):
        return self.add_ordered_coffee_list

    # Remain this one 
    def receipt(self):
        name = f"Kun {self.customer_name}'s Receipt"

        sentence = '++++++++++++++++++++++++++++++++\n'
        sentence += '      CPE38 **StarBUG Cafe    \n'
        sentence += f"{name:^32}\n"
        sentence += '++++++++++++++++++++++++++++++++\n'
        sentence += 'Description                Price'

        total = 0

        for order in self.add_ordered_coffee_list:
            total += order.price

        for order in self.add_ordered_coffee_list:
            pass

        return sentence

def runStarBUGcafe_main(DEBUG = False):
    coffee_men = []
    coffee_menu = []

    add_on_men = []
    add_on_menu = []

    for cof in coffee_menu_CSV.splitlines():
        if cof != '':
            coffee_men.append(cof)

    coffee_menu = [item.replace(' ','') for item in coffee_men]

    print(f'coffee menu = {coffee_menu}')

    for add in add_on_menu_CSV.splitlines():
        if add != '':
            add_on_men.append(add)

    add_on_menu = [item.replace(' ','') for item in add_on_men]

    # DEBUG
    if DEBUG:
        print(f'Coffee menu = {coffee_men}')
        print()
        print(f'Clean menu = {coffee_menu}')
        print()
        print(f'Add on menu = {add_on_menu}')
        print()
    
    print('Welcome to CPE38 **StarBUG Cafe!')
    print('+++++++++++++ MENU +++++++++++++')
    print('Coffee         Hot  Cold  Frappe')

    for i in range(1, len(coffee_menu) + 1):
        temp = coffee_menu[i - 1].split(',')

        print(f'{i}.{temp[0]:<12} {temp[1]:>3} {temp[2]:>5} {temp[3]:>5}')

    print('++++++++++++ ADD-ON ++++++++++++')

    for b in range(1, len(add_on_menu) + 1):
        temp = add_on_menu[b - 1].split(',')

        print(f'{b}.{temp[0]:<19} {temp[1]:>2}')

    print('++++++++++++++++++++++++++++++++')
    print()

    customer_name = input("Enter customer's name: ")
    amount_of_cup = int(input('How many cups of coffee to order? '))

    # Create Object
    customer = CustomerBill(customer_name)

    # Cup amount 
    for i in range(1, amount_of_cup + 1):
        # Coffee Type
        while True:
            coffee_type_num = int(input(f'Cup #{i}, please select type of coffee: '))
            if 1 <= coffee_type_num <= len(coffee_menu):
                break
            else:
                print(' ERROR: Invalid input!')

        count_true = 0
        type_index = 0
        real_type = None

        if coffee_menu[coffee_type_num - 1].split(',')[1] != '0':
            h = 'H'
            count_true += 1
            real_type = 'hot'
        else:
            h = ''
        if coffee_menu[coffee_type_num - 1].split(',')[2] != '0':
            c = ', C'
            count_true += 1
            real_type = 'cold'
        else:
            c = ''
        if coffee_menu[coffee_type_num - 1].split(',')[3] != '0':
            f = ', F'
            count_true += 1
            real_type = 'frappe'
        else:
            f = ''

        if DEBUG:
            print(f'count_true = {count_true}')
            print()
            print(f'Real type = {real_type}')
            print()

        coffee_type = coffee_menu[coffee_type_num - 1].split(',')[0]

        # Drinking Type
        while True:
            if count_true == 1:
                drinking_type = real_type
                if real_type == 'hot':
                    type_index = 1
                elif real_type == 'cold':
                    type_index = 2
                elif real_type == 'frappe':
                    type_index = 3

                break
            drinking_type_num = input(f'Cup #{i}, please select drinking type ({h}{c}{f}): ')
            if drinking_type_num.lower() in f'{h}{c}{f}'.lower():
                if drinking_type_num == 'H' or drinking_type_num == 'h':
                    drinking_type = 'hot'
                    type_index = 1
                elif drinking_type_num == 'C' or drinking_type_num == 'c':
                    drinking_type = 'cold'
                    type_index = 2
                elif drinking_type_num == 'F' or drinking_type_num == 'f':
                    drinking_type = 'frappe'
                    type_index = 3
                break
            else:
                print(' ERROR: Invalid input!')

        coffee_price = coffee_menu[coffee_type_num - 1].split(',')[type_index]
        coffee_price = int(coffee_price)

        if DEBUG:
            print()
            print(f'Coffee type = {coffee_type}')
            print()
            print(f'Drinking tyoe = {drinking_type}')
            print()
            print(f'Coffee price = {coffee_price}')
            print()
            print(f'Add on menu = {add_on_menu}')

        # Create Object
        coffee = CupOfCoffee(coffee_type, drinking_type, coffee_price)

        customer.add_ordered_coffee(coffee)
        
        k = []

        # Add on
        while True:
            add_on_num = input(f'Cup #{i}, please select add on (enter for exit): ')
            if add_on_num == '':
                break

            add_on_num = int(add_on_num)
            if 1 <= add_on_num <= len(add_on_menu) and not add_on_num in k :
                coffee.set_add_on(add_on_menu[add_on_num - 1].split(',')[0], int(add_on_menu[add_on_num - 1].split(',')[1]))
                k.append(add_on_num)
            else:
                print(' ERROR: Invalid input!')
            
            if len(k) == len(add_on_menu):
                break

        print(coffee.__repr__())

    print(customer.receipt())

    if DEBUG:
        print(f'add_on list = {coffee.get_add_on_list()}')
        print()
        print(f'order list = {customer.get_ordered_coffee()}')
        print()
        print(f'Price = {coffee.price}')
        print()
        
coffee_menu_filename = input('Enter Coffee Menu available today (filename): ')
coffee_menu_CSV = readMenu(coffee_menu_filename)
addon_menu_filename = input('Enter AddOn Menu available today (filename): ')
add_on_menu_CSV = readMenu(addon_menu_filename)

runStarBUGcafe_main(debugging)
