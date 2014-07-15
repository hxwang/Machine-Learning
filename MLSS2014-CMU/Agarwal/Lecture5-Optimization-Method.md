Optimization Methods
====================

* Lecturer: Agarwal
* Recorded by: Huangxin
* Date: 07/14/2014

### Motivation
- CTR & Session
	- CTR increase, session may decrease, which one prefer?

- Problem Setup
	- Given n articles from K different web properties
	- Consider two objectives: click and time-spent
		- Max time-spent s.t. click >= 95% optimal
	- Estimate CTR


### Problem Model
- Segmented Click Shaping(KDD'11)
	- CTR: p_ij, time-spent d_ij, serving plan x_ij
	- Objective: Clicks and Time-Spent
		- Linear Program Formulation
			- max: totalTime(x)
			- s.t. totalClicks(X) >= \alpha* totalClicks*
			- total-time(x,p_k) >= \beta*total-time*(p_k), \any k \in I
				- time-spent in property p_k
- From segmented to Personalized
	- change i->u, does this work??
		- there are many new users when serving online
		- sparsity
- From Primal to Dual
	- Observations
		- Primal variables x: millions of variables
		- only tens of non-trivial constraints
	- Formulation
		- Primal Form: max_x TotalTime(x)
		- Constraints: 
			-s.t. totalClicks(X) >= \alpha* totalClicks*
			- total-time(x,p_k) >= \beta*total-time*(p_k), \any k \in I
		- Can we operate in dual?
			- Idea: covert it to strictly convex -> conversion from dual to primal
				- min_x 1/2 \gamma ||x-q||^2 - totalTime(x)
				- s.t. totalClicks(X) >= \alpha* totalClicks*
				- s.t. total-time(x,p_k) >= \beta*total-time*(p_k), \any k \in I
			- Lagrangian
- Conversion Algorithm
	- Similar to conversion algo used in advertising
		- solve QP and to obtain dual solution \miu (K+1 numbers)
		- For each user, compute and sort c_{uj}; the determine x_{uj} in linear time
	- Handle unseen users
		- as long as we can predict p_{uj} and d_{uj}
	- Allow for approximation
		- solving QP can be time consuming
		- we only need to determine k+1 number in dual...
		
### Experiments
- Metrics
	- CTR ratio: CTR relative to a baseline model
	- TS ratio: 
- Conclusion
	- it is possible to increase users' time-spent on all properties while losing a negligible fraction of clicks
	- personalized click shaping provides significant improvement over segmented click shaping
	- Lagrangian duality allows efficient construction of personal serving plan based on a small number of dual variables
- Future work
	- how to handle multiple positions, multiple content modules
	- beyond per-epoch constraints, long-term multi-epoch constraints

### Summary
	- Modern recommendation systems on the web crucially depend on extracting intelligence from massive amounts of data collected on a routine basis
	- Lots of data and processing power not enough, the number of things we need to learn grows with data size
	- Extracting grouping structures at coarser resolutions based on similarity(correlations) is important
		- ML has a big role to play here
	- Continuous and adaptive experimentation in a judicious manner crucial to maximize performance
		- Again, ML has a big role to play
	- Multi-objective optimization is often required, the objectives are application dependent
		- ML has to work in close collaboration with engineering, product & business execs

### Challenges
- Scoring
	- Multi-position optimization
		- explore/exploit, optimal subset selection
	- explore/exploit strategies for large content pool and high dimensional problems
		- some work on hierarchical bandits but more need to be done
	- Constructing user profiles from multiple sources with less than full coverage
	- Content understanding
	- Metrics to measure user engagement(other than CTR)
