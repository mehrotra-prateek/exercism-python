from threading import Lock


class BankAccount:
    def __init__(self):
        self.lock = Lock()
        self.accountState = ""
        self.amount = 0

    def get_balance(self):
        with self.lock:
            self.account_state()
            return self.amount

    def open(self):
        if self.accountState:
            raise ValueError("Account is already open")
        self.accountState = True

    def deposit(self, amount):
        with self.lock:
            self.check_amount(amount)
            self.account_state()
            self.amount += amount

    def withdraw(self, amount):
        with self.lock:
            self.check_amount(amount)
            self.account_state()
            if amount <= self.amount:
                self.amount -= amount
            else:
                raise ValueError("not enough money in account")

    def close(self):
        self.account_state()
        self.accountState = False
        self.amount = 0

    def account_state(self):
        if not self.accountState:
            raise ValueError("Account is closed")

    def check_amount(self, amount):
        if amount < 0:
            raise ValueError("amount cannot be negative")
