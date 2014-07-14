
* Lecturer: Agarwal
* Recorded by: Huangxin
* Date: 07/14/2014

### Model & Methods
- Scoring methods
	- Feature based(good for cold start)
		- supervised
			- Cosine similarity s(x_i, x_j) = x_i'*x_j/(|x_i|*|x_j|)
			- Ridge logistic regression for binary response
		- unsupervised
	- collaborating filtering(good for warm start)
		- score user-item pairs using past response data
			- user-user & item-item similarities, matrix factorization
			- Example using user-user similarity
			- s_{ij} = \bar{y_i} + k*\sum_a w_{a,i} (y_{i,j) - \bar{y_i})
		- estimating similarities
		- Matrix factorization
			- Elegant parametrization to incorporate user-user and item-item similarities
			- s_{ij} = u_i'*v_j, u_i is item factor, v_j is user factor
			- ...
	- hybrid: both cold and warm start
		- Heuristic-based approaches
			- linear combination of regresssion and CF models
			- use content based to fill up entries, then use CF
			- Filterbot
				- add user features as psuedo users and do collaborative filtering
		- Model-based approaches
			- add feature-based regression to matrix factorization (Agarwal and Chen 2009)
			- ad topic discovery(from textual items) to matrix factorization
		
### Offline Model
- Per-item regression models
	- for application where most user have few visits, we can take a simpler approach
		- per item models(regression) based on user covariates attractive in such cases
			- y_{ijt} ~ Bernoulli(p_{ijt})
			- s_{ijt} = log()/(p_{ijt})(1-p_{ijt})
		- several per-item regression
			- s_{ijt} = x_{ij}' * Axj + x_{it}'B\theta_j, where x_{it}' affinity to old items...
- Per-user, per-item models via 
	- Latent Factor Models
		- Latent user factor (\alpha_i, u_i vector)
		- Latent item factor: (\beta_j, v_j vector)
		- N users T(E(y_ij)) = \miu _ \alpha_i + \beta_j + \miu_i'*B*v_j
		- (Nn + M..) items, will overfit
	- optimization
		- through iterated conditional modes
		- other variations like constraining
	- Beyesian probabilistic matrix factorization
		- Fully Bayesian treatment using an MCMC approach, significant improvement
		- Interaction as a full Bayesian hierarchical model

### Regression-based Factorization model(RLFM)
- How to incorporate features?
	- Main idea: flexible prior, predict factors through regressions
	- Seamlessly handles cold-start and warm-start
	- *modified prior to incorporate features*
- Advantage of RLFM	
	- better regularization of factors
- Computing the E-step
	- Stochastic EM(Markov Chain EM; MCEM)
		- computer expectation by drawing samples from p(\delta|\theta_old,Y)
		- effective
	- **Monte Carlo E-step**
		- through a vanilla Gibbs sampler(conditional closed form)
		- Let o_ij = y_ij - \alpha_i - \beta_j - x_ij'*b
		- e.g. if you watch a movie that everyone like, then there is not much information that could be collected
			
### Add topic discovery into matrix factorization: Factorized LDA(fLDA)
- Overview
	- LDA: Latent Dirichlet Allocation, give topic representation of  each document
		- do a supervised LDA...
		- use the rating given by user
	- modeling the rating y_ij that usre i gives to item j as the user's affinity to the topics that the item has
		- y_ij = ... + \sum_k s_ik *\bar(z_jk), s_ik is user i's affinity to topic k, z_jk = pr(item j has topic k)
	- LDA is effective for unsupervised topic discovery (BLei' 03)
		- for each topic k, draw a word distribution 
		- for each item j, draw a topic distribution
		- for each word, say the nth word, in item j
			- draw a topic z_jn for that word from \theta_j
			- ...
- fLDA model
	- Response: y_{ij} ~ N(\miu, ...)
	- Supervised Topic Assignment
		- new: likelihood of obseverd rating by users who rated item j when z_jn is assign to work n
- Experiment
	- Task: predict the rating that a user would give a movie

	
		