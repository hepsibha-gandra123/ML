# GROUP 0-FULL match
# GROUP1-2-3-CAPTURED SUB MATCHES

import re
# 3
# d = input("enter date?")
# date = r'(\d{2})-(\d{2})-(\d{4})'
# if (re.fullmatch(date, d)):
#     print("it is in standard format")
# else:
#     print("not in standard format")

# 4
# d = input("enter number?")
# pattern = r'^\d{1,3}(,\d{3})*(\.\d{1,2})?$'
# if (re.fullmatch(pattern, d)):
#     print("it is in the format")
# else:
#     print("not in the format")

# 5
# p = input("enter name?")
# pattern = r'^[A-Z][a-z]+ ["Nakammoto"]+$'
# print(bool(re.fullmatch(pattern, p)))

# 6
# p = input("enter the sentence?")
# pattern = r'^["ALICE","BOB","CAROL","alice","bob","carol"]' \'+ ["EATS","PETS","THROWS","eats","pets","throws"]' \
#     '+ ["APPLES","CATS","BASEBALLS","apples","cats","baseballs"]+$'
# print(bool(re.fullmatch(pattern, p)))

# 7


# def password(p):
#     pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
#     print(bool(re.fullmatch(pattern, p)))


# p = input("enter password?")
# password(p)


# password
# import re
# pattern = r'^\[a-zA-Z0-9]{8,}$'
# p = input("enter password?")
# if (re.fullmatch(pattern, p)):
#     print("VALID")
# else:
#     print("INVALID")

# import re
# pattern = r'^\["alice","bob","carol"]'
# \'+["eats","pets","throws"]'
# \'+["apples","cats","baseballs"]$'
# p=input("enter string?")
# if(re.match(pattern,p)):
#     print("VALID!")
# else:
#     print("INVALID!")
