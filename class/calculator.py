

class Computer:

    def __init__(self, money_given, price):
        self.money_given = money_given
        self.price = price

        self.coins = (0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0)
        self.bank_notes = (5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0)

    def get_return_money(self):
        return_money = self.money_given - self.price
        change_money_dict = {}
        for notes_coins in sorted(self.bank_notes + self.coins, reverse=True):
            change_money_dict[notes_coins], return_money = divmod(return_money, notes_coins)
            print(change_money_dict)
            return_money = round(return_money, 2)
            print(return_money)

        new_dict = {k: int(v) for k, v in change_money_dict.items() if v != 0.0}
        return new_dict




