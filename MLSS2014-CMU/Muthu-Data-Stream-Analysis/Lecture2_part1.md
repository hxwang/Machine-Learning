Lecture 2: Data Stream Analysis
===============================

Lecturer: Muthu Muthukrishnan
Note by Huangxin

*~F[i]* indicates the estimation of F[i] 

**Count-Min Sketch**

- Index problem: build data as a tree or some other structure
	- A virtual array F[1,...n]
	-  update F[i]++, F[i]--
	-query, F[i]
		- key: O(n) space, maybe O(logn) space
- Main idea	
	- rather than maintain an array from [1..n], it maintains a small array
	- for each update F[i]++, 
		- for each.. estimate f(i)
	- using approxiate approach, you will fail sometimes

- Analysis:
		- F[i] <= ~F[i], with probability at least  1- \delta
			- ~F[i] <= F[i] + \epsilon * sum_{j ~=i} F[j]
		- x_{ij} is the expected contribution of F[j] to the bucket containing i, for any h
			- E(x_{ij}) = \epsilon/e * sum_{j ~=i} F[j]
		- consider Pr(~F[i] > F[i] + \epsilon * sum_{j ~=i} F[j]):
			- Pr = Pr[\any j, F[i] + x_{ij} > F[i] + \epsilon  * sum_{j ~=i} F[j])
			   = ...
			   = Pr(\any j, x_{ij} > \epsilon * E(X_{ij})) < e^(-log(1/\epsilon)) = \delta
		- Explain Pr(~F[i] > F[i] + \epsilon * sum_{j ~=i} F[j]):
		
		- Done the estimate, and show the estimate is within some distance to the true value

		- The random variable is some ? larger than the probability
		
	- Claim:
		- space used is O(1/\epsilon * log(1/\delta))
		- Time per update is O(log(1/\delta)), in depth of n
	- Comment: 
		- mathematically analyse the upper bound and upper bound
		
	
- Index Problem
	- Alice has n long bitstring and sends messages to Bob who wishes to compute the ith bit
	- Needs Omega(n) bits of communication
	
- Reduction of estimating F[i] in data stream model
	- I[1,...,1/(2\epsilpn)] such that 
		- I[i] = 1 -> F[i] = 2
		- I[i] = 0 -> F[i] = 0; F[0] <- F[0] + 2
	- Observe that ||F|| = \sum_{i} F[i] = 1/\epsilon, 
	- Estimating that F[i] <= ~F[i] <= F[i] + \epsilon*||F||
	- Therefore O(1/\epsilon) space lower bound for index problem
	
- Proof: The Count-Min Sketch(A) is as hard as Index problem(B)
	- B -> A
		-If there is an array F, could there be small argument for the ? 
	
- The challenges
	- Not all projections, dimensionality reduction are the same:
		- all prior work \Omega(1/\epsilon) space, via Johnson-Lindenstrauss
	- Not all hashing algorithms are the same:
		- pairwise independence
	- Not all approximations are sampling
		- recovering F[i] +- 0.1F[i] accuracy will retrieve each item precisely
		- e.g. insert 1000 000 items, delete 999996 items, 4 left, with such small size, sample may not be doable?

- Using Count-Min Sketch
	- For each i, determine ~F[i]
	- Keep the set S of heavy hitters, (~F[i]>=2*\epsilon||F||)
		- Guaranteed that S contains i such that F[i]>=2*\epsilon||F||, and no F[i] <= \epsilon *||F||
		- extra log n factor space for n queries
	- Problem is of database interest
	- Faster recovery: in each bucket, recover majority i:
		- F[i] > \sum_{j, same bucket as i} F[j]/2
	- eg. you have k items, randomly throw to k^2 buckets
		- the heavy one will have log distributions
			- (my idea) each one will have 1/k^2 probability to located in a random bucket, 
			  than the expected guys each bucket will have is 1/k^2 *k = 1/k
		- Takes O(logn) extra time, space
		- gives compressed sensing in L1:
			-abs(F - ~F_k)_1 <= abs(F-F*)_1 + \epsilon *abs(F)_1
			
- Useful reference
	- https://sites.google.com/site/countminsketch/

		
			
	

		
		
		
	
