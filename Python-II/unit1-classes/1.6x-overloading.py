# Now it's your turn to practice operator overloading.
# Add support for the subtract (-) operator to the BankAccount class
# to transfer money from one account to another.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return BankAccount(self.balance + other.balance)
    
    # Define a method here that overloads the - operator
    
    def __str__(self):
        return f"BankAccount(balance: ${self.balance:.2f})"

# After you define the __sub__ method, the following code should work.

# Create bank accounts
account1 = BankAccount(1000.50)
account2 = BankAccount(2500.75)

# Transfer money between accounts using the overloaded - operator
account1_after_withdrawal = account1 - 300.00
print(account1_after_withdrawal)  # Output: BankAccount(balance: $700.50)

# If you see 'TypeError: unsupported operand type(s) for -: 'BankAccount' and 'float''
# that means you have a mistake in your implementation. Keep at it!
