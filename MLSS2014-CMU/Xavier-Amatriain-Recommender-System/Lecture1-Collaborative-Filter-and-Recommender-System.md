Collaborative Filter and Recommender System
===========================================

* Lecturer: 
* Recorded by: Huangxin
* Date: 07/17/2014

### Introduction
- What?
	- Search is what you do when you are looking for something
	- Discovery is when something wonderful what you didn't know existed, or didn't know how to ask for, finds you.
- Information overload
	- In 2105, consumption will raise to 74GB a day per person (UCSD study 2014)
- The value of recommendations
	- Netflix: 2/3 of the movies watched are recommended
	- Google News: recommendations generate 38% more click through
	- Amazon: 
- Recommender problem
	- estimate a utility function that automatically predicts how a user will like an item
	- based on: Past behavior, relations to other users, item similarity, ...
- Definition
	- let *C* be the set of all users and let *S* be the set of all possible recommendable items
	- Let *u* be the utility function measuring the usefulness of item s to c
- Two step process
	- offline part 
		- learning process
		- model or clusters []
	- online part 
		- decision process(context as input)
		- recommended items
		
### Traditional Methods
- **Collaborative Filtering**: recommended items based only on the users past behavior
	- user-based: find similar users to me and recommend that they like
	- item-based: find similar items to those that I have preciously like
- **Content-based**: recommend based on item features
- **Personalized Learning to Rank**: Treat recommendation as a ranking problem
- **Demographic**: Recommend based on user features, e.g. where they come from etc.
- **Social recommendations**(trusted-based)
- **Hybrid**: combine any of the above

### Characteristic
- Recommendation as data mining
	- The core of the Recommendation Engine can be assimilated to a general data mining problems
		- Data preparation...
- Machine Learning + all other things
	- user interface, system requirements(efficiency, scalability, privacy), serendipity
- Serendipity
	- unsought finding
	- don't recommend items the user already knows or would have found anyway
	- expand the user's taste into neighboring areas by improving the obvious
	- collaborative filtering can offer ..
- what works?
	- depends on the domain and the particular item
	- however, in the general case it has been demonstrated that the best isolated approach is CF
		- other approaches can be hybridized to improve the results in specific cases(cold start problem...)
	- ...

### Collaborative Filtering
- The CF ingredients
	- list of m users and a list of n items
	- each user has a list of items with associated opinion
		- explicit opinion, e.g. a rating score
		- something the rating is implicitly, e.g. purchase records or listen to tracks
	- active user for whom the CF prediction tasks is performed
	- metric for measuring similarity between users
	- method for selecting a subset of neighbors
	- method for predicting a rating for items not currently rated by the active user
- The Basic Steps
	- identify set of rating for target/active users...
- Pros
	- requires a minimal knowledge engineering effort
	- users and products are symbols without any internal structure or characteristics
	- produces good-enough results in most cases
- Cons
	- user feedback must be reliable
	- products must be standardized
	- assumes that prior behavior determines current behavior
- Personalized vs Non-Personalized CF
	- CF recommendation are personalized since the prediction is based on similar users
	- a non-personalized approach is by using the average of all users
	- MAE_{NP} = \sum_{i,j} abs(v_{ij} - v_j)/(?), where v_j is the average rating for item j
	- Netflix Prize's first conclusion: it is really extremely simple to produce "reasonable" recommendations, and extremely hard to improve
- **UB collaborative rating**
	- user u_i, product p_j
	- a matrix of user rating, v_ij is rating of user i to product j
	- predict for user i 
		- approach 1: combine the average of my neighbours
	- the weight of neighbors?
		- similarity can be computed by **Pearson correlation**
		- cos(u_i,u_j) = sum_k v_ik*v_kj/sqrt(sum_m v_ik^2 * sum_m v_kj^2)
	- Challenges of User-Based CF algorithms
		- sparsity, e.g. evaluation of large items sets, users purchases are under 1%
		- difficult to make predictions based on nearest neighbor algorithms, accuracy of recommendations may be poor
		- scalability, nearest neighbor require computation that grows with the number or users and the number of items
		- poor relationship among like minded but sparse-rating users
		- solution: usage of latent models 
