Users = {"Tony": "luke", "Abrar": "Dheeru", "SreeKanth": "Sirisha"}

val1 = input("Enter User Name: ")
val2 = input("Enter Password: ")


class InvalidUser(Exception):
    def __init__(self, msg="Invalid User"):
        Exception.__init__(self, msg)

try:
    for i in Users:
        if val1[val2] == i:
            raise InvalidUser

        else:
            print("Welcome")

except InvalidUser as e:
    print(e)

