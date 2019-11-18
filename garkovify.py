# Simulation Analysis & Design
# Sprint 5
# a program that generates a Garfield comic using markovify

# run with python3.6

# import markovify and pillow
import sys
sys.path.insert(0, "/usr/local/lib/python3.6/dist-packages/")
import markovify
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# markovify garfield quotes
with open("garfield_quotes.txt") as f:
    text = f.read()
garkovify = markovify.Text(text, state_size=2)

# open blank garfield comic
comic = Image.open('garfield_texting_jon.jpg')
# initialize the comic
draw = ImageDraw.Draw(comic)
# color and font for text
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('HelveticaNeue-Medium.otf', size=12)

# -----------------------------------------------------
# GARFIELD'S PANEL
txt_position = (24, 58) # starting position of text
garfield_message = garkovify.make_sentence()
while (len(garfield_message) > 40): # to fit text in panel
    garfield_message = garkovify.make_sentence()

# draw the message on the comic
draw.text(txt_position, garfield_message, fill=color, font=font)
# -----------------------------------------------------

# -----------------------------------------------------
# JON'S PANEL
txt_position = (378, 58) # starting position of text
jon_message = garkovify.make_sentence()
while (len(garfield_message) > 40): # to fit text in panel
    garfield_message = garkovify.make_sentence()
 
# draw the message on the comic
draw.text(txt_position, jon_message, fill=color, font=font)
# -----------------------------------------------------

# save the edited image
comic.save('garfield_comic.png')

