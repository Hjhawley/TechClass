# Operator Overloading

# Operator overloading lets you define how operators behave with user-defined objects.
# For example, the add (+) operator performs addition with integers and concatenation with strings.
# With operator overloading, you can define how the addition operator should behave with instances
# of your custom classes.

# Operator overloading is useful because:
# - It allows your custom objects to interact with Python's built-in operators.
# - It makes your classes more intuitive and easier to use.
# - It can help in making your code cleaner and more readable.

# Python lets you overload operators by defining special methods in your class.
# These methods have double underscores (__) at the beginning and end of their names.
# These are called "dunder" methods.

# Common operators and their dunder methods:
# - Addition: __add__(self, other)
# - Subtraction: __sub__(self, other)
# - Multiplication: __mul__(self, other)
# - Division: __truediv__(self, other)
# - String Representation: __str__(self)

# Example: Overloading the + Operator
# We'll create a BankAccount class and overload the + operator to merge two bank accounts.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    # Overload the + operator
    def __add__(self, other):
        # Make sure the other object is a BankAccount instance
        if isinstance(other, BankAccount):
            # Merge the balances of the two accounts
            return BankAccount(self.balance + other.balance)
        else:
            raise ValueError("Can only add BankAccount to another BankAccount")

    # Overload the str operator to print the account balance in a nice format
    def __str__(self):
        return f"BankAccount(balance: ${self.balance:.2f})"

# Create two bank accounts
account1 = BankAccount(1000.50)
account2 = BankAccount(2500.75)

# Merge the two accounts using the overloaded + operator
merged_account = account1 + account2

# Print the result
print(merged_account)  # Output: BankAccount(balance: $3501.25)

# Now, let's overload the * operator to multiply the balance of the account by a number.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return BankAccount(self.balance + other.balance)
        else:
            raise ValueError("Can only add BankAccount to another BankAccount")

    def __mul__(self, multiplier):
        if isinstance(multiplier, (int, float)):
            return BankAccount(self.balance * multiplier)
        else:
            raise ValueError("Can only multiply BankAccount by an int or float")

    def __str__(self):
        return f"BankAccount(balance: ${self.balance:.2f})"

# Create a bank account
account = BankAccount(1010.25)

# Multiply the account balance by 3 using the overloaded * operator
multiplied_account = account * 3

# Print the result
print(multiplied_account)  # Output: BankAccount(balance: $3030.75)

# Operator overloading helps to make custom classes work intuitively with built-in operators.
# Practice using operator overloading with your own classes!
