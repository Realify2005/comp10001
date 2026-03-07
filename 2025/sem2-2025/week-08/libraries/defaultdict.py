from collections import defaultdict

text = "Hello, World!"

freq = defaultdict(int)
for char in text:
    freq[char] += 1

