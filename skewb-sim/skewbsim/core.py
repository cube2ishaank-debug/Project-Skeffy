# **Simulate Skewb**

##Initializing cube state

### Creating Fundamental Storage Variables

#Standard Color Storage
#1 = Green
#2 = Blue
#3 = Red
#4 = Orange
#5 = White
#6 = Yellow
Skewb_state=[] #This will store all the faces of the cubes as multiple lists in this format: [Front,Back,Right,Left,Top,Bottom]
#################
Front=[]
Back=[]
Right=[]
Left=[]
Top=[]
Bottom=[]
#These lists represent each face of the skewb.

###  Initializing skewb in a solved state

#Standard Piece Storage: [topLEFTcorner,topRIGHTcorner,bottomRIGHTcorner,bottomLEFTcorner,center]
#The cube state will be green-front, white-top as the WCA Standards and will have the standard BOGR color scheme.
Front=[1,1,1,1,1]
Back=[2,2,2,2,2]
Right=[3,3,3,3,3]
Left=[4,4,4,4,4]
Top=[5,5,5,5,5]
Bottom=[6,6,6,6,6]
#The list of colors of each pieces has been put in the solved state.

Skewb_state=[Front,Back,Right,Left,Top,Bottom]
#Now, the variable storing the overall state of the cube has been inputted and has been put in solved state (Green Front, White Top)

## Creating Turning Mechanisms

### Creating turning variables

#These variables will store the new state of the cube before updating it
front_prime=[]
back_prime=[]
right_prime=[]
left_prime=[]
top_prime=[]
bottom_prime=[]
repeat=0 #This variable will be store how many times a turn should be done
#Repeat=1 Normal Turn
#Repeat=2 Prime Turn

###Defining basic update functions

def update_state():
  global front_prime, back_prime, right_prime,left_prime,top_prime,bottom_prime, Front,Back,Right,Left,Top,Bottom,Skewb_state
  #This function will be used to update the state in the end of every turn
  Front = front_prime[:]
  Back = back_prime[:]
  Right = right_prime[:]
  Left = left_prime[:]
  Top = top_prime[:]
  Bottom = bottom_prime[:]
  Skewb_state=[Front,Back,Right,Left,Top,Bottom]
def clear_turn_var():
  global front_prime, back_prime, right_prime,left_prime,top_prime,bottom_prime, Front,Back,Right,Left,Top,Bottom,Skewb_state
  #The variables storing the new state of the cube will be cleared before starting any turn
  front_prime=[]
  back_prime=[]
  right_prime=[]
  left_prime=[]
  top_prime=[]
  bottom_prime=[]
import copy
def load_state():
  global Front, Back, Right, Left, Top, Bottom, Skewb_state
  Front=Skewb_state[0]
  Back=Skewb_state[1]
  Right=Skewb_state[2]
  Left=Skewb_state[3]
  Top=Skewb_state[4]
  Bottom=Skewb_state[5]

### Defining turning functions

#### R & R' Turns

# Like WCA scrambling notation, turning in skewb will be stored as R, U, L & B moves with prime moves possible
#Actual turning functions will be defined now
def R_turn(Prime=False):

  global front_prime, back_prime, right_prime,left_prime,top_prime,bottom_prime, Front,Back,Right,Left,Top,Bottom,Skewb_state
  #Globalizing all of these variables allows them to be updated across the code using this function
  ####
  #This is a function that can be used further in the code to perform a R move on a skewb
  #Prime will be a true/false bolean variable that will tell the function whether the move should be R or R'
  ####
  clear_turn_var()
  #This resets the required variables
  if Prime:
    repeat=2
    #If a prime move is requested, a R move will be done twice
  else:
    repeat=1
    #If a prime move is not requested, a R move will only be done once
  a=0
  while a < repeat:
    #This will do the R move 'repeat' number of times
    front_prime=[Front[0],Front[1],Left[3],Front[3],Front[4]]
    #Front face variable has been changed
    back_prime=[Right[3],Back[1],Right[1],Right[2],Right[4]]
    #Back face variable has been changed
    right_prime=[Right[0],Bottom[1],Bottom[2],Bottom[3],Bottom[4]]
    #Right face variable has been changed
    left_prime=[Left[0],Left[1],Left[2],Top[1],Left[4]]
    #Left face variable has been changed
    top_prime=[Top[0],Front[2],Top[2],Top[3],Top[4]]
    #Top face variable has been changed
    bottom_prime=[Bottom[0],Back[2],Back[3],Back[0],Back[4]]
    #Bottom face variable has been changed
    update_state()
    #The cube has been updated
    #MOVE DONE
    a+=1

