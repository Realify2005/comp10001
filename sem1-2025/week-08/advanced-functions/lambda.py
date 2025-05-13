def last_char(s):
    return s[-1]

last_char = lambda s: s[-1]

animals = ['cat', 'dog', 'elephant', 'giraffe', 'hippo']
sorted_animals = sorted(animals, key=last_char)
sorted_animals = sorted(animals, key=lambda s: s[-1])

