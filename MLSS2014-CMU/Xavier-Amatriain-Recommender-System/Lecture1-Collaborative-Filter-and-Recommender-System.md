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
- serendipity
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
	



### 