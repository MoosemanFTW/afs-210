# Data1 = 7, False, "Apple", True, 7, 98.6 has to be tpl

# Data2 = "July", 4, 8, "Tango", 4.3, "Bingo"

# Data3 = "A", 7, -1, 3.14, True, 7  

# Data4 =  "name" = "Joe",  "age" = 26,   "active" = True,  "hourly_wage" = 14.75 has to be dict

import random

tpl = (7, False, "Apple", True, 7, 98.6)

def countList(list):
    count = 0
    for item in list:
        count += 1
    return count

print(countList(tpl))

print(tpl[3])

print(tpl.count(7))

print('-----------------------------------------')
set1 = {"July", 4, 8, "Tango", 4.3, "Bingo"}

set1.pop()
set1.add("Alpha")
print(set1)

print('-----------------------------------------')
list1 = ["A", 7, -1, 3.14, True, 7]
list1.reverse()
print(list1)
list1.pop(1)
list1.insert(1,"B")
list1.pop(5)
print(list1)

print('-----------------------------------------')
dict = {
    "name": "Joe",
    "age": 26,
    "active": True,
    "hourly_wage": 14.75
}
dict.update({"active": False})
dict["address"] = "123 West Main Street"
pay = float(dict.get("hourly_wage"))
wPay = pay * 40
print(wPay)
print(dict)