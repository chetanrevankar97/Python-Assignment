data = [
    {"id": "111", "name": "phone", "cost": 10000, "brand": "onePlus", "rating": "5", "discount": "20",
     "category": "electronics"},
    {"id": "222", "name": "shirt", "cost": 2000, "brand": "Tommy", "rating": "5", "discount": "15",
     "category": "clothing"},
    {"id": "333", "name": "shirt", "cost": 1500, "brand": "USPA", "rating": "3", "discount": "30",
     "category": "clothing"},
    {"id": "444", "name": "pant", "cost": 2000, "brand": "levi's", "rating": "4", "discount": "20",
     "category": "clothing"},
    {"id": "555", "name": "toaster", "cost": 5000, "brand": "philips", "rating": "3", "discount": "25",
     "category": "electronics"},
    {"id": "666", "name": "earphones", "cost": 2000, "brand": "skullcandy", "rating": "2", "discount": "40",
     "category": "electronics"},
    {"id": "777", "name": "phone", "cost": 20000, "brand": "iphone", "rating": "4", "discount": "10",
     "category": "electronics"}

]

fields = {1: ["cost", False], 2: ["cost", True], 3: ["rating", True], 4: ["discount", False], 5: ["discount", True]}
inp = -1
while inp != 0:
    print("Press 1. to sort by cost Low to High")
    print("Press 2. to sort by cost High to Low")
    print("Press 3. to sort Rating")
    print("Press 4. to sort by Discount Low to High")
    print("Press 5. to sort by Discount High to Low")
    print("Press 0 to exit")
    inp = int(input("Enter your option "))
    if inp != 0:
        data.sort(key=lambda ele: ele[fields[inp][0]], reverse=fields[inp][1])
        for d in data:
            print(d)
