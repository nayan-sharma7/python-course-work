import re

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

phone3 = input()
pattern3 = r"\+91[6-9]\d{9}"
if re.fullmatch(pattern3,phone3):
    print("valid phone number")
else: 
    print("invalid phone number")