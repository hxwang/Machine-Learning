REEF Tutorial
=============

* Lecturer: Markus Weimer
* Recorded by: Huangxin
* Date: 07/14/2014

### Distributed Learning on Hadoop
- Drawback
	- Hadoop MR does not support iterations(30x slow down compares to others)
	- Hadoop MR does not match other forms of algorithm
- Solution: map only jobs
	- allocate a set of map tasks
	- instantiate learning algorithm
	- execute iterative algorithm until convergence
	- release mappers
