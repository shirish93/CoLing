# CoLing
A repo of my experiments in Computational Linguistics, till they are mature enough to require their own repos.

##Papers/Projects of note

###Papers
Here's an interesting list of recent papers/works in Computational Linguistics that I've been following:

* [*Computational Linguistics and Deep Learning*](http://www.mitpressjournals.org/doi/pdf/10.1162/COLI_a_00239) by [Prof Chris Manning](https://twitter.com/chrmanning) of Stanford.

Gives a nice outline of the field, and explains how traditional NLP people should embrace Neural Networks and deep learning instead of grudging them .

* [*A Primer on Neural Network Models for Natural Language Processing*](http://u.cs.biu.ac.il/~yogo/nnlp.pdf) by [Prof Yoav Goldberg](https://twitter.com/yoavgo/). 

Is a _really, really_ good intro to the field, and brings one up-to-date with the happenings in the field.

* [*Distributed Representations of Words and Phrases and their Compositionality*](http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf) by Mikolov et al.

The paper that introduced the Word2Vec model to the world. There's many follow-up papers that are important too that I'll update this list with.
___

###Projects
* For those more humanistically inclined, [Benamin Schmidt](https://twitter.com/benmschmidt) has a fantastic post titled [Rejecting the gender binary: a vector-space operation](http://bookworm.benschmidt.org/posts/2015-10-30-rejecting-the-gender-binary.html) that will most certainly give one experiment ideas.

___
#Downloads

You can download the pre-trained models that I created [here](https://onedrive.live.com/?cid=7cc22cf7576cff2d&id=7CC22CF7576CFF2D%216178&authkey=%21AN89qA7PCfp61z4
). Look in the "Model" folder for instructions and other details.

___

##Currently Reading and Exploring

This is a list of papers I'm reading/exploring and either figuring out a way to implement or waiting for implementation. 

* Inducing semantic meaning into word embedding models(?)
* Infinite-lenght word embedding vectors
* ^- the paper that inspired it.
* The other paper I was looking at... That allows for better extraction of multiple meanings of same words. can't remember atm.

___

##Running Experiments

'''
Because the experiments can often fail miserably, making the experimenter look foolish for not considering the obvious, I have not included the models for the following in the datasets that have been made public.
'''

* Stripping the Nepali corpus of all vowels, to see how much 'one-off' words/misspellings decrease by.
* Using 3-grams to replace rare words, such that vocabulary is not reduced. Kind of like a poor man's version of char-level embeddings.
* Combining the above two, along with (...lookup the paper) to make sure multiple meanings of de-voweled words are preserved. This is STRICTLY work in progess.
