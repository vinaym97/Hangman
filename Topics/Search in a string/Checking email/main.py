# def check_email(string):
#     if (" " not in string) and ('@' in string):
#         # if '@' in string:
#         if '@.' not in string:
#             ind = string.find('@')
#             Print("True")
#             if "." in string[ind:]:
#                 return True
#         else:
#             return False
#         # else:
#         #         return False
#     else:
#         return False
# x = input()
# print(check_email(x))
# import re
# def check_email(address):
#   # Checks if the address match regular expression
#   is_valid = re.search('^\w.+@\w+.\w+$', address)
#   # If there is a matching group
#   if is_valid:
#     return True
#   else:
#     return False
import re

regex = r'\b[A-Za-z0-9._%+-]+email@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):
  if(re.match(regex, email)):
    print("True")

  else:
    print("False")

# Driver Code
x = input()
check(x)