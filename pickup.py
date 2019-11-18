# a program that generates pickup lines

# import markovify
import sys
sys.path.insert(0, "/usr/local/lib/python3.6/dist-packages/")
import markovify

# read pickup lines
with open("pickup_lines.txt") as f:
    text = f.read()

# markovify pickup lines
model = markovify.Text(text, state_size=2)

# print 10 pickup lines
for i in range(10):
    print(i + 1, ">>", model.make_sentence())
    print('\n')

