nums = [1, 2, 3, 4, 5]
# Write a program to return squared, squared numbers of the list nums.

# Without using map + lambda functions
squared = []
for num in nums:
    squared.append(num ** 2)

# Using map + lambda functions
squared = list(map(lambda num: num ** 2, nums))

