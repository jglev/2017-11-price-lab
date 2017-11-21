"""Demonstrate different types of variables."""

test_1 = 23

round(23)
round(test_1)

type(test_1)

test_2 = 23.5
type(23.5)

type(round(test_2))

int(test_2)
float(test_1)

print('this is a string of characters.')
test_4 = "this is a string of characters."
print(test_4)

round(test_4)

int(test_4)

type(int('123'))

help(round)


dir(test_4)

123.capitalize()


test_4.capitalize()

test_4.upper()


len(dir(123))

del(test_5)

test_6 = [1, 3, 4, 6, 8, 9, '.:!']

type(test_6)

type(test_6[-1])

test_4[0:6]


len('this is  atest')

print(max(1, 2, 3))
test_7 = max('a', 'A', '0')

round(12.3354, ndigits=-3)

commandname(option1, option2)


variable_to_look_at = 7.3

int(variable_to_look_at)

if type(variable_to_look_at) is float:
    variable_to_look_at = int(variable_to_look_at)
    
variable_to_look_at = 'test!'

variable_to_look_at <= 123567

if(
   type(variable_to_look_at) is str and variable_to_look_at == "Hello!"):

    print("It's a string and it's 'Hello!'")

elif type(variable_to_look_at) is int:

    print("it's an integer!")

else:

    print("Nope, it's not a string or it's not 'Hello'")

my_variable = 4

if my_variable < 1:

    print("Less than 1")

elif my_variable < 5:

    print("Less than 5")
    
elif my_variable == 3:
    print("It's three")
else:
    print("It's not three")

elif my_variable < 7:
    print("Less than 7")

else:
    print("Something else")


test_8 = ["a", "b", "c", "d"]


test_9 = 3

for pizza in test_8:
    print(f'Processing "{pizza}"...')
    if thing
    print(pizza.capitalize())


for number_of_thing in range(0, len(test_8)):

    beepboop = test_8[number_of_thing]

    print(f'Processing "{beepboop}"...')
    print(f'Beepboop plus 5 is {beepboop + 5}')

    beepboop_plus_seven = beepboop + 7
    print(f'beepboop plus seven is {beepboop_plus_seven}')
    if number_of_thing in [1, 2]:
        print(beepboop.capitalize())
    else:
        print(beepboop)



for value in range(0, len(test_8)):
    print(value)







pizza


thing = test_8[0]
print(thing.capitalize())

thing = test_8[1]
print(thing.capitalize())

thing = test_8[2]
print(thing.capitalize())

thing = test_8[3]
print(thing.capitalize())


batman = 'a'
batman = 'b'
batman = 'c'

batman




test_1
test_2
test_3 = 'abc'

new_list = [test_1, test_2, test_3]


for thing in new_list:
    if type(thing) is str:
        print(thing.upper())
    elif type(thing) is not str:
        print(thing + 5)
    else:
        print(": (")


print('this is a string', 5)

f-strings

f'The value of test_3 is "{test_3}"'




["a",
 "b",
 3]



my_list = ["a", "b", "c"]

', '.join(my_list)





test_6
test_7 = test_6.copy()

test_7
test_6 = 'a'

del(test_6)






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
