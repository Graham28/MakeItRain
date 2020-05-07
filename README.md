# MakeItRain
Learning to dodge rain drops in PYGAME using Q-LEARNING

<div style="width:260px;max-width:100%;"><div style="height:0;padding-bottom:106.92%;position:relative;"><iframe width="260" height="278" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameBorder="0" src="https://imgflip.com/embed/40h1fp"></iframe></div><p><a href="https://imgflip.com/gif/40h1fp">via Imgflip</a></p></div>

White cube learns to dodge blue rain drops(also cubes) using Q-Learning.

Cube "views" the world based on when rain drops or borders come close to it's sides.

It uses this "vision" to decide if its in one of 64 different states.

Q-learning is used with variable learning rate based on performance, to update the optimal action for the states the occured in each run of the game.

q_table_final.csv contains already trained q-table which can be seen by runnin main.py.
