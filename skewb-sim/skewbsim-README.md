# Skewb Sim

A Python simulation engine for skewbs that can track the state of a skewb and perform every turn on it!

## Usage

''' python
import skewbsim
skewbsim.R_turn(True) #For R'
skewbsim.R_tun(False) #For R
print(skewbsim.Skewb_state)
print(skewbsim.Front)
'''

## Data Format

#### Standardized data storage
Colors (Green, Blue, Red, Orange, White & Yellow) on a skewb will be stored as
1 = Green
2 = Blue
3 = Red
4 = Orange
5 = White
6 = Yellow
Number of faces and pieces on each face: 6 faces: 5 pieces on each face
Each face will have pieces stored in the order: [Top left corner, Top right corner, Bottom right corner, Bottom left corner, Center]
Following SPEFFZ lettering scheme used in blindfolded solving
List format = [Front,Back,Right,Left,Top,Bottom]
