Lecture 2 (Part2)

Note record by Huangxin

-------------------------------------------------------------------------------------------------------------------
Topic: L0 Sampling

-Problem description
	-Main idea: random selection of distinct numbers
	-return i, F[i]!=0 with probability 1/({i|F{i>=0}})

-Application
	-Graph Sketch: for node i, let a_i be vector indexed by node pairs, a_i[i,j]=1 if j>i and a_i[i,j]=-1 if j<i
	-merge two sets, and tell what edge coming out of the sets(by sampling)
	
-Paper
	-Analyzing graph structure via linear measurement, SODA12

-------------------------------------------------------------------------------------------------------------------	
Topic: L2 approximation

-Main idea:
	- ||F||_2 = \sum_i F[i]^2
	-Least square approximation
	
-Paper	
	-Low rank approximation and regression in Input sparsity Time

-------------------------------------------------------------------------------------------------------------------	
Topic3: Nonstreaming Problems

-Problem Statement:
	-compute the discrete fourier transformation of signal of size n 
	-classical: o(n logn) time
	-recent result: o(k logn) time

	-Paper: Nearly Optimal Sparse Fourier Transform, STOC12
	
-Comments:
	-the outline algorithm is similar to ? (index problem)

-------------------------------------------------------------------------------------------------------------------

	