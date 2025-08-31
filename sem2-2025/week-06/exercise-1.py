# Exercise 1a
seq = [4, 1, 3, 2, 5]
seq.sort()
print(seq) # [1, 2, 3, 4, 5]

seq = seq.sort()
print(seq) # None


# Exercise 1b
seq = [4, 1, 3, 2, 5]
new_seq = sorted(seq) # Don't use sort(seq)! NameError: name 'sort' is not defined
print(new_seq) # [1, 2, 3, 4, 5]

new_seq = seq.sort()
print(new_seq) # None


# Exercise 1c
seq = [4, 1, 3, 2, 5]
seq.append("hi")
print(seq) # [4, 1, 3, 2, 5, 'hi']

seq = seq.append("hi")
print(seq) # None