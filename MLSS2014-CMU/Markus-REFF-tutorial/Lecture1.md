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

### Silos
- Silos are hard to build
	- each duplicates the same mechanism under the hood
	- in practice: Silos from pipelines
		- in each step, read from and ...
		
### REEF
- overview
	- resouces manager and DFS: cluster OS
	- REEF: stdlib
	- REEF can tell you that a machine crash, it depends on you how to deal with the fault
- design mechanism
	- Breath
		- mechanism over policy
	- Avoid Silos
		- recognize the need for different models, but allow them to be composed
	- Bridge the JVM/CLR/...divide
	
### REEF control flow

- Components
	- Yarn(): handles resouces management(security, quotas, proorities)
	- Per-job Drivers() request resources, coordinate computations and handle events: faults, preemption, etc
	- REEF Evaluators() hold hardware resources, allowing multiple tasks to use the same cached state
	
- Retaining evaluators
	- handover of pre-partitioned and parsed data vetween frameworks
	- iterative computations
	- iterative queries
- Centralized error handling
	- e.g. when not asked enough big container, then it may have faults, REEF can catch the fault and return the error message to...
	- task exceptions are thrown at the driver evaluator failure is reported to the driver
- Wake: Events + I/O
	- Event-based...
- REEF v.s. Tang
	- configuration is hard, errors often show up at running time only State of receiving process is unknown to the configuring process
	- *REEF's approach*: configuration as dependency injection configuration here is pure data-> early static and dynamic checks

### REEF Data Plane
- Fault-tolerance communication
- Group communication/Shuffle
- low-latency communication
	- low-latency between two nodes

### Conclusion
- Resource management is upon us
	- Failure and preemption
	- upwards elasticity
	- My idea: when running map reduce, and the prices fluctuate, how to use the machine in order to reduce cost?
- REEF provides a useful abstraction
	- natural events happens to the driver...

	
