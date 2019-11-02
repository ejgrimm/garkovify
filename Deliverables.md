# Sprint 5 Deliverables

## Make Randomized Text Great Again

Creating randomized text generators is a fun application of Markov chains. For example [this Reddit account](https://www.reddit.com/user/FloridaMan_SS/posts/), which creates random
Florida Man posts.

The model starts by picking a random starting word, then randomly choosing the next word, in such a way that words pairs occurring more
frequently in the source text are more likely to be chosen by the generator. This process then repeats, randomly choosing the next word
based on the current word.

If you'd like, you can think of it as writing using only the autocomplete feature of your phone.

Clone this public repo:

```
git clone cms380-f18-lab-2
```

The lab instructions tell you how to use a tool named `markovify` to generate random sentences. Work through the examples it contains and 
record your five best random tweets.

## Predictive Keyboards

[Botnik](https://botnik.org/) is a group that uses predictve text to make humor products. Some of their work includes:

- [*Harry Potter and the Portrait of What Looked Like a Large Pile of Ash*](https://botnik.org/content/harry-potter.html)

- [This episode](https://twitter.com/botnikstudios/status/1113130983426002944) of *Tidying Up with Marie Kondo*

- ["Bored with This Desire to Get Ripped"](https://www.youtube.com/watch?v=BtybvwLJC30) trained from Morrissey lyrics and reviews of the
P90X workout DVDs

Play around with the predictive keyboard on Botnik's website. Record your best creative work.

## Seussical

Consider the sentence

> one fish two fish red fish blue fish

Fill in the matrix describing the transition probabilities in this sentence.

```
        one   fish   two   red   blue
one
fish
two
red
blue
```

The starting state is on the left side and the destination state is on the top.


## 
