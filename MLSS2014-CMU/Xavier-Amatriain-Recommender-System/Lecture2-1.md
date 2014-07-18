Collaborative Filter and Recommender System
===========================================

* Lecturer: 
* Recorded by: Huangxin
* Date: 07/18/2014

### Ranking
- Popularity and Predicted Ranking
	- Linear Model
		- e.g. f_rank(u,v) = w1*p(v) + w2*r(u,v) + b
- Definition
	- Goal; construct ranking model from training data
- Metrics
	- Quality of ranking measured using metrics as
		- normalized discounted cumulative gain
		- mean reciprocal rank(MRR)
		- Fraction of concordant pairs(FCP)
		- ...
	- But, it is hard to optimized machine-learned models directly on these measures(they are not differentiable)
	- Recent research on models that directly optimize ranking measures
- Approaches
	- Pointwise
		- ranking function minimizes loss function defined on individual relevance judgement
		- ranking score based on regression or classification
	- Pairwise
		- Loss function is defined on pair-wise preferences
		- Goal: minimize the number of inversions in ranking
		- Ranking problem is then transformed into the binary classification problem
		- RankSVM, RankBoost, RankNet, FRrank...
	- ListWise
		- Indirect Loss Function
			- RankCosine: 
			- ListNet
		- Direct
			- directly optimize IR measures through Genetic Programming
			- directly optimize measures with Simulated Annealing
			- gradient descent on smoothed version of objective function
			- SVM-MAP relaxes the MAP metric by adding it to the SVM constraints
			- AdaRank uses boosting to optimize NDCG
	