# name = "Mike"
# age = "28"
# pronouns = "she/her"

# print("This is {}, using {} pronouns, and is {} years old.".format(
#   name, pronouns, age))

# name = "Katie"
# age = "22"
# pronouns = "hh/him"

# print(
#   "This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far"
#   .format(name=name, pronouns=pronouns, age=age))

# name = "Katie"
# age = "28"
# pronouns = "she/her"

# response = "This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far".format(
#   name=name, pronouns=pronouns, age=age)

# print(response)

# name = "Katie"
# age = "28"
# pronouns = "she/her"

# response = f"This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far"

# print(response)

# name = "Katie"
# age = "28"
# pronouns = "she/her"

# response = f"""This is {name}, using {pronouns} pronouns, and is {age} years old. Hello, {name}. How are you? Have you been having a great {age} years so far"""

# print(response)

# for i in range(1, 31):
#   print(f"Day {i} of 100 completed")

# for i in range(1, 31):
#   print(f"Day {i: <1} of 100 completed")

# for i in range(1, 31):
#   print(f"Day {i} of 100")

# food = "pizza"
# location = "beach"
# color = "green"
# friend = "Quinn"

# response = "Alejandra ordered {food} to eat at the {location} with her friend, {friend}. She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame." .format(food=food, location=location, color=color, friend=friend)

# print(response)

print("          30 Days Down - What did you think?")
print()
print()
for i in range(1, 31):
  thought = input(f"Day {i}:\n")
  print()
  myText = f"You thought Day {i} was"
  print(f"{myText:^35}")
  print(f"{thought:^35}")
  print()