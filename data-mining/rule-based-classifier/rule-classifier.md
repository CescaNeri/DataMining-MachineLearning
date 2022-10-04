# Rule-Based Classifier

The basic idea is to classify records using rule sets of the type "*if .. then*". The condition used with 'if' is called the antecedent and predicted class of each rule is called the consequent.

A rule has the form: (condition) -> y

Building a model means identifying a set of rules

![](properties.jpg)

## Coverage and Accuracy

Given a dataset D and a classification rule A -> y, we define:

- **Coverage** as the portion of records satisfying the antecedent of the rule
    - Coverage = |A|/|D|
- **Accuracy** as the fraction that, by satisfying the antecedent, also satisfy the consequent
    - Accuracy = |A ∩ y|/|A|

A set of rules R us said to be **mutually exclusive** if no pair of rules can be activated by the same record.

A set of rules R has **exhaustive coverage** if there is one rule for each combination of attribute values.

## Properties

- It is nt always possible to determine an exhaustive and mutually exclusive set of rules
- Lack of mutual exclusivity
- Lack of exhaustiveness

## Rule Sorting Approach

1. Rule-based sorting (individual rules are sort according to their quality)
2. Class-based sorting (groups of rules that determine the same class appear consequently in the list)

![](sorting.jpg)

## Sequential Covering

```
set R = Ø
for each class y ∈ Y 0 y k do
    stop=FALSE;
while !stop do
    r = Learn One Rule(E,A,y)
    remove from E training records that are covered by r
    If Quality(r,E ) < Threshold then
        stop=TRUE;
    else
        R = R ∪ r // Add r at the bottom of the rule list
end while
end for
R = R ∪ {{} -> y k } // Add the default rule at the bottom of the rule list
PostPruning (R);

```
![](sequantial.jpg)

## Dropping instances from Training Set
Deleting instances from the training set serves the purpose of:

- Properly classified instances: to avoid generating the same rule again and again, avoid overestimating the accuracy of the next rule
- Incorrectly classified instances: to avoid underestimating the accuracy of the next rule

![](dropping.jpg)

