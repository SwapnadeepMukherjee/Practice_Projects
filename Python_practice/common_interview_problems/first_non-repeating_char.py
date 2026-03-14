# WAP to print first non-repeating character:

from colletions import Counter

s = "Swiss"
count = Counter(s)

print(next(c for c in s if count[c]) == 1)