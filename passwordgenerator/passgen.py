import random
import string

s1 = string.ascii_lowercase
s2= string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

# print(s4,s3)
# appends each alphabet in s one by one parsing the string

# list with lowercase 
s11 = []
s11.extend(s1)

# list with only uppercase letters
s22 = []
s22.extend(s2)

# list with only digits
s33 = []
s33.extend(s3)

# list with only specuial characters
s44 = []
s44.extend(s4)

# we will make password of 10 words
random.shuffle(s11)
random.shuffle(s22)
random.shuffle(s33)
random.shuffle(s44)
# print(s)

# print(s33)
# print(s44)
# print(s22)

password = []

password.extend(s11[0:2])
password.extend(s22[0:3])
password.extend(s44[0:3])
password.extend(s33[0:2])

random.shuffle(password)

passw = (''.join(password[0:len(password)]))
print(passw)