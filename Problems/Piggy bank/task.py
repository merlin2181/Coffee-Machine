class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        if self.cents >= 100:
            new_dollars = self.cents // 100
            self.dollars += new_dollars
            self.cents -= (new_dollars * 100)