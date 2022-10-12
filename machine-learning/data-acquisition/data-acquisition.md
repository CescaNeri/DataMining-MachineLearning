# Data Acquisition and Processing

Data acquisition and processing are the first steps in the Machine Learning pipeline.
This is one of the most important steps for many companies, but acquiring data is a time-consuming, investment and knowledge intensive process.

**Big Data**: having large amounts of data available has been one of the reasons for the strong development of machine learning.
We are able to collect large amounts of data thanks to new storing devices and process digitalization.

## Data Acquisition

Data acquisition is the first step in developing a machine learning system. 
We can get data mainly in two ways:

1. By using **publicly available** data (quality must be checked)
2. By acquiring a new set of **specific** data (generate specific expertise for the company)
    - It is not certain that public data well represent the problem we want to solve
    - We are forced to acquire data that, due to their sensitive nature, would not otherwise available (privacy issues)
    - The company we work for already has a data collection process that we can use

**Public Datasets**

Many Universities publicly release their datasets. There are no requirements related to profit or non-disclosure agreement.
It is a consolidated practice in the world of research to share data to test the reproducibility of the results obtained.

**Acquisition of a new dataset**

Acquiring a new dataset is usually a costly process (time and money).

- Program acquisition tool
- Handle large amounts of data
- Test to find bugs
- New hardware

It is necessary to carefully consider whether it is appropriate to acquire a new dataset.

*Acquiring a new dataset does not mean acquiring only new data*

## Data Annotation

It is one of the most relevant aspect in the data acquisition phase.
It regards the **semantic content** of the data and the label depends on the problem we want to solve.

It can be numerical or categorical and associates a label to data.

Data collection without correct and timely annotation is often useless.
However, it also possible to extract knowledge from un-annotated data through **clustering.**

**Data Annotation Process**

The data annotation process can take place in several ways:

- **Manual** (long and expensive but the quality of the annotations is usually controllable and high)
- **Automatic** (each data is automatically annotated using specific tools)
- **Third parties** (all data is noted by a third party)
    - Free of charge (free use of a platform in exchange for annotated data)
    - Paid (purchase annotation time from third parties, usually from developing countries)

**Closed Set**: the pattern to be classified belongs to one of the known classes

**Open Set**: you do not know all the possible annotations, so the pattern to be classified can belong to one of the known classes or to non of these.
You can define a threshold above which a specific pattern is assigned.

## Problems in Data Acquisition

Companies usually face common problems:

- The business process produces huge amounts of data (it is impossible to acquire all the data due to physical limitation)
- Sometimes companies have a lot of old data in their databases
- In many business processes it is unclear understanding which data is possible to collect or which data is really useful for the business

