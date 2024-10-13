class AccountState:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance


class BankAccount:
    def __init__(self, name, account_no, balance):
        self.__name = name
        self.__account_no = account_no
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def save(self):
        return AccountState(self.__balance)

    def restore(self, account_state: AccountState):
        self.__balance = account_state.balance

    def show_balance(self):
        return f"Balance: {self.__balance}"


class TransactionHistory:
    def __init__(self):
        self.__history = []

    def save_transaction(self, account_state: AccountState):
        self.__history.append(account_state)

    def rollback_transaction(self):
        return self.__history.pop()


def main() -> None:
    account = BankAccount(name="Himanshu Kumar", account_no=101, balance=5000)
    history = TransactionHistory()

    account.deposit(200)
    history.save_transaction(account.save())
    print(account.show_balance())

    account.withdraw(500)
    print(account.show_balance())

    account.restore(history.rollback_transaction())
    print(account.show_balance())


if __name__ == '__main__':
    main()
