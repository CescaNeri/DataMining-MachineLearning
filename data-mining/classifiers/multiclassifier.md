# Multi-Classifier

Construct multiple base classifiers and predict the class to which a record belongs by aggregating the classification obtained.

**How to build a composite classifier**

- Changing the training set by building more training set from the given one
- Change the attributes (random forest)
- Changing the classes considered (translate a multi-class classification into a binary one)
- Change the parameters of the learning algorithm

## Error Decomposition

Classifiers make mistakes in predictions, due to:

- **Bias**: ability of the chosen classifier in modeling events and extending the prediction to events not in the training set
- **Variance**: capability of the training set in representing the actual data set
- **Noise**: non-determinism of the classes to be determined

Different types of classifiers have inherently different capabilities in modeling the edges of regions. 
The difference between the true separation line and the average separation line represents the classifier bias.

## Bagging

Bagging allows the construction of compound classifiers that associate an event with the highest rated class from the base classifiers.

Each classifier is constructed by **bootstrapping** the same training set.

*bootstrapping: any test or metric that uses random sampling with replacement*

![](bagging.jpg)

Bagging determines the behavior of a two-level decision tree.

![](tree.jpg)

## Random Forest

It is a bagging method in which base classifiers are decision trees:
For each node in the decision tree, the split attribute is chosen on a random subset of features rather than on the entire set of features.

Random forest performs two types of bagging: one on the training set and one on the feature set.

## Boosting

An iterative approach to progressively adjust the composition of the training set in order to focus on incorrectly classified records.

- Initially, all N records have the same weight (1/N)
- Unlike bagging, the weights can change at the end of the boosting round in order to increase the probability of the record being selected in the training set

The final result is obtained by combining the result the predictions made by the different classifiers.

One of the most widely used boosting techniques is **AdaBoost:**

![](ada.jpg)
![](boost.jpg)





