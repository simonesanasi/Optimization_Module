 Standalone Optimization Module (Python / Linear Programming)

This is a small project I built to put into practice some of the concepts I learned in my Operational Research (Ricerca Operativa) course.
It’s a simple prototype that applies linear programming to a real-world problem — deciding how to allocate a limited budget in the most efficient way.

-What It Does

The module takes a few “spending categories” and tries to find the best way to distribute a given budget among them.
The goal is to maximize a satisfaction score (basically how “good” each spending decision is) while respecting certain constraints like total budget limits or minimum savings.

In short:
	•	Objective: Maximize total satisfaction.
	•	Constraints: Keep spending within the total budget and meet minimum saving requirements.
	•	Output: The optimal allocation of funds.

-Why I Made It

During my course I realized most exercises were theoretical — so I wanted to create something more concrete.
This project was a way to see how linear programming can be used for actual decision-making problems, not just textbook examples.
It’s also a nice way to get some hands-on experience with Python + PuLP.

-How to Run It

You only need Python and PuLP to try it out.

Requirements
	•	Python 3.x
	•	PuLP (install via pip): " pip install pulp "

  -Run the test case: " python3 Optimization_Module.py "

- Notes:

The whole project is standalone and doesn’t need any external data or dependencies.
It’s a basic prototype, but it could easily be extended with a user interface or different optimization goals in the future.
