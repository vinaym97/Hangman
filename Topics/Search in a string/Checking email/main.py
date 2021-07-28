#
# import re
#
# regex = r'\b[A-Za-z0-9._%+-]+email@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#
# def check_email(email):
#   if(re.match(regex, email)):
#     # print("True")
#     # return True
#   # else:
#     print("False")
#     return False
# Driver Code
# x = input()
# check(x)
def check_email(email):
  index = email.find("@")

  if " " in email:
    return False
  elif "@" not in email:
    return False
  elif "." not in email:
    return False
  elif "@." in email:
    return False
  elif "." not in email[index:]:
    return False
  else:
    return True