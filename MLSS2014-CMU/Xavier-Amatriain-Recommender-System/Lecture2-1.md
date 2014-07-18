Collaborative Filter and Recommender System(Novel Methods)
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

### Ranking Approaches
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
		
### Context-aware Recommendations
- Pre-Filtering Technique
	- using contextual information to select the most relevant
	-
- Post-Filtering Technique
- Contextual Modeling
	- using contextual information directly in the modeling learning phase
		- Multi-dimensional recommendation models
	- contextual variable are added as dimensions in the feature space
	- N-dimensional Model
		- Tensor Factorization
			- e.g. decompose cubic to a number of two dimensional metrics, have a tensor in the middle
			- regularization for both U and C and S
			- for the loss function, we can use square error
	- Evaluation
		- evaluate on contextual rating data and compute the Mean Absolute Error(MAE)
- Tensor Factorization
	- context does not matter
	- TF offers a way to integrate as many contextual variables ad needed
	- can be "easily" trained in a similar way to MF
	- however, factorization machine seem to work better, especially for higher dimensional spaces
- Factorization Machine
	- Generalization of regularized matrix(and tensor) factorization approaches combined with linear(or logistic) regression
	- Problem: each new adaptation of matrix or tensor factorization requires deriving new learning algorithms
		
		

	