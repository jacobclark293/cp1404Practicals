numbers = [3, 1, 4, 1, 5, 9, 2]

# 3
# 2
# 1
# [3, 1, 4, 1, 5, 9]
# 1,5
# True
# False
# False
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


# 1. Change the first element of numbers to ten (string)
numbers[0] = "ten"

# 2. Change the last element of numbers to 1
numbers[-1] = 1

# 3. Get all the elements from numbers except the first two (slice)
del numbers[0:2]

# 4. Check if 9 is an element of numbers
9 in numbers