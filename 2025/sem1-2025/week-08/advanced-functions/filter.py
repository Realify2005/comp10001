nums = [1, 2, 3, 4, 5]
# Write a program to return a list of numbers greater than 2

# Without using filter + lambda functions
greater_than_2 = []
for num in nums:
    if num > 2:
        greater_than_2.append(num)

# Using filter + lambda functions
greater_than_2 = list(filter(lambda num: num > 2, nums))

