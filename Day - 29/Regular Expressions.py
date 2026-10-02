# import re

#match()
# text = "python code"
# re.match("python",text)

#search()
# text2 = "Yadagiri nayan harshith ruthvik"
# re.serach("nayan",text2)

# #sub()
# s3 = "I love python"
# re.sub('I','you',s3)

# #fullmatch()
# s2 = "python"
# re.fullmatch("python","python")

# #findall()
# text5 = "cat dog cat fish cat"
# result = re.findall("cat", text5)


"""         Meta Characters          """


"""         Email Validation         """
# user1_email = input()
# pattern = r"\w+@\w+\.\w+$"
# if re.fullmatch(pattern,user1_email):
#     print("valid")
# else: 
#     print("invalid")


# phone2 = input()
# pattern2 = r"\d{10}"
# if re.fullmatch(pattern2,phone2):
#     print("valid phone number")
# else: 
#     print("invalid phone number")

# phone3 = input()
# pattern3 = r"\+91[6-9]\d{9}"
# if re.fullmatch(pattern3,phone3):
#     print("valid phone number")
# else: 
#     print("invalid phone number")


#credit card validation :- 

# import re
# num=input()
# c=r'\d{4}\s\d{4}\s\d{4}\s\d{4}'
# if re.fullmatch(c,num ):
#     print('Valid')
# else:
#     print('Invalid')


#Date validation :- 

#import re
# date=input()
# d=r'\d{2}-\d{2}-\d{4}'
# if re.fullmatch(d,date):
#     print('Valid')
# else:
#    print('Invalid')

# #employee validation :- 

# import re
# emp = input()
# q = r"CGTD\d{3}"
# if re.fullmatch(q,emp):
#     print("Valid Employee ID")
# else:
#     print("Invalid Employee ID")

# Password Validation

# import re
# num=input()
# p=r"[A-Z]{1}[a-z]+[0-9]+"
# if re.fullmatch(p,num):
#     print('Valid')
# else:
#     print('Invalid')

# #URL Validation :-

# import re
# URL = input()
# z = r"https?://\w+\.\w+\.\w+"
# if re.fullmatch(z,URL):
#     print (URL)
# else:
#     print("Invalid URL")

import re 
prices = input()
p = r"\$,\d{1,5}"
if re.fullmatch(p, prices):
    print("Valid price format")
else:
    print("Invalid price format")