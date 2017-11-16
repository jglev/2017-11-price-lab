#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Show that a list comprehension is just a 'for loop,' where you save the
output to a variable.
"""

# A 'for loop'
for x in range(0, 13):
    print(x)

# The same loop, as a 'list comprehension'
[x for x in range(0, 13)]

# To save the output of the loop, we would do this:
example_list_from_for_loop = []  # Create a blank list.
for x in range(0, 13):
    example_list_from_for_loop.append(x)  # Add x to the end of the list.

# Alternatively, we can save the output of the 'list comprehension' format
# directly:
example_list_from_list_comprehension_loop = [x for x in range(0, 13)]
