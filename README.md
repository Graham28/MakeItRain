# MakeItRain
Learning to dodge rain drops in PYGAME using Q-LEARNING

![Image description](#)

White cube learns to dodge blue rain drops(also cubes) using Q-Learning.

Cube "views" the world based on when rain drops or borders come close to it's sides.

It uses this "vision" to decide if its in one of 64 different states.

Q-learning is used with variable learning rate based on performance, to update the optimal action for the states the occured in each run of the game.

q_table_final.csv contains already trained q-table which can be seen by runnin main.py.
