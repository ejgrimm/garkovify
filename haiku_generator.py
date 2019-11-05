### Automatic snail haiku generator

# little straw fence-- coming down skillfully a snail
# Mokubo Temple-- a snail and Mount Fuji!

from random import choice

model = {}
starting_words = []
ending_words = []

f = open('kobayashi_issa_10000_haiku.txt')

# Read the file text as a string
text = f.read()

# Split into separate poems
# Poems are separated by a newline
#
# In general, split the text using some marker that makes sense
# You could use lines, periods, or other punctuation marks
poems = text.split("\n\n")

for poem in poems:
    
    # Split the poem into its component words
    words = poem.split()
    
    if len(words) == 0:
        continue
    
    starting_words.append(words[0])
    ending_words.append(words[-1])
    
    for w in range(len(words) - 1):
        current_word = words[w]
        
        if current_word not in model:
            model[current_word] = []
            
        model[current_word].append(words[w + 1])
        
first_word = choice(starting_words)
haiku = [first_word]

while True:
    next_word = choice(model[haiku[-1]])
    haiku.append(next_word)
    
    if next_word not in model:
        break
    
    if next_word in ending_words and len(haiku) > 7:
        break
    
print(haiku)

final = ' '.join(haiku)
print(final)
