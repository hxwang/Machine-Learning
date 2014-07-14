Gradient Descent
================
*Lectuer: Mu Li
*Note by Huangxin
*Date: 07/11/2014

### Algorithms revisited
- SPD
	- process one example at a time
		- for t =1,2,... 
		- pick up an example i
		- ...
	- the cost of an iteration is small
	- often converges faster than batch algorithm such as gradient descent
	- But, is a sequential algorithm

- Parallel gradients
	- Machines process examples in parallel
		- n machines, then the delay is n-1
		- the assumption of examples are not correlated often does not hold
	- Parallel models
		- several worker groups update the parameter at the same time
		- Pro: good system performance
		- Con: may affect the convergence rate
			- 10x machines may have 2x speed up

- Minibatch SGD
	- Idea
		- process several examples(rather than 1) in an iteration
		- convergence rate: O(1/\sqrt(bT) + ...)
	- Increase effective workload
		- the overhead of a mini-batch is large
			- read from disk, communicate over network
		- why not take advantages of this batch more before throw it away?
			- add regret here to guarantee that you not go away from ...
	- Practical implementation
		- solve the subproblem approximately by early stop
	- Vary minibatch size
		- e.g. implement logistic regression
		- EMSO-CD: percent of effective traffic increase
- Conclusion
	- stochastic gradient descent is used more widely than coordinate descent
	- distributing SGD is more difficulty than CD
		- samples are often more correlated comparing to features

### Experiments
- Model/Data partition
		- learn from ...
	- Distributed Subgradient Descent
	- Billions of Parameters
		- A worker cannot cache the whole model
			- some features is not in some training data
		- For space data and linear methods, a worker only needs to cache the working set
			- local cached model
	- Compact Representation
		- A feature ID can be a string, or a random 64bit/128bit integer
		- how to access w[feature_id]
		- you can use hash!
		- But, you need to ranking things. E.g. you need to predict the probability that an ad will be click. Therefore, you need to have large space
		- But, it could be slow. Will have some branch, if , else
	- Localize keys
		- each worker machine maps globl features id into local features id 0,1,2,
		- use global key array, value array
		- save space
		- faster access
		- reuse existing libraries
		- but, need preproessing
		- but, maybe slow if there are a lot of insert
			- can be solve using online learning/LDA
- Communication API
	- Idea
		- communication over global keys
		- batched communication via ranged-based push and pull
	- Message
		- data transmission format
			- protobuf header(command, timestamp, etc)
			- a list of keys
			- a slit of values
		- will split into several messages if send to multiple machines
	- Reduce message size
		- key cache
			- both server and receiver cached he key list. If hit cache, then only send a checksum, could save half of the space
		- value compression
			- may contains a lot 0s: sparse model, user-defined filter
			- can re-encode the data 
- System components
	- System: core system
	- App: optimization application
		- gradient descent, coordinate descent
	- Parameters: globally shared parameters
		- sort key-value vector, maps
	- Loss
	- Penalty
	- ...

- Van
	- Zeromq: a convenient socket-like library
	- RDMA(Remote memory access): increasing interests, the network part can read the data directly, instead of going to CPU
- Thread Model
	- T0: postoffice
	- T1: customers, receive update_model task, calculate gradients, call parameter's push
	- T2: customer, received pulled values, updating local data
	- Note: need to pay attention whether T1 and T2 are running ...
- Conclusion
	- support extremely large model
	- asynchronous
	- flexible consistency model
	- use like writing single-thread

### Experiments
	- settings
		- in training, change "files" to the data you want
		- state configuration
		- load data:
	- implementation
		- the squared hinge loss
		- go to loss.h, you can see
			- evaluate function: input y, xw, return log(1+exp(-y+xw)).sum()
			- compute function: input y, x, ws, gradient, diag_hessian, return
		- square-hinge-loss.h, and implement evaluate and compute
		
###Conclusion
	- Industrial-scale problems
		- 100B examples, 10B features, 1T-1P size
		- problem: limited machine resources
	- Distributed implementation
		- gradient descent
		- coordinate descent
		- stochastic gradient descent
	- Future
		- scalability

	
			
	