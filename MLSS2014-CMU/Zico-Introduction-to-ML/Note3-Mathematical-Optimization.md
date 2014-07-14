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
	- Note
		- max substitue is convex
	
### Convex Optimization Problems
- Advantage
	- can be solved in polynomial time
	- all local solutions are global solutions
- Formal Definition	
	- minimize_x f(x), s.t. x \in C, where x in optimization variable, f is a convex function and feasible set C is convex set
	- constraints, the equality constraints are affine
- Convex Sets
	- if x and y are all in c, then the linear combination of x and y should also be in C
	- intervals, C = {x \in R^n: l <= x <=u} (elementary inequality)
	- the intersection of convex sets are also convex sets
- Convex functions
	- for any two points x and y in the curve, the linear combination of f(x) and f(y) is smaller than f(the same linear combination of x and y)
	- f is concave, if -f is convex
	- f is affline if f is convext and concave, must have form f(x) = a.T*x + b, a \in R^n, b \in R
- Testing for convexity
	- f''(x) >=0, the function must be "curve upwards" everywhere
	- [TODO] for vector-input functions, corresponding condition is that \delta^2_x f(x) >=0, where \delta^2_x f(x) is the Hessian of f
- Examples
	- a non-negative weighted sum of convex function is still convex function
	- composition of convex and affine function: if f(y) convex in y, f(Ax-b) is convex in x
- Theorem
	- for a convex optimizaiton problem, all locally optimal are also global optimal, can be proved by contradiction
	- assume x is local optimal, and assume there is an y that is global optimal where y!=x, then we can find z whose value is smaller than x, however z is within R distance from x, which contradicts with the local optimal with x

- **Quadratic programming**
	- Definition	
		- objective: minimize_x (x.T * Q * x + x.T*x)
		- subject to: 

### Nonconvex problems
- Definition
	- any f or g_i is not convex
	- any h_i is not affine

- Two solutions
	- local
	- global

- Local methods
	- given an initial point x_0, repeatedly search its nearby points until a(feasible) solution ~x that is better than all its nearby points
		- typically, some approximation approach
- Integer programming
	- definition: add integer constraints to the optimization variables

### Solving optimization problem
- Convex Problem(local optimal)
	- Gradient descent
		- gradient = 0 is for constraint optimization, but if has constraint, then gradient may not be 0 for global optimal
		- Example, quadratic function, Q should be positive define?
		- Non-smooth function, should use gradient descent
	- Newton's method
		- use root finding algorithm to find solution to (nonlinear) equation \delta_x f(x) = 0
		- x <- x - f(x)/f'(x)
		- multivariable generation for finding \delta_x f(x) = 0, x<- x - (\delta^2f(x))^-1 \delta_x f(x)
		- need loglog rounds, however, each round is expensive
- Constraint optimization
	- Projected gradient
		- Project function f: for any x, P(x) returns it to a feasible point
	- Barrier method
		- approximate problem via unconstrained optimization
		- minimize_x f(x) - t \sum^m_{i=1} log(-g_i(x))
		- as t->0, this approaches original problem
- Practically solving optimization problem
	- Matlab
		- CVX, TALMIP
	- Python
		- *cvxpy*
	- custom language
		- AMPL, GAMS
		
	



