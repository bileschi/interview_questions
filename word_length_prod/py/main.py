# Load the file and print the lenghth.

IN_FILE = "/usr/share/dict/words"
file1 = open(IN_FILE, 'r') 
words_w_newline = file1.readlines()
words = []
for w in words_w_newline:
    words.append(w.strip())
print(len(words))

# organize the words into a map
# len(word)->map(word -> set of letters in word)

# Get list of all lengths
lens = set()
for w in words:
    lens.add(len(w))

# initialize d to have an empty map at each word len
d = {}
for word_len in lens:
    d[word_len] = {}

for word in words:
    word_len = len(word)
    d[word_len][word] = set(word)

# Get schedule of wordlen pairs (in desc order)
schedule = []
for len1 in lens:
    for len2 in lens:
        # Only include those where len2 <= len1
        if (len2 > len1):
            continue
        prod = len1 * len2
        schedule.append((prod, len1, len2))

# sort schedule by prod
schedule = sorted(schedule, reverse=True)

def go():
    for (prod, len1, len2) in schedule:
        for word1 in d[len1]:
            set1 = d[len1][word1]
            for word2 in d[len2]:
                set2 = d[len2][word2]
                if set1.intersection(set2):
                    continue
                print(f"{prod} , {len1} , {len2} , {word1} , {word2}")
                return

go()
