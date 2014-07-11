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
---	

### Applications
1. Least Squares
	- given x_i \in R^n, y_i \in R, i=1,...,m find \theta that optimizes
	- minimize_\theta sum^m_{i=1} (x_i.T * \theta - y_i)^2
2. Weber point
	- I have a bunch of point in n dimension space, find the point z that minimizes the sum of distances to the points 
	- minimize_z \sum^m_{i=1} * \sqrt(\sum^n_{j=1} (x^(i)_j - z_j)^2)
	- Special case, if it is two dimension, the optimal solution is the average
	- Possible extensions, like keeping z within some range l<=z<=u
3. Support vector machine
	- Formulation: minimize_\theta \sum^m_{i=1} \max{0, 1-y^(i)*x^(i).T * \theta} + \lambada \sum^n_{i=1} \theta^2
	- Challenge: but objective is non-differentiable, which makes is hard to get numeric optimal solution
		- therefore, we need to transform the problem to e.g soft margin SVM
		- move the non-differentiable part from objective function to constraints
	- Convert
		- Let \delta_i = \max{0, 1-y^(i)*x^(i).T * \theta}
		- then the objective function is minimize_\theta \sum^m_{i=1} \delta_i + \lambada \sum^n_{i=1} \theta^2
		- constraints: \delta_i >=0; \delta_i >= 1-y^(i)*x^(i).T * \theta
		- after conversion, the objective is differentiable
	- Scale
		- the cost will be n^2, where n is the dimension of the cost
		- optimization tool could solve it in times linear to n?
---
	
### Convex Optimization Problems
-Advantage
	- can be solved in polynomial time, and you can find the global optimal solution
- Formal Definition	
	- minimize_x f(x), s.t. x \in C, where x in optimization variable, f is a convex function and feasible set C is convex set
- Convex Sets
	- if x and y are all in c, then the linear combination of x and y should also be in C
	- intervals, C = {x \in R^n: l <= x <=u} (elementary inequality)
- 

