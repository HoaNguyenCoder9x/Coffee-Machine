from menu import MENU, resources


class CoffeeMachine:
    def __init__(self):
        self.resource = resources
        self.profit = 0
        self.menu = MENU

    def run_report(self):
        """ SHOW THE CURRENT REPORT OF PROFIT AND MATERIAL"""
        print(f"Water: {self.resource['water']}")
        print(f"Milk: {self.resource['milk']}")
        print(f"Coffee: {self.resource['coffee']}")
        print(f"Profit: {self.profit}")

    def menu_list(self):
        """show menu list"""
        menulist = []
        for item in MENU:
            menulist.append(item)
            menu = ', '.join(menulist)
        return menu

    def select_drink(self):
        drink_name = input(f'select drink {self.menu_list()}: ')
        return drink_name

    def check_ingredients(self, drink):
        """ CHECK THE ABILITY TO MAKE A COFFEE"""
        drink_ingredient = self.menu[drink]['ingredients']
        for ingredient in self.resource:
            if drink_ingredient[ingredient] > self.resource[ingredient]:
                print(f'Lack of {ingredient}')
                return False
        return True

    def process_coin(self):
        coin_input = int(input("Give money,pls: "))
        return coin_input

    def check_coin(self, coin_input):
        drink_cost = self.menu[drink_name]['cost']
        """ Get and check if it's enough money """
        if coin_input >= drink_cost:
            inchange = coin_input - drink_cost
            print(f"You have {inchange}VNĐ in change")
            self.profit += drink_cost
            return True
        return False

    def make_coffee(self, drink):
        drink_ingredient = self.menu[drink]['ingredients']
        for ingredient in self.resource:
            self.resource[ingredient] -= drink_ingredient[ingredient]
        print(f'Here is your {drink}')


cfmachine = CoffeeMachine()
is_machine_on = True
while is_machine_on:
    drink_name = cfmachine.select_drink()
    if drink_name == 'report':
        cfmachine.run_report()
    elif drink_name == 'off':
        is_machine_on = False
    else:
        if cfmachine.check_ingredients(drink_name):
            coin_input = cfmachine.process_coin()
            if cfmachine.check_coin(coin_input):
                cfmachine.make_coffee(drink_name)

