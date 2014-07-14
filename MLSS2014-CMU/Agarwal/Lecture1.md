Recommender System
==================

* Lecturer: Agarwal
* Recorded by: Huangxin
* Date: 07/14/2014

### Introduction to Recommender Systems
- Overview
	- why? Improving relevancy of information
	- what? serve the right item to user 
	- how? a scientific discipline that involves
		- Machine learing & statistical methods
		- optimization
		- user modeling
		- NLP to understand content
- Example
	- Online Advertising
		- **Ad Network** will recommend best ads to **publishers**, with the goal to increase the user clicks
		- users click ads: statistical model
	- LinkedIn Today
		- Content Module, Objective:...
		- Recommend relationship
			- both users are items are the same. Link prediction model
		- Feed recommendation
			- network updates, content(shares by friends), sponsored updates
		- Jobs recommendation
- Goal
	- matchmaker
		- placing the "best" content in a given context for every user visit
	- match making at scale requires automation
		- serving with low marginal cost
	- personalized
		- incorporate both implicit and explicit signals about user and their intent
- Personalization at scale
	- connecting long-term objectives to machine learning
		- long-term objectives(return visits, advertising, revenue, sign-ups, job apply..)
		- formulate objectives(proxies, e.g. CTR, revenue, multi-objectives...)
		- Large scale optimization via ML, UI changes
- Algorithmic Components
	- content filtering and understanding
		- junk, spam, aboutness, topicality,..
	- user understanding
		- behavioral, intent, interests, social...
	- scoring
		- likely future value of showing item to user, e.g. CTR, relevance, revenue...
	- ranking
		- sorting based on multiple considerations, e.g., score, diversity, freshness, multiple objectives
- CTR(click through rate)
- Evaluation
	- pre-deployment
	- ...

### Scoring user-item interactions(e.g. CTR)
	- we have lot of data, is processing power enough?
		- Parameters to learn increases with sample size
			- Rate of increase is not slow in many application, e.g. new users and items added continuously
		- System dynamic and non-stationary
		- Rapid learning and quick reaction important
	- data sparsesness for personalization
		- user-item interaction matrices **heavy tailed**
			- user visits **power law**, items served **power law**, Bivariate Zipf: Owen & Dyer, 2011
	- can machine learning help?
		- some group behaviors relatively stable
			- e.g. users in San Francisco tend to read more baseball news
		- Key: modeling group behaviors(bias & variance tradeoff)
			- Coarse models: more stable but does not generalize that well
			- Granular models: less stable with few individuals
			- Sweet spot often between extremes
				- go granular but back-off via regularization when there is lack of data
		- Another advantage on the web...
	- Simple scoring model: most popular recommendation	
		- single item to recommend per visit, select most popular(highest CTR item) to maximize total clicks
			- good baseline for other sophisticated methods
			- often a good starting point, easy to implement
		- Solution: if CTRs is know, easy....
	- Simple algorithm to estimate most popular item with small but dynamic item pool
		- simple explore/exploit scheme
		- temporal smoothing
			- items CTRs change over time, provide more weight for recent
		- discount item score with repeat views
			- CTR(item) for a given user drops with repeat view by ...

	- More economical explorations? Better bandit solutions
		- consider two armed problem
		- optimal solution
	
			
		