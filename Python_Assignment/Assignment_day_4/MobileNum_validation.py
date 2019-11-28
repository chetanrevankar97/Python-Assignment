'''
Note mobile number
From current dir extract files with .log and read their email id
'''

import re

number = input("Enter Mobile Number")

pattern = "^[789][0-9]{9}$"
data = re.search(pattern, number)
if data:
    print("Enter 10 digit number")

else:
    print("Thank You ")
