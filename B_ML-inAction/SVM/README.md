Support Vector Machines(SVM)
===========================

#### Files
- SMO.py: implement a simple version of Sequential Minimal Optimization(SMO)
	- iterate all alpha, for each alpha, randomly choose the other alpha to pair with it and optimize the pair.
	- input: testSet.txt 
	
- plattSMO.py: improve version of SMP
	- instead of randomly choose the other alpha to pair, it finds the optimal alpha
	- interchangeably uses two approaches to choose alpha, one is iterating all alpha, the other is choosing the non-bounds alpha
	- input: testSet.txt

- kernel.py: apply radial basis function to SMO
	- using radial basis function for mapping the data from one space to the other.
	- input: testSetRBF.txt(training set), testSetRBF2.txt(test set)
	
- recogDigits.py: an application of SVM(using kernel function), used to classify handwriting digits number(only digit 0 and 9 are included in this example)
	- input: digits/trainingDigits(training file set), digits/testDigits(test file set)

- testSet.txt: a set of nodes which have two types of labels
- digits.7zip: a set of files contain handwriting information of digits 0 and 9

- Note: the current implemented SVM only supports two label classification, modification is required to support classifying of more labels. 