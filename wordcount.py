# put your code here.
word_file = open("twain.txt")

def word_space (word_file):

    different_words = {}
    
    for line in word_file:
        line = line.rstrip()
        # print(line)
        words = line.split()
        # print(words)

        for word in words:
            different_words[word] = different_words.get(word, 0) + 1

    # keys = different_words.keys()
    # values = different_words.values()
    
    for keys, values in different_words.items():
        print(f'{keys} {values}')


word_space(word_file)