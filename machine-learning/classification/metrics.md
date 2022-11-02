# Metrics

The **prediction** of the system is an extremely important step.
It allows you to calculate the performance of the system through metrics, to understand if the system responds correctly with respect to what was designed and desired.

The computation of metrics is also linked to the achievement of certain contractual obligations.

## System Performance with Classification

Generally, it is preferred to use a measure linked directly to the semantics of the problem.
The **metric** examines the prediction of the model and the label provided in input (GroundTruth and prediction).

```
Accuracy = # pattern correctly classified / total patterns
```
## Confusion Matrix

The confusion matrix is very useful in multi-class classification problems to understand how errors are distributed.

- Rows: classes of GT
- Columns: predicted classes

A *cell (r,c)* shows the percentage in which the system predicts class c for a ground truth class r.

Ideally, the matrix should be diagonal and high values (off diagonal) indicate concentrations of errors.

![](confusion.jpg)

In the example, the class "0" is often confused with "6".

