# Census Data

Identify relevant attributes:

- Capital gain/loss are not relevant because many attributes are zero
- Age (we expect it to be linear but the majority of >50k is in the range of 40 years)
- Work class is unbalanced (the majority of people works in private), coverage is very low
- Education number 
- Marital status (interesting, married is different)
- Occupation (interesting)

Education and education-num are perfectly correlated (it is duplicated).

![](census.jpg)

We can enhance accuracy by replacing missing values:

Preprocess - filter - unsupervised - attribute - replacemissingvalues

