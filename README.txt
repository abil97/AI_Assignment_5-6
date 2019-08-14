Assingment 5. 15/10/18
======================================================

General notes:
======================================================

- This program constructs a maze for assignment 5, as well as loads one from file 
- There are 4 files in the archive: 
	maze.py - main file with generator
	node.py - file with class for room object
	input.txt - file where maze will be loaded from
	output.txt - file where created maze will be printed
- There are some additional files may appear in the process of compilation

- There are two ways of running the program: to construct the maze or load one from file

- A maze constructed using following parameters: N - total number of nodes, K - numer of border nodes, p - number of edges of normal nodes, k - number of edges of border nodes
	M - number of monsters, W - number of walls, G - number of gold, H - number of holes, T - number of teleportation gates, as well as parameters for spread and decay and clock cycles

- N should be > K and p should be > k, otherwise error will be returned

- There is algorithm that checks if it possible to consruct the maze with entered K, N, k, p. If it is not possible, error will be returned
======================================================

Running the program
======================================================

 1. There is a folder inside an archive - assignment5. It should be extracted in any directory
 2. In terminal, change the directory to assignment5
 3. In the terminal, type: python maze.py
 4. Next, you will be asked if you want to create a maze or load one from a file

 	1. To create a maze, type in the terminal: initMaze N K k p M W H G σ ω τ
		"initMaze" is case sensitive, M - capital letter. Parameters should be entered exactly in this order
		If it is impossible to construct a maze, an error will be output
		If input is incorrect, corresponding error will be provided

		
		If input is correct, requested number of cycles of maze will be output to the terminal and to the file output.txt
	2. To load the maze, type in terminal: loadMaze filename σ ω
		It is assumed that input is provided in the file input.txt, however, it could be provided in any new file that is inside assignment5 folder
		
		If input is correct, loaded maze with correspnding smell/wind will be output to terminal
=========================================================

Contact info:
=========================================================

Author: Abil' Kuatbayev
Email: abil.kuatbayev@nu.edu.kz
