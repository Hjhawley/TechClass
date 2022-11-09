def check_equality(x):
    if x == True:
        pass
    if x == False:
        pass

def check_identity(x):
    if x is True:
        pass
    if x is False:
        pass

'''
== is for value equality, or to check if two objects have the same value.
"is" is for reference equality, or to check if two references point to the
same object. Two objects are identical if they have the same memory address.

In most cases, you should be using ==, but it's advisable to use "is" for
singletons like None, True, and False.
'''