- **Item-item collaborative filtering**
	- item similarity, e.g. cosine-based similarity
- The sparsity problem
	- typically; large product sets, user ratings for a small percentage of them
		e.g. in amazon, two user boy 100, and have 1 in common is of low probability
		e.g. in Netflix prize, rating data in a user/movie matrix is 8500M, and only 100M are not zero
	- methods of dimensionality reduction
		- matrix factorization
		- clustering
		- projection(PCA)
	- a web-based recommender can suffer serious scalability problems, the worst-case complexity can by O(m*n)
- Other approaches to CF
	- Model-based CF algorithms
		- use all the data I have to build a model, e.g, probabilistic, ...
	- Memory-based CF algorithms
		- use all the rating I have to do the prediction
		- the nearest neighbour
		
### SVD/MF
- reduce the item space to a lower space
	- X[n*m] = U[n*r]S[r*r]*[V[m*r]]'
		- X: m*n, m user, n items
		- U: n items, r factors
- using stochastic gradient descent to compute
- rating prediction	
	- baseline b_uv = \miu + b_u + b_v (user & item deviation from average)
	- predict rating as: r_uv = b + p_u'*q_v(p_u is user factor, q_v is item factor)
	- SVD++, asymmetric variations and implicit feedback...
	
### Restricted Boltzmann Machines(RBM)
- Introduction
	- each unit is a state that can be active or in-active
	- each input to a unit is associated a weight
	- the transfer function calculate a score based on the weighted sum of inputs
	- score is passed to the active .. to compute the probability of active
- Restricted the connectivity to simplify learning
- [Paper](http://www.cs.utoronto.ca/~hinton/absps/netflixICML.pdf)
- Activation probability is used to recommend items
- Note: current product is a combination for SVD++ and RBM, linear combination
	
### Clustering
- Idea
	- build group of similar users
	- compute the typical preferences of a cluster
- Pros
- Cons
	- assume user behave can be grouped in a cluster
- Locality-sensitive Hashing(LSH)
	- Method for grouping similar items in highly dimensional spaces
	- find a hashing function s.t. similar items are grouped in the same buckets
	- main application is nearest-neighbours	
		- hashing function is found iteratively by concatenating a random hashing functions
		- addresses one of the NN main concerns, performance
- Association Rules
	- Past perchases are transformed into relationship of common perchases e.g. customer buy A will also buy B
	- recommendations are constrained to some minimum level of confidence
	- Pros
		- fast to implement, execute
		- require little storage
	- Cons
		- not suitable if knowledge of preference change rapidly, e.g. click website?
- Classifiers
	- are general computation model trained using positive and negative examples
	- they may take into input: vector of item features, vector of user preferences, or the relationship among them
	- Pros
		- versatile
		- can be combined with other methods to improve the accuracy of recommendations
	- Cons
		- may overfit(regularization)
		- need a relevant training set
		
### Limitation of CF
- Cold start: New items need to get enough rating. There should be enough users in the system.
	- for a new user: recommend popular things 
	- for a new item: content-based approach
- Popularity Bias: it is hard to recommend something that really to someone's taste
	- usually will recommend popular items(items in the tail do not get much data)

### Content-based Recommendation
- Find similarity of items by analyzing the contents, e.g. meta data associated in items
	- e.g. recommend book or webpages, 
	- we have a description of the features of items
	- then we can build model, we have some users, some documents, some ratings(or click informaiton), then we trained the classifier based on the information
		- e.g. neurual network
	- Pros
		- no need for on other users
	- Cons
		- build model, overfit
- Contents usually described by words
- Cosine similarity
- TF-IDF(frequency/inverse document frequency)
- [Recommending new movies: even a few ratings are more valuable than metadata](http://dl.acm.org/citation.cfm?id=1639731)

### Comments
- In collaborative filtering, the feature engineering step is not required