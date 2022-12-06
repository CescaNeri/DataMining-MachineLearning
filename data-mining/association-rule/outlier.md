# Outlier Detection

An **anomaly** is a pattern in the data that does not conform to expected behavior.

Anomalies can be caused by different aspects:

- Data from different classes (an object may be different because it belongs to different class).
- Natural variations (many phenomena can be modeled with probabilistic distributions in which there is a probability that a phenomenon with very different characteristics from others will occur).
- Measurement errors (due to human or device errors).

We can identify different types of anomalies:

1. **Spot** anomaly (an individual data instance is anomalous with respect to data)
2. **Contextual** anomaly (a single instance of data is anomalous within a context)
3. **Collective** anomaly (a set of related instances is anomalous and requires a relationship between data instances)

## Outliers application

Data from different classes, for example, can be used to identify a different purchase pattern followed by fraudsters who stole a credit card.
Also, intrusion detection can be used to monitor events occurring in a computer system and analyze them for intrusion.

In the healthcare sector, outliers can be useful to detect abnormal data, disease outbreaks or instrumentation errors.

Finally, in the industrial sector, anomalies detection can be used to identify failures and malfunctions in complex industrial systems, intrusions in security systems, suspicious events in video surveillance and abnormal energy consumption.

Anomaly detection follows different approaches:

- **Supervised** anomaly detection, where labels are available for both normal and anomaly data.
- **Semi-supervised** anomaly detection, where labels are available for *normal* data.
- **Unsupervised** anomaly, where labels are not available and validation is complex since the real anomaly number is unknown.

**Anomaly Detection Outputs**

- **Label**, each test instance is assigned a label which is the outcome of classification-based approaches.
- **Score**, each test instance is assigned an anomaly score which allows the instance to be sorted

Anomalies are rare events which make it difficult to label these with high accuracy.
**Swamping** is the error of labelling normal events as anomalies while **masking** is the error of labelling anomalous events as normal.