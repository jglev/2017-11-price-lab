"""Demonstrate different types of variables."""

# An "integer" (a whole number)
test1 = 123
round(test1)

# Text
test2 = "123"
round(test2)  # This won't work -- you can't round text!

# A "floating-point" number (that is, a number with a decimal)
test3 = 123.2
round(test3)
type(round(test3))

# Lists
test4 = range(1, 13)
test4[0]  # Get the first ("0th") item from the list.
type(test4)

# Dictionaries
test5 = {"a": 12345, "b": "Shakespeare"}
test5['a']
type(test5)
