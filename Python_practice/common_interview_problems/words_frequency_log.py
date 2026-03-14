# WAP count frequency of words in a log file:

# Approach - 1:

from collections import defaultdict

word_count = defaultdict(int)

with open("logfile.log", "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            word_count[word] += 1

for word, count in word_count.items():
    print(word, ":", count)

# Approach - 2:

from collections import Counter

with open("logfile.log", "r") as file:
	words = file.read().split()
	
word_count = Counter(words)

print(word_count)