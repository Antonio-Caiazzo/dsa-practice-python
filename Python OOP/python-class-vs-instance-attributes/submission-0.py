class BankAccount: 
    total_accounts = 0
    total_balance = 0
    
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance


# TODO: Create two accounts
first_account = BankAccount("Alice", 1000)
second_account = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format

print(f"{first_account.name}'s balance: ${first_account.balance}")
print(f"{second_account.name}'s balance: ${second_account.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")