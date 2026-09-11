# import random
# characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# characters += "abcdefghijklmnopqrstuvwxyz"
# characters += "0123456789"
# characters += "@#*!&$"
# length = int(input())
# password = ""
# for i in range(length):
#     ch = random.choice(characters)
#     password += ch
# print(password)

import random
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#*!&$"
password = []
length = int(input())
if length < 4:
    print("your password length is (length) which is small , choose higher length password")
else: 
    password.append(random.choice(upper))
    password.append(random.choice(lower))
    password.append(random.choice(num))
    password.append(random.choice(special))
for i in range(length - 4):
    all_char= upper + lower + num + special
    ch = random.choice(all_char)
    password.append(ch)
    random.shuffle(password)
new_password = "".join(password)
print(new_password)