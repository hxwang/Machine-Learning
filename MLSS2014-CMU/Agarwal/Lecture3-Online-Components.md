Online Component
================

* Lecturer: Agarwal
* Recorded by: Huangxin
* Date: 07/14/2014

### Introduction
- why online component
	- cold start
		- new users/data keep coming in
		- how to quick update the model
	- concept drift
		- item popularity, user interest, mood, and user-to-item affinity may change overtime

### Online components for most popular recommendation
- overview
	- Most popular recommendation(no personalization, all users see the same thing)

- online models
	- Definition 
		- How to track the changing CTR of an item
		- Data:
		- Problem definition: given c1, n1, ..., ct, nt predict the CTR p_{t+1} at time t
	- Model: Dynamic Gamma-Poisson
		- model-based approach
			- (c_t| n_t, p_t) ~ Poisson(n_t,p_t)
			- ...
		- Derivation
- Intelligent Initialization: Pior Estimation
	- Prior CTR distribution: Gamma(mean, var)

### Explorer/Exploit
- Problem Definition
	- determine(x_1,x_2,...,x_k)[k items] based on clicks and views observed before t in order to maximize the expected total number of clicks in the future
	- if you are myopic, you may think it is the one with the highest clicks so far. But this doesn't look into the future
	- solution: like dynamic programming
- Example
	- simplified setting: two items
	- if we only make a single decision, we select the one with higher CTR
	- if we make several decision???
- **Multi-Armed Bandits**
	- Bayesian approach
		- seeks to find the Bayes optimal solution to a Markov decision process(MDP) with *assumptions on distributions*
			- representative work: Gittins' Index
		- Markov decision process(MDP)
			- consider a slightly different problem setting
			- infinite time horizon, but future rewards are geometrically discounted
			- theorem[Gittins 1979]: the optimal policy decouples and solves a bandit problem for each arm independently
				- significantly reduce the problem dimension
	- Minimax approach
		- seeks to find a scheme that incurs bounded regret(with no or mild assumptions about the probability distribution)
		- compute the priority of each arm i in a way that the regret is bounded, lowest regret in the worst case
			- priority = observed payoff + factor representing uncertainty
		- one common policy is UCB1

### Summary
- classical multi-armed bandits
	- a fixed set of arms with fixed rewards, no delay in feedback
- Bayesian approach
- minimax approach
- heuristics
	- \epsilon-greedy: random exploration using faction \epsilon of traffic
	- softmax: pick arm i with probability related to temperature and predicted CTR of item i 
	- Thompson sampling: index = drawing posterior of an arm
	


