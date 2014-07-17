Human Brain and Machine Learning
================================
* Lecturer: Tom Mitchell
* Recorded by: Huangxin
* Date: 07/16/2014

### Introduction
- classifiers trained to decode the stimulus word
	- e.g. for each "word", brain will have different stimulus
- question: are neural representation similar across people?
	- Yes
	- But how do we know the representation is the stimulus by word?
- Lessons from fMRI word classification
	- Neural representation similar across
		- people
		- language
		- word/picture
	- Easier to decode:
		- concrete nouns
		- emotion nouns
	- Harder to decode:
		- abstract nouns
		- verbs
		
### Model
- Predicted activation is sum of feature contributions
- canonical correlation analysis
	- corr(A,B) = 1/N * sum^N_{i=1} (A_i - ~A)/\sigma_a * (B_i - ~B)/\sigma_b
- Discovering shared semantic basis
	- use CCA to discover latent features across subjects(Rustandi et al. 2009)
	- train regression to predict them
	- e.g. 218 MTurk features(denoted as b(w）) -> 20 learned latent features(denoted as f(w))
	- f_i(w) = \sum_k b_k(w)*c_{ik}
- color
	- decodability of "grasping" features
	


	
	

