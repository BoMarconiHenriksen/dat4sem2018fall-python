from collections import Counter

# Omskriv nedenstående kode så det virker med dictionary.
""" 
def word_appearance(content):
    appearence = {}
    for line in content:
        words = line.split()[2:]
        for word in words:
            appearence.setdefault(word, 0)
            appearence[word] += 1
    return appearence

def find_most_used_word(content):
    return Counter(word_appearance(content)).most_common(1)[0][0] 
    """

# En måde at undgå den dybe nesting
# liste laves om til set
all_words = list(set{[word for line in content for word in line.splilt()[2:]]})

# Trade offcontent.word tager meget lang tid. Ikke performance venlig.
appearence = {word: content.count(word) for word in all_words}

# en nested lykke
appearence = {for line in content for word in line.split()[2:]}
