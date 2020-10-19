![sklearn cheat sheet](https://scikit-learn.org/stable/_static/ml_map.png)

## Introducing the machine learning principles

[Machine learning](https://en.wikipedia.org/wiki/Machine_learning) is a kind of AI that can automatically react to unexpected input through experience.

[Deep learning](https://en.wikipedia.org/wiki/Deep_learning) is the dominant approach in machine learning that involves arranging ["neurons"](https://en.wikipedia.org/wiki/Artificial_neuron) into "layers", the entire concept being called ["neural nets"](https://en.wikipedia.org/wiki/Artificial_neural_network). "Deep" just refers to the characteristic that these neural nets are made up of many layers.

[Hidden layers](https://medium.com/fintechexplained/what-are-hidden-layers-4f54f7328263) are just non-input, non-output layers. You can still look at them.

For some reason (which may be explained later), while machine learning requires a developer to define *what is useful data*, whereas deep learning does [feature creation](https://en.wikipedia.org/wiki/Feature_engineering) by itself.

All in all, all of these are just names for fancy feedback loops. The computer still doesn't *understand* anything.

Deep learning isn't for every problem. They can be slow.

### What it takes to be a data scientist

A data scientist needs to know what algorithms are available to them, as well as how to use them, and how to get the desired output from them.

### Learning strategies

* Supervised
* Unsupervised
* Self-supervised
* Reinforcement

#### Supervised

**Input data is labelled** and has an expected output.

Example supervised learning algorithms:

* Linear regression
* Support vector machines (SVMs)
* Naive Bayes
* K-nearest neighbours (KNN) (Note: K-means is an unsupervised algorithm discussed later.)

Types of problems:

* Regression (the output is a continuous numeric value)
* Classification (the output is some kind of discrete tag)

Example uses:

* Product recommendation
* Image detection
* Dumb chat bot
* Language translation

#### Unsupervised

**Input data is not labelled** so the output is also not known.

Analysing the structures in the data produces the required model.

Example supervised learning algorithms:

* Clustering
* Anomaly detection
* **Neural nets**

#### Self-supervised

The model is trained with a small amount of labelled data along with a large amount of unlabelled data.

Self-supervised learning does not require a person to label the inputs. It uses correlation, metadata, or domain knowledge in the input to find the labels.

The input *can* be labelled, but the labels are ignored.

#### Reinforcement

An extension of self-supervised learning with a feedback loop. If the solution gets the answer right, it gets positive feedback. Likewise, if it gets the answer wrong, it gets negative feedback.

### Training / validiating / testing data

The **training data** *needs* to represent the entire problem domain. If you don't give it good enough data, it is not going to do what you want it to do.

> If you give it more data of a certain kind than another (e.g. a set of random numbers that has way more 5s than other numbers), it can be said as "biased".

Some of your dataset can be reserved for **validating** (checking whether your solution gets it right most of the time).

And then you test your solution out with real-world data.

#### [Underfitting vs. Overfitting](https://towardsdatascience.com/overfitting-vs-underfitting-a-complete-example-d05dd7e19765)

Underfitting: a lack of training data makes the model not follow the data close enough.

Overfitting: the model matches all the training data but doesn't represent the real world, like a polynomial function that is cranked too high.

**Both underfitted and overfitted models will result in a high testing error.**

### Algorithmic approaches

Different types of algorithms are good at solving different problems. There is no do-it-all algorithm.

#### Symbolic reasoning

Deduction: if green trees are alive and this tree is green, then it is alive.

Induction: if this tree is green and it is also alive, then green trees are alive.

#### Neural nets

Neural nets have a thing called *backpropagation*, which... `tells the previous layer of neurons how much of the solution was wrong? I think.`

#### Evolutionary algorithms

Any solution that doesn't "fit the desired output" is eliminated (survival of the fittest). Whether a solution "fits the desired output" is done with a **fitness function**.

#### Bayesian inference

One applicatin of Bayesian inference algorithms is the spam filter. If given symptoms (example in the book), it can be used to determine the probability of each disease that has that exhibits that symptom.

Apparently this has to do with the idea of not trusting outputs that others have given you. `Somehow`

#### Types

Neural nets:

* Perceptron
* Feed-forward neural net
* Hopfield net
* Radial basis function
* [Self-organising map (SOM)](https://en.wikipedia.org/wiki/Self-organizing_map)

Association rule: extracts rules that help explain the relationships between variables in data, to help discover relationships that may be hard to miss.

* [Apriori algorithm](https://en.wikipedia.org/wiki/Apriori_algorithm)
* Eclat algorithm

Bayesian: for use in classification and regression problems.

* Naive Bayes
* Gaussian naive Bayes
* Multinomial naive Bayes
* [Bayesian network and Bayesian belief network](https://en.wikipedia.org/wiki/Bayesian_network)

Clustering:

* K-means
* K-medians
* [Expectation maximisation](https://en.wikipedia.org/wiki/Expectation%E2%80%93maximization_algorithm)
* Hierarchical clustering

Decision tree: for use in classification and regression problems. Somehow lets you quickly compare new and existing data.

* Classification and regression tree (CART)
* Iterative dichotomiser 3 (ID3)
* C4.5 and C5.0
* Chi-squared Automatic Interaction Detection (CHAID)

**Deep learning**: neural nets, but if you have a lot more data. Works well with partially labelled data (semi-supervised).

* Deep Boltzmann Machine (DBM)
* Deep Belief Networks (DBN)
* Convolutional Neural Network (CNN)
* Recurrent Neural Net (RNN)
* Stacked [Auto-Encoders](https://en.wikipedia.org/wiki/Autoencoder)

Dimensionality reduction: to shrink your dataset by summarising and describing the data. For use in classification and regression problems.

* Principal Component Analysis (PCA)
* Factor Analysis
* Multidimensional scaling (MDS)
* t-Distributed Stochastic Neighbour Embedding (t-SNE)

Ensemble: grouping weaker models into one with reduced errors (`somehow`).

* [Boosting](https://en.wikipedia.org/wiki/Boosting_%28machine_learning%29)
* Bagging
* AdaBoost
* [Random Forest](https://en.wikipedia.org/wiki/Random_forest)
* Gradient Boosting Machines (GBM)

Instance-based: `the book said what it's used for, but I don't understand it.`

* K-nearest neighbours (KNN)
* Learning Vector Quantisation (LVQ)

Regression:

* Ordinary Least-Squares Regression (OLSR)
* Logistic Regression

Regularisation: penalises complex solutions, favouring simpler ones. For use with regression methods.

* Ridge regression
* Least Absolute Shrinkage and Selection Operator (LASSO)
* Elastic net
* Least-Angle Regression (LARS)

[Support Vector Machines (SVMs)](https://en.wikipedia.org/wiki/Support_vector_machine): supervised learning. Attempts to make a gap between two sets of data points or something.

* Linear support vector machines
* Radial basis function support vector machines
* One-class support vector machines (unsupervised learning)

Other:

* Future algorithms for problems of tomorrow.

### Deep learning frameworks

Frameworks are domain-specific, so you might need multiple frameworks (or libraries I guess) if you want to create a project that spans multiple domains.

Low-end frameworks:

* [TensorFlow](https://www.tensorflow.org/), still the most popular choice
* [Caffe2](https://caffe2.ai/), which is now [PyTorch](https://pytorch.org/)
* [Chainer](https://chainer.org/), something no one uses anymore
* [MXNet](https://mxnet.apache.org/)

TensorFlow supports static and [dynamic](https://github.com/tensorflow/fold) computational graphs. You can either build a graph, or use "eager execution", which evaluates operations immediately, and for some reason, does not require a computational graph.

TensorFlow is low-level so it's hard to learn but you don't really need to. Add [TFLearn](http://tflearn.org/) on top of it if you want. You use TensorFlow through [Keras](https://keras.io/) (bundled with TensorFlow), which the book claims to be a set of APIs that you use any ML frameworks with.

There is no free lunch: "You can't develop an application of any kind that is both easy to use and able to
handle truly complex situations — all while being flexible as well". Sometimes you still still need to bypass Keras to do something more complicated.