#### L & L' Turns

def L_turn(Prime=False):

  global front_prime, back_prime, right_prime,left_prime,top_prime,bottom_prime, Front,Back,Right,Left,Top,Bottom,Skewb_state
  #Globalizing all of these variables allows them to be updated across the code using this function
  ####
  #This is a function that can be used further in the code to perform a L move on a skewb
  #Prime will be a true/false bolean variable that will tell the function whether the move should be L or L'
  ####
  clear_turn_var()
  #This resets the required variables
  if Prime:
    repeat=2
    #If a prime move is requested, a L move will be done twice
  else:
    repeat=1
    #If a prime move is not requested, a L move will only be done once
  a=0
  while a < repeat:
    #This will do the L move 'repeat' number of times
    front_prime=[Left[3],Front[1],Left[1],Left[2],Left[4]]
    #Front face variable has been changed
    back_prime=[Back[0],Back[1],Right[3],Back[3],Back[4]]
    #Back face variable has been changed
    right_prime=[Right[0],Right[1],Right[2],Top[3],Right[4]]
    #Right face variable has been changed
    left_prime=[Left[0],Bottom[3],Bottom[0],Bottom[1],Bottom[4]]
    #Left face variable has been changed
    top_prime=[Top[0],Top[1],Top[2],Back[2],Top[4]]
    #Top face variable has been changed
    bottom_prime=[Front[3],Front[0],Bottom[2],Front[2],Front[4]]
    #Bottom face variable has been changed
    update_state()
    #The cube has been updated
    #MOVE DONE
    a+=1

#### U & U' Turns

def U_turn(Prime=False):

  global front_prime, back_prime, right_prime,left_prime,top_prime,bottom_prime, Front,Back,Right,Left,Top,Bottom,Skewb_state
  #Globalizing all of these variables allows them to be updated across the code using this function
  ####
  #This is a function that can be used further in the code to perform a U move on a skewb
  #Prime will be a true/false bolean variable that will tell the function whether the move should be U or U'
  ####
  clear_turn_var()
  #This resets the required variables
  if Prime:
    repeat=2
    #If a prime move is requested, a U move will be done twice
  else:
    repeat=1
    #If a prime move is not requested, a U move will only be done once
  a=0
  while a < repeat:
    #This will do the L move 'repeat' number of times
    front_prime=[Right[1],Front[1],Front[2],Front[3],Front[4]]
    #Front face variable has been changed
    back_prime=[Left[3],Left[0],Left[1],Back[3],Left[4]]
    #Back face variable has been changed
    right_prime=[Right[0],Bottom[3],Right[2],Right[3],Right[4]]
    #Right face variable has been changed
    left_prime=[Top[0],Top[1],Left[2],Top[3],Top[4]]
    #Left face variable has been changed
    top_prime=[Back[1],Back[2],Top[2],Back[0],Back[4]]
    #Top face variable has been changed
    bottom_prime=[Bottom[0],Bottom[1],Bottom[2],Front[0],Bottom[4]]
    #Bottom face variable has been changed
    update_state()
    #The cube has been updated
    #MOVE DONE
    a+=1

#### B & B' Turns

def B_turn(Prime=False):

  global front_prime, back_prime, right_prime,left_prime,top_prime,bottom_prime, Front,Back,Right,Left,Top,Bottom,Skewb_state
  #Globalizing all of these variables allows them to be updated across the code using this function
  ####
  #This is a function that can be used further in the code to perform a B move on a skewb
  #Prime will be a true/false bolean variable that will tell the function whether the move should be B or B'
  ####
  clear_turn_var()
  #This resets the required variables
  if Prime:
    repeat=2
    #If a prime move is requested, a B move will be done twice
  else:
    repeat=1
    #If a prime move is not requested, a B move will only be done once
  a=0
  while a < repeat:
    #This will do the L move 'repeat' number of times
    front_prime=[Front[0],Front[1],Front[2],Top[0],Front[4]]
    #Front face variable has been changed
    back_prime=[Back[0],Bottom[2],Bottom[3],Bottom[0],Bottom[4]]
    #Back face variable has been changed
    right_prime=[Right[0],Right[1],Front[3],Right[3],Right[4]]
    #Right face variable has been changed
    left_prime=[Back[3],Left[1],Back[1],Back[2],Back[4]]
    #Left face variable has been changed
    top_prime=[Right[2],Top[1],Top[2],Top[3],Top[4]]
    #Top face variable has been changed
    bottom_prime=[Left[0],Bottom[1],Left[2],Left[3],Left[4]]
    #Bottom face variable has been changed
    update_state()
    #The cube has been updated
    #MOVE DONE
    a+=1