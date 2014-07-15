Core-Sets
==========
* Lecturer: Dan Feldman
* Recorded by: Huangxin
* Date: 07/15/2014

### Introduction
- Definition
	
- Example Core-Sets
	- K-Means
	- K-segments
	- LSA/PCA/SVD
	- K-line means
	- Mixture of Gaussians
	- Google PageRank
	- Image compression
	- Non-negative matrix factorization
	- Hidden Markov chain
	- ...
- Big data
	- characteristics
		- volume: huge amount of data points
		- variety: huge number of sensors
		- velocity: data arrive in real-time streaming
	- Need:
		- streaming algorithms(use lagaraithmic memory)
		- parallel algorithms
		- simple computations(use GPUs)
- Big data computational model
	- = streaming + parallel computation
	- input: infinite stream of vectors
	- n: vector seen so far
	- log n: memory
	- M: processors
	- log(n)/M insertion time per point(Embarrassingly parallel)
- Type of Coresets
	- small (sub)set (e.g. \epsilon-nets)
	- weighted subset
	- additive weights
	- **strong Coreset**: approximates any feasible solution
	- **weak Coreset**: approximates only optimal solution
	- **weaker Coreset**: spans an approximated solution
	- **private Coreset**: using different privacy
- Core-Sets for HD images
	- procedure
		- Input image
		- Coreset for K-SVD on images
		- Denoiser for Coreset
		- Denoised image
	- how to find outlier?
		- sampling
		- you are allowed to scan the data for once, but have no chance to see it again
		- sensitivity(p)

### sample image
- Procedure
	- C is a non-uniform sample of image patches
	- patches with high variance are sampled with high probability
	- **the weight of each sample is inverse proportional to the corresponding probability** 
- how to solve optimization problem in Coreset?
- Problems
	- if there are noise? by using sampling, will you get better local optimal?
	
### Coreset techniques
- Exponential grids
	- try to optimize the size
- Important Sampling
	- reduction to \epsilon-nets
- Gradient descent
	- Frank-Wolfe Algorithm
	- PCA
- Bi-criteria approximation
	- Creating a sampling distribution

### Related Techniques
- Sketches: random projections
	- usually loss sparsity
	- input is matrix with integer entries
	- support update for entries
-...

### Application
- Real-time clustering
	- motivation
		- wifi servers, moving the servers to serve people
	- problem model
		- cluster n moving clients to k servers
		- minimize max of: client-server distance, server-server distance
	- Coreset for(unconstrained) k clusters
		


