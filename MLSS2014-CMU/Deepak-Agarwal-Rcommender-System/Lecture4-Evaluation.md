Evaluation Methods
================

* Lecturer: Agarwal
* Recorded by: Huangxin
* Date: 07/14/2014


	
### Overview
- Ideal method
	- Experimental Design: Run side-by-side experiments on a small fraction of randomly selected traffic with new method(treatment) and status quo(control)
- How to evaluate offline on logged data
	- Goal: to maximize clicks/revenue and not prediction accuracy on the entire system. Cost of predictive inaccuracy for different instances vary.
		- e.g. 100% error on a low CTR article may not matter much because it alwasy co-occurs with a high CTR article that is predicted accurately
- Usual Matrix
	- Predictive accuracy
		- Root Mean Squared Error(RMSE)
		- Mean absolute Error(MAE)
		- ...
	- Recall per event based on Replay-Match method	
		- fraction of clicked events where the top recommended item matches the licked one.
		- this is good if logged data collected from a randomized serving site...

### Methods
- Offline Replay
	- Procedure
		- random bucket logs, e.g. <user, article, click?, duration>
		- recommender system recommend a*
		- avoid explicit reward modeling -> simple
		- give provably unbiased evaluation result -> reliable
	- Details
		- x: feature vector for a visit
		- r=[r_1,r_2,...,r_k] reward vector for the K items ...
		- Estimator: 1/T \sum_t \sum_i I(h(x_t)) = i and s(x_t) =i)*r_{ti}*\alpha_t
		- if importance weights and (x_t, r_t) iid ~ p, it can be shown estimated is unbiased???
		- e.g. if s(x) is a random serving scheme, importance weights are uniform over the item set, if s(x) is not random, importance weights have to be estimated through a model
	
	
	
	


	
