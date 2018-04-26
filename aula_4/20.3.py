import re

fin = open('alices_adventure.txt', 'r')
lines = fin.readlines()
fin.close()

word_count = {}

for line in lines:
    matches = re.findall('[a-zA-Z]+(?:-[a-zA-Z]+)*', line)
    for word in matches:
        word_count[word.lower()] = word_count.get(word.lower(), 0) + 1

word_items = list(word_count.items())
word_items.sort()

fout = open('alice_words.txt', 'w')
fout.write('Words                    Count\n')
fout.write('==============================\n')
for word, count in word_items:
    fout.write(f'{word:25s}{count:<5d}\n')
fout.close()