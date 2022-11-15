# Sequential Pattern

Often, temporal information is associated with transactions, allowing events concerning a specific subject to be linked together.

A **sequence** is an ordered list of elements, each of which contains a set of events (items).
Each item is associated with a specific time instant or ordinal position.

The length of the sequence is given by the number of elements in it.

## Sub-sequence

We have sequences (like ordered purchase list from the same customer) and **sub-sequences** are sequences contained in a sequence where the mapping respects the order.

![](sequence.jpg)

The support of a sub-sequence w is defined as the fraction of sequences that contain w.

Searching for sequential patterns is a difficult problem given the exponential number of subsequences contained in a sequence.

## Temporal Constraints

Temporal constraints increase the expressiveness of sequential pattern by better defining their structure.

- **MaxSpan** defines the maximum time interval between the first and the last sequence element
- **MinGap** defines the minimum gap between events belonging to two different elements
- **MaxGap** defines the maximum gap between events belonging to two consecutive elements