
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
		- serveral per-item regression
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
	
		