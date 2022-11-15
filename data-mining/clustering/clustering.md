# Clustering

Clustering analysis aims at finding groups of objects such that objects that belong to the same group are more similar to each other than objects belonging to different groups.

CLustering is NOT supervised classification (it assumes classes to be known) or segmentation (partition rule is given) or querying a database (the selection and grouping criteria are given).

## Types of clustering

We can distinguish between:

- **Partitioning clustering**: a division of objects into non-overlapping subsets (clusters), in which each object belongs exactly to a cluster.
- **Hierarchical clustering**: a set of nested clusters organized as a hierarchical tree.
- **Exclusive vs non-exclusive**: in non-exclusive clustering, points can belong to multiple clusters.
- **Fuzzy vs non-fuzzy**: in a fuzzy clustering a point belongs to all clusters with a weight between 0 and 1.
- **Partial vs complete**: in a partial clustering, some points may not belong to any of the clusters.
- **Heterogeneous vs homogeneous**: in a heterogenous cluster, clusters can have very different sizes, shapes and densities.

Similarly, we can identify different types of **clusters**:

- **Well-separated clusters**: each point in the cluster is closer (more similar) to any other point in the cluster than any other point that does not belong to the cluster.
- **Center-based clusters**: a point in the cluster is closer to the *center* of the cluster, rather than to the center of each other cluster.
    - Cluster center = **centroid**
- **Contiguous clusters** (nearest neighbor): a point in a cluster is closer to one or more other points in the cluster than to any point not in the cluster.
- **Density-based clusters**: a cluster is a dense region of points, which is separated by low-density regions from other regions of high density.
- **Conceptual clusters**: clusters with shared properties or in which the shared property derives from the whole set of points.

## K-means Clustering

![](k-means.jpg)

Initial centroids are often chosen randomly (clusters produced vary from one run to another).

![](sse.jpg)

## Converge and Optimality

There is only a finite number of ways to partition n records into k groups.
So, there is only a finite number of possible configurations in which all the centers are centroids of the points they possess.

If there are K real clusters, the probability  of choosing a centroid from each cluster is very limited.

Some solutions to this problem, include:

- Run the algorithm several times with different centroids.
- Perform a sampling of the points and use a hierarchical clustering to identify k initial centroids.
- Select more than k initial centroids and then select the ones to use from these.
- Use post-processing techniques to eliminate the identified erroneous cluster.
- Bisecting K-means (less affected by the problem).

**Handling empty clusters**

The K-means algorithm can determine empty clusters if, during the assignment phase, no element is assigned to a centroid.

In this case, different strategies can be used to identify an alternative centroid:

- Choose the item that most contributes to the value of SSE (sum of squared errors).
- Choose an item of the cluster with the highest SSE (the cluster will split into two clusters that include the closest elements).

**Handling Outliers**

The goodness of clustering can be negatively influenced by the presence of outliers that tend to shift the cluster centroids so that to reduce the increase in the SSE they determine.

Outliers, if identifies, can be eliminated during *preprocessing.*

**Limits of K-means**

The k-means algorithm does not achieve good results when natural clusters have:

- Different size (the value of SSE to the identification of centroids so as to have clusters of the same size if the clusters are not well-separates)
- Different density (more dense clusters lead to smaller intra-cluster distances, so less dense areas require more medians to minimize the total value of SSE)
- Non-globular shape (SSE is based on an Euclidean distance that does not take into account the shape of objects)
- Data contains outliers

**Possible Solutions:**

- Use a higher k value, thus identifying portions of clusters
- The definition of natural clusters then requires a technique to bring together the identified clusters
- **Elbow method**: execute k-means several times with increasing values for k

