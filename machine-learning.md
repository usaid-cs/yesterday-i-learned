# [Machine Learning](http://blog.algorithmia.com/introduction-machine-learning-developers/)

> ["All I know is my gut says _Maybe_." - Neutral Planet President](https://theinfosphere.org/Neutral_People)

_Andrew_ is a man with Canto accent ("people"), British accent ("chances", "better", "that", "so"), American accent ("talking"), Mandarin acccent ("learning", "data", "idea"), German accent ("the"), and Canadian accent ("house"). [He also co-founded coursera](https://en.wikipedia.org/wiki/Andrew_Ng) (you know, where this comes from).

## What [is machine learning]

A computer program is said to _learn_ from experience _E_ wrt some task _T_ and some performance measure _P_, if its performance on T, as measured by P, improves with E.

## Octave

Andrew says a lot of silicon valley companies model (the following) algorithms in Octave first, because many things can be done in just a few lines (even fewer than python).

The course therefore uses Octave.

## Applications

- Search engines (ranking/scoring)
- Data[base] mining / recommendation engines
- Photo tagging (classification) / computer vision
- Spam filters
- NLP
- Computational biology
- Chess
- AI (according to a man called Andrew, AI predates machine learning.)
- Other applications that humans are too stupid to write (the example given was a helicopter that does inverted flips)

## Supervised machine learning (SML)

> "Right answers given"

Supervised machine learning is used to predict things. Data is labelled before it is fed into an algorithm. After training, SML can be used to make certain guesses, like whether an image contains a bird. Examples of UML include regression and classification.

_Without a correct model, a machine cannot predict anything [useful]._

### Regression

A _regression problem_ is to predict a _continuous_ output; something like a function, f(x). Given x, give the result, even if x is not in the learning set.

### Classification

A _classification problem_ is one where you are asking the program to output _discrete_ values, e.g. 0 or 1.

_Classification_ is the act of applying the right label(s) to a given input. Naive Bayes Classifiers, Decision Trees, and Neural Networks (Neuralnets) all belong to classification.


## Unsupervised machine learning (UML)

> "Right answers not given"

Unsupervised machine learning is used to find patterns in data. _Data is unlabelled_ (the algorithm can still be asked to output continuous and discrete data). Examples of UML include K-means, hierarchical clustering, and max entropy.

Applications of UML:

- Optimisation of some sort
- Finding your friends on social networks
- Market segmentation
- Noise cancellation
- Astronomical data analysis (finding planets)

### K-means

K-means is a good first-round for understanding the structure of data. Given a number of clusters (K), it will group your data into this many clusters. How much the clusters make sense depends on you.

## Reinforcement learning

## Recommender systems
