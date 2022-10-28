from guitar import Guitar

# name = "Gibson L-5 CES"
# year = 1922
# cost = 16035.4
gibson = Guitar("Gibson L-5 CES", 1922, 16035.4)
other = Guitar("Jacob' guitar", 234, 36385987)
# print(gibson)

print(f"{gibson.name} get_age() - Expected {100}. Got {gibson.get_age()}")
print(f"{other.name} get_age() - Expected {1788}. Got {other.get_age()}")
print()
print(f"{gibson.name} is_vintage() - Expected {True}. Got {gibson.is_vintage()}")
print(f"{other.name} is_vintage() - Expected {True}. Got {other.is_vintage()}")