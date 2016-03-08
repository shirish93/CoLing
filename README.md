# CoLing
A repo of my experiments in Computational Linguistics, till they are mature enough to require their own repos.

##Hot Now


* [ ] Use diff-patch-match to identify common spelling errors
* [ ] Just added the IPYNB
* [x] Added the segmentation tool. Works remarkably well. 
*  [x] Need to figure out the use of Word2Vec similarities for best segmentation.

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

* [Retrofitting Word Vectors to Semantic Lexicons](http://arxiv.org/pdf/1411.4166.pdf)
* [Infinite-dimensional word embedding](http://arxiv.org/abs/1511.05392)
* [Breaking Sticks And Ambiguities With Adaptive Skip-Gram](http://arxiv.org/pdf/1502.07257v2.pdf)
* [sense2vec - A Fast and Accurate Method for Word Sense Disambiguation In Neural Word Embeddings](http://arxiv.org/abs/1511.06388)

___

##Running Experiments

```
Because the experiments can often fail miserably,
making the experimenter look foolish for not considering the obvious, 
I have not included the models for the following in the datasets 
that have been made public.

That would be the first thought. However, collecting data is a work in 
itself, and so is processing it. All the data models mentioned in 
this repo are available, most likely at my onedrive linked in the README.

If they are not, send me a message, and they will be made available at the
earliest.
```

* Stripping the Nepali corpus of all vowels, to see how much 'one-off' words/misspellings decrease by.
  
* Using 3-grams to replace rare words, such that vocabulary is not reduced. Kind of like a poor man's version of char-level embeddings.
  Out of vocabulary words (OOV) are a problem. 375 000 words >10 occurences. 1.4 M words with usage less than that.
  Mispellings + morphological complexity is a problem.
  This is ALL strictly untrained. Difference with existing work.

* Combining the above two, along with ways to retrofit them(look at the reference papers) to make sure multiple meanings of de-voweled words are preserved. This is STRICTLY work in progess.
* Related to above: Need to be able to retrofit the Nepali trained model using a Nepali dictionary. The UChicago librarian had given offer of help, but has now gone AWOL. Need to reestablish contact and work on that.

* #####Projects in digital humanities
  * Cooccurence of castes according to activities?
  * Gendered words, and the relationship between gendered pronouns and neighboring words
  * More stuff here.
<<<<<<< HEAD

##Work in Progress

* Using ~5 million Nepali tweets to train a word2vec model/use lessons from running experiments.
=======
>>>>>>> 0ee4f57bfa2899a5cfabc9490ed057274dba3200
