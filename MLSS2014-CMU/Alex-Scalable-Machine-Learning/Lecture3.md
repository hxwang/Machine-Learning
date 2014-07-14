Modeling stuff-Clusters

* Lecturer: 
* Record by Huangxin
* Date: 07/14/2014

### Hierarchy of Clusters
- Examples
	- e.g. dog and cat have the same parent in the hierarchy
- Factorial representations
	- e.g. one instances may have several labels?
- Hierarchical factorial representations
	- Hierarchical Dirichlet process
		- Given hierarchy of objects
		- DP on children inherit from parent
	- Nested Chinese Restaurant Process
		- predefined the growth of the structure
		- (1) ...
		- (2) ...
	- Pachinko allocation
- Variable resolution models
	- users have different levels of detail for preferences
	- documents have different topics & levels of detail
	- want tree distribution per object. Sharing of strength between different trees
	- nested hierarchical Dirichlet process
	- nested Chinese restaurant franchise
- Generative process
	- for each documents, for each word, select a path in doc, if new in document, then select from global
	- if new in global, then add new path
	- main idea: ensure global is a superset

	
	
	