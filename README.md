# Project 3:Density Functional Theory and Machine Learning
## MSE 215: Introduction to Computational Materials Science, Fall 2019 
## University of California, Berkeley
### Instructor: Matthew Sherburne
### Graduate Student Instructor: John Dagdelen

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mse215/project3.git/master)

<h> <span style="color:red"><b>NOTICE TO BINDER USERS: YOUR NOTEBOOK PROGRESS WILL NOT BE SAVED IF YOU CLOSE THIS WINDOW OR LEAVE IT INACTIVE FOR TOO LONG.</b></span> </h>
      
<h> <span style="color:red"><b>PLEASE DOWNLOAD YOUR NOTEBOOKS AND FILES REGULARLY OR DOWNLOAD THIS REPO AND RUN OFFLINE ON YOUR MACHINE. See "[running_offline.md](running_offline.md)" for more info.</b> </span></h>


## Introduction

In this project, you are going to be using VASP (Vienna Ab Initio Simulation Package, https://www.vasp.at) to study the pressure driven structural transition in Si. At standard temperature and pressure conditions the ground state of Si is the diamond cubic structure. The diamond cubic structure is a face center cubic (FCC) lattice with a two-atom basis. At elevated pressures Si is known to have a structural phase transition to the β-Sn structure at a pressure of 15.2 GPa. Both structures are shown below.

<img src="static/structures.png" alt="diamond cubic Si and beta-Sn Si" width="500"/>

The figure of the diamond cubic structure is actually shown as a body centered tetragonal structure, hopefully helping you see the similarity between the two structures. (It is always possible to represent the FCC & BCC lattices as a body-centered tetragonal lattice.) This representation also allows one to study the transformation pathway between the phases. Another example of a transformation is the Bain transformation caused by strain that takes BCC to FCC in iron. Here it is possible to obtain both the diamond cubic phase and the β-Sn structures of Si merely by changing the ratio of c/a. 

We are going to use VASP to predict the hydrostatic pressure at which Si transforms from the diamond-cubic structure to the β-Sn structure. The procedure is straightforward. You will compute the energy as a function of volume for the two crystal structures and then fit the energy vs. volume curves to an equation of state. You can then determine the transition pressure using standard thermodynamic arguments. 

## Problem Walkthroughs
The notebooks in this repository will walk you through typical workflows that computational materials researchers today would use to solve these problems today. A lot of the details of running DFT calculations have been abstracted away by software in recent years, which has helped make DFT more accessible, faster to use, and robust. We will be using these tools in this project to give you a taste (and some practical training) on how DFT is done today. 

However, these abstraction layers can hide some important aspects of DFT that you should be aware of. With this in mind, we will also be asking you to prepare some input files by hand so you have a chance to see these details up close. 

Feel free to complete this lab however you would like, but we highly recommend following the jupyter notebooks in this repo and using python to perform the analyses.

## Project 2 Grading: 
```
Format (this is a professional report)		10pts
Explain Calculation/Introduction		10pts
Output/Input files				10pts

Calculations (and explanation): 
	DC: (Just showing plots is not sufficient)
	Energy convergence			5pts
	Kpts convergence			5pts
	Energy volume curve			10pts
	Explain 				5pts

	Beta-Sn:
	Energy convergence			5pts
	Kpts convergence			5pts
	Energy volume curve			10pts
	Explain					5pts

What is the pressure for transformation		5pts
Compare to experimental value			5pts
Explanation					10pts 
```
