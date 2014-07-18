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
	- ...
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
- Factorization Machine(Rendle,2010)
	- Generalization of regularized matrix(and tensor) factorization approaches combined with linear(or logistic) regression
	- Problem: each new adaptation of matrix or tensor factorization requires deriving new learning algorithms
	- Approaches: treat input as a real-valued feature vector
		- model both linear and pair-wise interaction of k features(i.e. polynomial regression)
		- traditional machine learning will overfit
		- ...
	- L2 regularized
		- regression: optimize RMSE
		- classification: optimize logistic log-likelihood
		- ranking: optimize scores
	- Can be trained using
		- SGD
		- Adaptive ...
	- Learning parameters
		- number of factors
		- iterations
		- initialized ...
		
### Deep Learning
- DL for collaborative Filtering
	- e.g. how Spotify users RecurrentNetworks for Playlist prediction, [check here](http://erikbern.com/?p=589)
- Model
	- we assume p(y_i|h_i) is a normal distribution, log-likelihood of the loss is just the negative L2 loss, -(y_t - h_t)^2 
	- we can specify that h_(i+1) is the previous given an previous visible
- Problem
	- in order to predict, we need to define a distribution of p(y_i|h_i)
	- ...

### Similarity
- Similarity can refer to different dimensions	
	- e.g. metadata/tags
	- e.g. user play behavior
	- e.g. user rating behavior
- You can learn a model for each of them and finally learn an ensemble
- graph-based similarity
	- Sim-Rank(Jeh & Widom, 02): two objects are similar if they are referenced by similar objects

### Social and Trust-based Recommenders
- Definition
	- a social recommender system recommends items that are "popular" in the social proximity of the user
	- This idea of trust is central in social-based system
	- it can be a general per-user value that takes into account social proximity but can also be topic-oriented
- Trust Inference
	- Goal: select two individuals, i.e. the source(node A) and sink(node C), and recommend to the source how much to trust the sink
- Major algorithms--Networks
	- Advogato(Levien)
	- ...
- Building Recommender Systems Using Trust
	- use trust as a way to give more weight to some users
	- Trust for collaborative filtering
		- use trust in place of (or combined with) similarity...
- Demographic Methods
	- aim to categorize the user based on personal attributes and make recommendation based on demographic classes	
	- ...
	
### HyBrid Approaches
	- Weighted
		- combine the results of different recommendation techqniues into a single recommendation list
		-e.g. Example 1: a linear combination of recommendation scores
		-e.g. treat the output of each recommender(collaborative, content-based and demographic) as a set of votes, ...
	- Switching
		- The system users criterion to switch between techniques
		- e.g. if the content-based system cannot make a recommendation with sufficient confidence, then a colaborative recommendation is attempted
	- Mixed
		- Recommendations from more than one technique are presented together
		- define a way to mix the results
		- however, it does not get around the "new-user" start problem
	- Feature Combination
		- feature can be combined in several directions
	- Cascade
		- our recommendation technique is employed first to produce a coarse ranking of candidates and a second technique refines the recommendation
		- conscadingallows the system to avoid emloying the second, low-priority...
	- Feature Augmentation
		- ...

### A practical example in Netflix Prize
	
	
			
		
	
		

	