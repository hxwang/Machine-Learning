Case Study
==========
* Lecturer: Agarwal
* Recorded by: Huangxin
* Date: 07/15/2014

### LinkedIn Advertising: Flow
- Ad request
- filter campaigns(targeting criteria, frequency cap, budget pacing)
- automatic format selection(campaigns eligible for auction)
- response prediction engine(sorted by bid*CTR)
- Note
	-serving constraint < 100 millsec
	-the advertiser pay only when user clicks

### CTR Prediction Models for Ads
- Feature vectors
	- Member feature vector: x_i(identity, behavioral, network)
	- Campaign feture vector: c_j(text, adv_id...)
	- Context feature vector: z_k(page type, device)
- Model
	- y_{ijk} ~ Bermoulli(p_{ijk})
	- p_{ijt} = 1/(1+exp(-s_{ijt})), ?? k or t 
	- s_{ijt} = w + s^{1,c}_{ijt} + s^{2,c}_{ijt} + ...
	- cold start component
		- s^{1,c}_{ijt} = ..
		- s^{2,c}_{ijt} = ..
	- warm-start component(per-campaign component)
- Model Fitting
	- Single machine(well understood)
		- conjugate gradient
		- L-BFGS
		- Trusted region
		- ...
	- Model Training with Large scale data
- Model considered
	- CONTROL: per-campaign CTR counting model
	- COLD-ONLY: only cold-start component
	- LASER: cold start + warm start
	- LASER-EE: LASER with explore/exploit using Thompson sampling

	