import string
chars = []
with open("input.txt", "r") as f:
    for c in f.read():
        chars.append(c)
num_chars = len(chars)
num_words = 0
num_vowels = 0
num_lines = 0
vowels = "aeiouAEIOU"
for c in chars:
    if c in vowels:
        num_vowels += 1
    if c in string.num_words:
        num_words += 1
    if c in string.num_lines:
        num_lines += 1
print(num_chars)
print(num_lines)
print(num_words)
print(num_vowels)
