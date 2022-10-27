# Password validator

import re

password = input("Enter your password --> ")

expression = r'([A-Z]+\B)([a-z]+\B)([0-9]+)(\W+)'

flag = re.search(expression, password)

if flag is not None:
  print(flag)
else:
  print(
    "Your password should be 8 characters long, with Uppercase , strats with upper case, lowercase, digit and special characters"
  )
