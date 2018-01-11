# GPSP
This is the code for *GPSP: Graph Partition and Space Projection based approach for Heterogeneous Network Embedding*. The data and embeddings are aviable at https://drive.google.com/open?id=1PFp1E0O4I2LbitPo4_SV_0VP5hs2Z5gp.






## Requirement
* Python 3.5
* Pandas
* NLTK
* Scikit-Learn


\RestyleAlgo{boxruled}
\KwData{The heterogeneous information network $G=(V,E,T)$, number of negative samples $n$, number of walks per node $w$, walk length $l$, embedding dimension $d$, neighborhood size $k$.}
\KwResult{The latent vertex embeddings $X\in R^{|V|\times d}$}
subnetworkList = EdgeTypedBasedGraphPartition($G$)
homogeneousEmbeddingList projectiveEmbeddingList  $X$
