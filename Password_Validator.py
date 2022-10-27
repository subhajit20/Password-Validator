# Password validator
import re


def Custom_Password_Validator(password):
  try:
    expression = r'([A-Z]+\B)([a-z]+\B)([0-9]+)(\W+)'

    flag = re.search(expression, password)

    if flag is not None:
      return flag.group()
    else:
      return False

  except Exception as e:
    print(e)


password = input("Enter your password --> ")

data = Custom_Password_Validator(password)
if data != False:
  print(data)
else:
  print(
    "Your password should be 8 characters long, Starts with uppercase, then lowercase , then digits and then special characters except _"
  )
