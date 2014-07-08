Adaptive Boosting(adaBoost)
===========================

### Files:
- **boost.py**: build decision stump
- **adaBoost.py**: build classifier
	- call boost.py to find best decision stump
	- computer weighted value(alpha) of each classifier
	- adjust weight of training samples gradually
- **horseColic.py**: use adaBoost to test whether a horse could be saved
	- compare the result to LogRegress which has 35% error rate
	- input: horseColicTraining2.txt(training file), horseColicTest2.txt(test file)
- **plotRoc.py**: plot ROC curve
