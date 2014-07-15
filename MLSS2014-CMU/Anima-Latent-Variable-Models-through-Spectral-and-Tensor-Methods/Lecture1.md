Guaranteed and efficient learning through spectral methods
===========================================================
http://newport.eecs.uci.edu/anandkumar/MLSS.html


* Lecturer: Anima
* Recorded by: huangxin
* Date: 07/14/2014

### Application
- Clustering
- Topic modeling
	- document modeling
		- observed: words in document corpus
		- hidden: topics
		- goal: carry out document summarization
- Understanding Human Communities
	- Social Networks
		- Observed: network of social ties, e.g. friendships, co-authorships
		- Hidden: groups/communities of actors
- Recommender Systems
	- Observed: rating of users of various products, e.g. yelp reviews
	- Goal: predict new recommendations
	- Modeling: ...
- Feature learning
	- learn good features/representations for classification tasks. e.g. image and speech recognition
	- **Sparse** representations, low dimensional hidden structures
- Computational Biology
	- observed: gene expression levels
	- Goal: discover gene groups
	- Hidden variable: regulators controlling gene groups 

### Challenges in Learning
- How to model hidden effects?
	- Basic approach: mixtures/clusters
		- hidden variable h is catergorical
	- Advanced: probabilitistic models
- Challenge in learning
	- discover hidden structure in data: unsupervised learning
	- condition for identifiability
		- when can model be identified(given infinite computation and data)?
		- does identifiability also lead to tractable algorithm?
	- efficient learning of Latent Variable Models
		- Maximum likelihood is NP-hard
		- Practice: EM, Variational Bayes have no consistency guarantees
		- Efficient computational and sample complexities?

### Basic Spectral approach: principal component analysis(PCA)
- denoisying methods
- PCA on Guassian Mixtures
	- k Gaussians: each sample is x = Ah + z
	- h \in ...
- Learning through spectral clustering
	- Learning A through spectral clustering
		- project sample x onto span(A)
		- distance-based clustering( e.g. k-means)
		- a series of works, e.g. Vempala & Wang
	- Failure to cluster under large variance
	- How to learn the component means A(not just its span) without separation constraints?

### Beyond PCA: Spectral Methods on Tensors
- PCA is a spectral method on (covariance) matrices
- what if number of components is greater than observed dimensionality k>d?

### Higher order moments for Gaussian Mixtures
 

### Beyond correlations: higher order moments

		