# hashtable_test.py

# Andrew Cunningham
# 20 April 2025

'''
Tests hash_table.py
'''

from hashtable_andrew import hash_table_andrew

class Payload:
    '''Defines a payload for the user's data that can be put into the hashtable'''
    def __init__(self, userID, userInfo = None, userInterests = None):
        self.userID = userID
        self.userInfo = userInfo
        self.userInterests = userInterests

    def __str__(self):
        return f"<{self.userID}, {self.userInfo}>"

user_list = {
    1: Payload(1, "A", None),
    2: Payload(2, "B" ,None),
    3: Payload(3, "C" ,None),
    4: Payload(4, "D" ,None),
    5: Payload(5, "E" ,None),
    6: Payload(6, "F" ,None),
    7: Payload(7, "G" ,None),
    8: Payload(8, "H" ,None)
}

table = hash_table_andrew(6)

print("Test 1: Add all of the elements, there will be 2 collisions")
for key, value in user_list.items():
    table.put(key, value)

table.print_hashtable()

print("/n Test 2: find a few elements")
print(table.get(2))
print(table.get(6))

print("\nTest 3: remove an element that's chained and not chained")
table.remove(3)
table.remove(8)
table.print_hashtable()

print("\nTest 4: get an element that's not there")
print(table.get(3))

print("\nTest 5: add three elements to 3")
table.put(3, Payload(3, "X", None))
table.put(9, Payload(9, "Y", None))
table.put(15, Payload(15, "Z", None))
table.print_hashtable()

print("\nTest 6: remove the middle element of 3")
table.remove(9)
table.print_hashtable()