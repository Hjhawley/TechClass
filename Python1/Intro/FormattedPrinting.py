print("This prints a string, filling in variable name for %s.")
name = "Jill"
print("hello %s." % (name))

print("\nThis does the same thing, but makes sure name is exactly 10 spaces wide.")
name = "Jill"
print("hello %10s." % (name))

print("\nThis prints two integers.")
i = 5
j = 15
print("%d" % (i))
print("%d" % (j))

print("\nThis prints two integers, making them take 2 spaces each.")
i = 5
j = 15
print("%2d" % (i))
print("%2d" % (j))

print("\nThis left pads with zeros.")
i = 5
j = 15
print("%02d" % (i))
print("%02d" % (j))

print("\nThis supresses the return until afterwards.")
i = 5
j = 15
print("%02d" % (i),end="")
print("%02d" % (j),end="")
print()

print("\nThis prints a float that will take 6 spaces, with 2 right of the decimal")
print("left padded with zeros.")
x = 13.12345
print("%06.2f" % (x))

print("\nThis prints a string left justified, instead of its default, right justified.")
print("It's in a field 9 wide, and suppresses the return.")
name = "jill"
x = name.ljust(9," ")

print (x,end="")