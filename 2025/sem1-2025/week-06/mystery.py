def mystery(x):
    x.append(5)
    x[0] += 1
    print("mid-mystery", x)

my_list = [1, 2]
print("Checkpoint 1", my_list)

mystery(my_list)
print("Checkpoint 2", my_list)

mystery(my_list.copy())
print("Checkpoint 3", my_list)