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
- Type of Corsets
	- small (sub)set (e.g. \epsilon-nets)
	- weighted subset
	- additive weights
	- **strong corset**: approximates any feasible solution
	- **weak corset**: approximates only optimal solution
	- **weaker corset**: spans an approximated solution
	- **private corset**: using different privacy
	

