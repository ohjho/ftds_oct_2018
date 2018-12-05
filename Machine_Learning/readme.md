# Recap of Machine Learning

## Preliminary
* Linear Algerba: needed for [dimensionality reduction]
* Calculus: needed for optimisation of which the most common one is [gradient descent]

## Machine Learning
### Algorithims
#### Supervised
where **target** is provided in training the model
* **Regression** models are for where target value is continuous, not discrete
* **Classification** models are for targets that are discrete (e.g. categories, classes, binary)
* **Decision Tree**
  * like [lattice model](https://en.wikipedia.org/wiki/Lattice_model_(finance)) in option pricing

#### Unsupervised
where no **target** is provided in training the model

### Tools
* [scikit-learn](): good for most cases
* [azure ML studio](): good for visual understanding of the ML workflow
* [tableau public](): good for Exploratory Data Analysis
### Overfitting the model
* the [Bias Variance trade-off](https://towardsdatascience.com/understanding-the-bias-variance-tradeoff-165e6942b229) and Irreducible Error
  * in the context of algo trading [here](https://www.quantstart.com/articles/The-Bias-Variance-Tradeoff-in-Statistical-Machine-Learning-The-Regression-Setting) and [here](https://mechanicalforex.com/2016/08/irreducible-error-in-trading-beyond-the-bias-variance-trade-off.html)
  * **Irreducible Error**: IMO we are just using models or systems to understand reality, which can never be perfect because it is the natural limitation of the human intellect. _That we are always trying to use our logical mind to understand things that are meant to be experienced._ So there always got to be some noise, some outliners that we can't wrap our mind/ model around and can't be understood. But that doesn't mean the model isn't good. What determine while a model is good or not depends on how it is used!
### Hyper Parameters tuning
### Bagging vs Boosting

## Deep Learning
* Neural Network
  * understanding [Epoch vs Batch Size vs Iterations](https://towardsdatascience.com/epoch-vs-iterations-vs-batch-size-4dfb9c7ce9c9)
  * and in the context of back propagation, here's a commentary on [batch vs stochastics gradient descent](https://arxiv.org/pdf/1609.04747.pdf) and what is [mini-batch](https://stats.stackexchange.com/questions/337608/stochastic-gradient-descent-vs-mini-batch-size-1)
* CNN
* Image Recognition:
  * CNN + ANN
  * layers -> pooling -> flattening -> neural network [[visualized](http://www.scs.ryerson.ca/~aharley/vis/conv/flat.html)]

### TensorFlow 101
* What is a [Tensor](https://en.wikipedia.org/wiki/Tensor)?
* [What is TensorFlow](https://www.infoworld.com/article/3278008/tensorflow/what-is-tensorflow-the-machine-learning-library-explained.amp.html)
* [Why use Graphs in TensorFlow?](https://www.tensorflow.org/guide/graphs)
  * [TensorBoard](https://github.com/tensorflow/tensorboard/blob/master/README.md) could be used to visualize these Graphs
* [Example of models built in TensorFlow](https://github.com/tensorflow/models)
### Tools
* [keras]() with [tensorflow blackend]()
