text = "Hello, World!"

freq = {}
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
        