# Operator Overloading

# Operator overloading allows you to define how operators (see Python I - Lesson 1.4)
# behave with user-defined objects. For instance, when you use the + operator with integers 
# or strings, it performs addition and concatenation, respectively. With operator overloading,
# you can define how the add (+) operator should behave with instances of your custom class.

# Python allows you to overload operators by defining special methods in your class. 
# These methods have double underscores (__) at the beginning and end of their names,
# also known as "dunder" methods.

# Here are some common operators and their dunder methods:
# - Addition: __add__(self, other)
# - Subtraction: __sub__(self, other)
# - Multiplication: __mul__(self, other)
# - Division: __truediv__(self, other)
# - String Representation: __str__(self)

# Example: Overloading the + Operator
# Let's start with an example where we create a BankAccount class. 
# We'll overload the + operator to merge two bank accounts together.

# Define a BankAccount class to represent a bank account
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    # Overload the + operator
    def __add__(self, other):
        # Merge the balances of the two accounts
        return BankAccount(self.balance + other.balance)

    # Overload the str operator to print the account balance nicely
    def __str__(self):
        return f"BankAccount(balance: ${self.balance:.2f})"

# Create two bank accounts
account1 = BankAccount(1000.50)
account2 = BankAccount(2500.75)

# Merge the two accounts using the overloaded + operator
merged_account = account1 + account2

# Print the result
print(merged_account)  # Output: BankAccount(balance: $3501.25)

# Operator overloading helps to make custom classes work intuitively with built-in operators. 
# Practice using operator overloading with your own classes to make them more flexible and intuitive to use!
