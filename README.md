# CS455FinalProject
IDFS Algorithm to solve a Rubiks Cube


This program will find the solution for an original 3x3 Rubik's cube using an Iterative Depth First Search Algorithm

Initialization of the Rubiks Cube and all of its states will be done through a 9x12 numpy array

# Requirements
Numpy

# RubiksCube.py Methods
  # PrintCube
    Simply prints the input state of the Rubiks Cube in the format as if it were an open box
                        _ _ _ W W W _ _ _ _ _ _
                        _ _ _ W W W _ _ _ _ _ _
                        _ _ _ W W W _ _ _ _ _ _
                        O O O G G G R R R B B B
                        O O O G G G R R R B B B
                        O O O G G G R R R B B B
                        _ _ _ Y Y Y _ _ _ _ _ _
                        _ _ _ Y Y Y _ _ _ _ _ _
                        _ _ _ Y Y Y _ _ _ _ _ _
                        
   # Rotations
  Contains every turn needed for the Rubiks cube except for cube rotations and middle slices (i.e. X, M, etc.)
    
   # Scramble
  Takes an input of the maximum number that will be used in a for loop. Will randomly call a turn for the call until the for loop ends
    
# Solve.py Methods
This is what will run the entire program

  # Class State
  Every Node will be a State that has its own numpy array, depth it's located in, and its parent that it belongs to
  
  # SovledCube
  Is used to see if the current node that is being looked at happens to be the solved state
  If it is solved, then the IDFS loop will end and then statistics will be printed on console
  
  # ChildIsInParent
  Is used to see if the current node that is being looked at happens to be the same as its parent
  If the child is the same, then it will not be appended to the frontier list
  
  # ChildIsInFrontier
  Is used to see if the current node that is being looked at happens to be the same as one in the frontier list
  If the child is the same, then it will not be appended to the frontier list
  
  # IDFSAlgorithm
  The main loop the will run an the IDFS Algorithm using an intial scrambled Rubiks Cube
  Once the loop ends, statistics that pertain to the depth of the solution, time taken to find the solution, and number of nodes 
  generated will be printed on the console

  #############################################
  
  Here a Rubik's cube is initally created with a solved state and then scrambled with 5 turns (Can be changed by editing the integer       parameter)
  
  The scrambled state is printed which in turn, starts the timer 
  
  IDFSAlgorithm is called with the scrambled state as an input
  
  Once the loop within IDFSAlgorithm ends, the timer ends and is printed
