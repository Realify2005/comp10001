# The correct program to exercise 10 in week 3 worksheet of COMP10001:

letter = input("Enter a letter: ")

if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print("vowel")
if letter in 'aeiou':
    print("vowel")
if letter in ('a', 'e', 'i', 'o', 'u'):
    print("vowel")
if letter in ['a', 'e', 'i', 'o', 'u']:
    print("vowel")