# List Comprehension
l = [i for i in range(10)]

# List Comprehension with If Condition
l = [i for i in range(10) if i % 2 == 0]

# List Comprehension with If/Else Condition
l = [i if i % 2 == 0 else i * i for i in range(10)]

# Nested Comprehension
l = [(i, j) for i in range(10) for j in range(10)]

# Dictionary Comprehension
d = {i: i * i for i in range(10)}

# Set Comprehension
s = {i for i in range(10) if i % 2 == 0}

# Generator Expression (NOT EXAMINABLE)
g = (i for i in range(10) if i % 2 == 0)

print(d) # Dictionary Comprehension
print(s) # Set Comprehension
print(g) # Generator Expression (NOT EXAMINABLE)