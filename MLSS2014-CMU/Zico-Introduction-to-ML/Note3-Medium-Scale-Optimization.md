Solving Optimization Problem
=============================

* Lecture: Ziko Kolter
* Note taken by Huangxin Wang
* Date: 07/11/2014

### Introduction to Mathematical optimization

- Search problems v.s. Mathematical programming
	- Search problems: discrete, finite, exponential
	- Mathematical programs: Continuous, Infinite, Polynomial(sometimes)

- Formal definition
	- minimize_x f(x), x is the optimization variable, f is an objective function
	- subject to g_i(x) <=0, g are (inequality) constraint functions
	- feasible region: {x: g_i(x) <=0, for any i=1..m}
	- x* is an optimal solution

- Other terminology
	- Numerical optimization, refer to the study of these problems
	
- Classification of optimization problems
	- Convex problems: including Semidefinite programming, Quadratic programming, Linear programming
	- Nonconvex problems: including Integer programming, 
	
### Applications
1. Least Squares
	- given x_i \in R^n, y_i \in R, i=1,...,m find \theta that optimizes
	- minimize_\theta sum^m_{i=1} (x_i.T * \theta - y_i)^2
2. Weber point
	- I have a bunch of point in n dimension space, find the point z that minimizes the sum of distances to the points 
	- minimize_z \sum^m_{i=1} * \sqrt(\sum^n_{j=1} (x^(i)_j - z_j)^2)
	- Special case, if it is two dimension, the optimal solution is the average
	- Possible extensions, like keeping z within some range l<=z<=u
	

