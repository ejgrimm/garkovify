# Sprint 5 Deliverables

## Make Randomized Text Great Again

Creating randomized text generators is a fun application of Markov chains. For example [this Reddit account](https://www.reddit.com/user/FloridaMan_SS/posts/), which creates random
Florida Man posts using a Markov model created from the r/FloridaMan subreddit.

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

- [A Bitcoin explainer](https://www.youtube.com/watch?v=tBRWJzAjkjk) trained from other Bitcoin explainers

- [This episode](https://twitter.com/botnikstudios/status/1113130983426002944) of *Tidying Up with Marie Kondo*

- ["Bored with This Desire to Get Ripped"](https://www.youtube.com/watch?v=BtybvwLJC30) trained from Morrissey lyrics and reviews of the
P90X workout DVDs

- A [makeup tutorial](https://www.youtube.com/watch?v=hSppmr_dRdQ) trained from Bob Ross episodes and YouTube makeup videos

- [Cooking for Valentine's Day](https://www.youtube.com/watch?v=ck-GZOKRBg0)

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


## Derivation

Review the pies-tanks model from the notes. Consider a more general form of the model.

There are two states, labeled 0 and 1. The one-step transition probabilities are controlled by two parameters , *p* and *q*, such that
the transition matrix is

```
                            to
                  state 0        state 1
  
       state 0    1 - p             p
from
       state 1      q             1 - q
```

Solve the global balance equations and show that the long-run probability of being in state 0 is

*π*<sub>*0*</sub> = *q* / (*p* + *q*)

and the long-run probability of being in state 1 is

*π*<sub>*1*</sub> = *p* / (*p* + *q*)

Tip: start by drawing out the chain and labeling the arcs with the probabilities from the transition matrix.


## Make Your Own Predictions

Create your own predictive text model and publish some examples of its output.

This is intended to be a creative project that you can add to your resume and talk about in
interviews, so I encourage you to experiment and come up with something fun. Part of the project is coming up with good sources and
combining them into 

You have a few options for how to proceed. You can use a tool like `markovify` or a predictive text keyboard to generate sentences, or 
you can write your own text generation code. I've included an example Python script that generates haiku-like poetry that you can use
as a starting point if you want to write your own code.

"Publishing" your work could happen in a lot of different forms, depending on what you want to do:

- Deploy a website showcasing your work
- Post some examples to Twitter, Instagram, or another social site
- Make some kind of video and upload it to YouTube
- Record a song
- Hand-make a children's picture book

Another way to "publish" your work is to turn your model into a tool that somebody else could use and then make it available, for 
example through a web front-end.
