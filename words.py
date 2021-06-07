input_file = input('What is the name of the file you want to analyze? ')

file = open(input_file, 'r')
counts = dict()

for line in file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

big_counts = None
big_word = None

for word, count in list(counts.items()):
    if big_counts is None or count > big_counts:
        big_word = word
        big_counts = count

print(big_word, big_counts)
