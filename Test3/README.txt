Author - NIKHIL KUMAR YADAV
DATED - 12 NOV 2018

In the GA problem I have implemented algorithm with averaging fitness and with non dominating solution. The results are stored in the Images folder.

The answer (f1+f2+f3) should be around -8 as the tuple (-0.01,-0.01,-0.01,-0.01,-0.01) will give me f1 ~ 0, f2 ~ -5 and f3 can give me anywhere between (-3*sigma , 3*sigma) with high probability.

The graph are plotted as follows
N - PopSize is varied over 50, 100, 200
Cross over probability is varies over 50,60,70,80
Mutation is also varied accordingly

And this is done for 3 models i.e Basic GA, Diversity GA and Elitism GA.
Performance of random selection model is also plotted.

Results are as follows - 
	GA with Elitism converges faster than all.
	Then Basic GA and Diversity GA converge somewhat equally (Maybe due to randomness in the problem due to function 3).
	Vanilla implementation Random search performs the worst.

Code off all these models can be easily interchanged into one other.

Implementation details - 
	non dominant solution - 
		I choosed my x range to be -204 to 204 and then divided by 100 anytime I used it.
	with nds (best fitness value) - 
		I converted the integer and the decimal points to binary separately and then append the string.