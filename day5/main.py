"""
>, <, >=, <=, ==, != => True/False
"""

"""
if - elif - else
"""
name = input("Please enter your name: ") # '' -> bool('') = False

if name:  # Checks the truth value of name by calling bool
      print(f"You entered {name}")
else:
      print("You didn't type anything")