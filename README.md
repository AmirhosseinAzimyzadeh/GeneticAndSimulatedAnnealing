# GeneticAndSimulatedAnnealing
In this repo, genetic and simulated annealing are used to optimize the Cross-in-Tray function <br>
more information about Cross-In-Tray function : [click here](https://www.sfu.ca/~ssurjano/crossit.html)<br>
![Alt Tex](https://www.sfu.ca/~ssurjano/crossit.png) <br>
![Alt Tex](https://www.sfu.ca/~ssurjano/crossit2.png)<br>
© pictures from SFU - ca
## Genetic Algorithm
Each individual contains two chromosomes (x and y)
x and y for the first-generation are created randomly
The cross-In-Tray function always returns a negative value so the fitness function for each individual is :
fitness(Ind) = value of(Ind)/ sum of all population values
## Simulated Annealing
