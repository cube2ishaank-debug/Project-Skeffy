# Datasets
## Data Included
### Scrambles & 'Solutions'
The datasets include the shortest move sequence or scramble to reach every state, the inverse of which becomes the optimal solution for every skewb state and the state of the skewb at every scramble, i.e the color of each sticker for every possible skewb position apart from the solved state.
#### Datasets:
all_scrambles.txt (Lost in uploading, will be linked shortly) <br/>
[all_scramble_states.txt](https://huggingface.co/datasets/BansalBytes/PROJECT_SKEFFY/blob/main/all_scramble_states.txt)
### Training the Model
To train an AI Skewb Solver using this dataset, there are specefically 2 datasets that can be used as X and Y datasets to create an AI Skewb Solver:
<br/>
##### X Dataset: [all_scramble_states.txt](https://huggingface.co/datasets/BansalBytes/PROJECT_SKEFFY/blob/main/all_scramble_states.txt)

_This dataset has the state of a skewb in every scrambled position._
##### Y Dataset: [skewb_solution_set.csv](https://huggingface.co/datasets/BansalBytes/PROJECT_SKEFFY/blob/main/skewb_solution_set.csv)
<br/> 
_This dataset has the corresponding optimal next move for every state in the X dataset._

#### How the model would work

By using these X and Y databases, the model can learn to predict the direct next move for any skewb state. 
Therefore, the AI model trained using this data would output just the next move, and using the model multiple times after every move until solved allows for the AI to find a full solution.
## New databases that can be formed using these datasets

Using the X and Y databases, by performing the corresponding move for a X state, then finding the corresponding move for the new state until the skewb is solved, you can connect these moves to create a dataset with the optimal solution for each scrambled state.
