Parameter Server Tutorial
===============

Lecturer: Mu Li

Notes recorded by Huangxin

- Newton method
	- Convex objective function function
	- Nonnegative second derivative
	
- Parallem Newton method

**BFGS algorithm**
- Basic Idea
	- Newton-like method to compute descent direction
	
- Properties
	- Simple rank 2 update for B
	- Use matrix inversion lemma to update inverse
	- Memory-limited versions L-BFGS
	- use toolbox if possible
	
**Coordination Descent**
- Basic Idea
	- update one feature each time
	- can oslve this small problem by expensive method, say Newton method
		- for t = 1,2, ...
		 -pick up feature i(in random)
		 -solve min_{w_i} f(w) by fixing w_1, ..., w_{i-1}
	- Drawback: this is a sequential method, slow, cannot run multiple thread
	- Pro: work very well for sparse data(liblinear)
- Shotgun
	- If you have n threads, why not let each thread update one feature
	- works well if features are not so correlated:
		- #of threads = O((#features)/(p(xTx))
	- one feature may be too small, you need to pay the thread synchronizations

**Block descent**
- Basic idea
- Comments
	- better than sequential coordination descent
- implement BlockCD
	- if block is big enough, the synchronizations cost and other cost are relative trivial
	- multi-threaded within in a block	
- Asynchronous Updating
	- computation use cpu power, but push and pull only use network
	- idea: keep the CPU busy
	- parallel CPU and I/O, hide synchronizations cost
	- a worker: eventual consistency(#TODO: check distributed system)
	- we only allow one block is inconsistent
- Analysis
	- L_{var}: correlation of features in a block
	- L_{cov}: correlation of features between too neighbour blocks
	- \tau bounded delay
	- fixed learning rate guarantee converge
- Implement via ParaServer
	- push gradients to server
	- pull weights from server
	- Task: a push, pull, or any user-defined function
		- one iteration (can contain push and pull)
	- Task dependency graph:
		- for each task, sequential dependency
		- between tasks: eventual dependency
		- bounded delay?
- Implement bounded-delay:
	- executed at the scheduler
	- for each iteration, for each block, update

**Experiments**

- Sparse Logistic Regression
	- min_{w \in R^p} \sum_{ log(1 + exp(-y_i(x_i,w)))} + \lambda ||w||_1
	- examples: 170B, features 65B, raw text data 636T, machines 1000, cores 16,000
	- Compare: L-BFGS, BlockCD(sequential), Bloack(bounded delay)
		- 1 at first converge slow, and then converge fast at the end
		- parameter server only use very small time for waiting (since we use bounded-delay)

	
	
	

	