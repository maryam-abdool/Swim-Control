# Swim: A General-Purpose, High-Performing, and Efficient Activation Function for Locomotion Control Tasks

## Overview
We propose Swim, a general-purpose, high-performing, and efficient activation function for locomotion control tasks. Swim is tested on MuJuCo continuous control tasks using TD3. The code for TD3 in this repository is adapted from the original author’s implementation, which could be found here: https://github.com/sfujim/TD3

Swim is defined within the new() function in the TD3.py file (first function).

## Quick Start

Run `python3 main.py` in the main directory to start the training. Hyperparameters such as the seed and environment are defined in main.py and can be modified from the main.py itself or the terminal. 

The results of the training are learning curves formatted as NumPy arrays of 201 evaluations (201,), stored under /results. To visualize the learning curves, see the examples provided in vis.py and `run vis.py` in the main directory. 

Videos are also created after training ends and are stored in the main directory. The videos could represent the results of the training or testing depending on the seed passed to the make_video() function defined in main.py. We leave that modifiable. If the user also wishes to not overwrite previous videos, the count variable, defined above the make_video() function, could be changed to store a new video under a new name. Sample Videos of the Walker-2d environment using Swim are also provided in the main directory.

To run the efficiency tests described in the paper, uncomment the two print statements under the train() function in TD3.py 

The default environment is Walker-2d. Make sure to have MuJoCo and OpenAI gym setup as well as matplotlib and PyTorch installed.
