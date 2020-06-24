# Write your code here
import sys

class CoffeeMachine:
    # declare amounts of water, milk, coffee beans, cups and money
    water = 400
    milk = 540
    beans = 120
    cups = 9
    money = 550

    def __init__(self):
        while True:
            self.user_action(self.user_choice())

    def __str__(self):
        return "I am a Coffee Machine designed to make you coffee."

    def user_choice(self):
        """ ask user for input"""
        print("Write action (buy, fill, take, remaining, exit) :")
        menu_choice = input()
        print("")
        return menu_choice

    def user_action(self, action):
        if action == "buy":
            self.buy(self.coffee_choice())
            print("")
        elif action == "fill":
            self.fill()
            print("")
        elif action == "take":
            self.take()
            print("")
        elif action == "remaining":
            self.print_status()
            print("")
        elif action == "exit":
            sys.exit()

    def print_status(self):
        """Prints the status of the coffee machine"""
        print(f"""The coffee machine has:
        {self.water} of water
        {self.milk} of milk
        {self.beans} of coffee beans
        {self.cups} of disposable cups
        {self.money} of money""")

    def check_inventory(self, drink):
        """
        Function that checks the current inventory levels of the coffee machine and
        returns a True value if the machine can make the user selection or a False
        value if the machine doesn't have enough inventory.
        """
        espresso = [250, 16]
        latte = [350, 75, 20]
        capp = [200, 100, 12]
        if self.cups - 1 < 1:
            print("Sorry, not enough cups!")
            return False
        if drink == "1":
            if self.water - espresso[0] < 1:
                print("Sorry, not enough water!")
                return False
            elif self.beans - espresso[1] < 1:
                print("Sorry, not enough beans!")
                return False
            else:
                return True
        if drink == "2":
            if self.water - latte[0] < 1:
                print("Sorry, not enough water!")
                return False
            elif self.milk - latte[1] < 1:
                print("Sorry, not enough milk!")
                return False
            elif self.beans - latte[2] < 1:
                print("Sorry, not enough beans!")
                return False
            else:
                return True
        if drink == "3":
            if self.water - capp[0] < 1:
                print("Sorry, not enough water!")
                return False
            elif self.milk - capp[1] < 1:
                print("Sorry, not enough milk!")
                return False
            elif self.beans - capp[2] < 1:
                print("Sorry, not enough beans!")
                return False
            else:
                return True

    def coffee_choice(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        user_wants = input()
        return user_wants

    def buy(self, user_option):
        """
        Allows the user to choose an espresso, latte or cappuccino and
        makes the correct adjustments to water, milk, beans, cups and money
        then prints the updated status of the coffee machine
        """
        if user_option == "1":
            if self.check_inventory(user_option):
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
            else:
                return
        elif user_option == "2":
            if self.check_inventory(user_option):
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
            else:
                return
        elif user_option == "3":
            if self.check_inventory(user_option):
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
            else:
                return
        elif user_option == "back":
            return

    def fill(self):
        """
        Allows the user to update the amounts of water, milk, beans and cups and
        prints out the updated status of the coffee machine
        """
        print("Write how many ml of water do you want to add:")
        self.water = self.water + int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk = self.milk + int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.beans = self.beans + int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups = self.cups + int(input())

    def take(self):
        """
        Allows the user to withdraw all the money from the machine and prints
        out the updated status of the coffee machine.
        """
        print(f"I gave you ${self.money}")
        self.money = 0


coffee = CoffeeMachine()
coffee.__init__()
