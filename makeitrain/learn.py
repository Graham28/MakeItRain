#!/usr/bin/env python
import pygame
from drop import Drop
import random
import os, sys
from functions import view, view_new
import numpy as np
from numpy import asarray
from numpy import savetxt
random.seed(31)

def learn():

    #Initialise learning variables & Q-table
    learning_rate = 0.1
    DISCOUNT = 0.9
    EPISODES = 75
    q_table = np.random.uniform(low = 4000, high = 5000, size =(64, 3))

    #Set max distance & reward sum, used to find average reward
    stop = 5000
    reward_sum = 0

    for i in range(EPISODES):
        #Remove display for training, initialise pygame
        os.environ['SDL_VIDEODRIVER'] = 'dummy'
        pygame.init()
        win = pygame.display.set_mode((500,500))
        pygame.display.set_caption('Make It Rain')

        #Initialise variables of man
        x = 210
        y = 450
        width = 30
        height = 30
        vel = 5

        #Initialise variables of drops
        rate = 100
        vel_rain = 1
        count = 0
        drops = []

        #Q-learning loop variables
        reward = 0
        state_list = []

        run = True

        while run:
            #Check to see if window has been closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            #Generate rain drops
            if count%rate == 0:
                size = random.randint(5,20)
                new_drop = Drop(random.randint(0,490), 0, size, size, vel_rain)
                drops.append(new_drop)
                count += 1
                if rate > 75:
                    rate -= 1
            else:
                count += 1

            #View enviroment & choose best action based on current view state & Q-table values
            vision = view(x,y,width,drops)
            action = np.argmax(q_table[vision])

            #Set list of states ordered by the last time they were present
            if vision not in state_list:
                state_list.insert(0,vision)
            else:
                state_list.remove(vision)
                state_list.insert(0,vision)

            #Take action
            if action == 0 and x > 0:
                x -= vel
            if action == 1 and x <460:
                x += vel

            #Code for human play
            """
            pygame.time.delay(5)
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and x > 0:
                x -= vel
            if keys[pygame.K_RIGHT] and x <470:
                x += vel
            if keys[pygame.K_UP] and y > 0:
                y -= vel
            if keys[pygame.K_DOWN] and y < 460:
                y += vel

            """
            
            #Check for collision between man and rain drops
            for drop in drops:
                drop.fall()
                if (x + width >= drop.get_x() and x <= drop.get_x() + drop.get_width()) and (y + height >= drop.get_y() and y <= drop.get_y() + drop.get_height()):
                    for drop_stop in drops:
                        drop_stop.set_velocity(0)
                    vel = 0
                    run = False
                    break

            #Clear window. Redraw man. Redraw drops. Update display
            win.fill((0,0,0))
            pygame.draw.rect(win, (255, 255, 255), (x,y,width,height))
            for drop in drops:
                pygame.draw.rect(win, (0, 0, 255), (drop.get_x(),drop.get_y(),drop.get_width(),drop.get_height()))
            pygame.display.update()

            #Increment reward
            reward +=1

            #Stop game if end has been reached
            if reward >= stop:
                run = False
            
        #pygame.quit()

        #discount variable
        this_discount = 1

        #Loop through states of previous game, update q-table based on reward of previous game
        for state in state_list:
            q_table[state][np.argmax(q_table[state])] = (1-(learning_rate*this_discount))*(q_table[state][np.argmax(q_table[state])])+((learning_rate*this_discount)*reward)

            #Decrement discount
            this_discount = this_discount*DISCOUNT
        
        #Change learning rate based on average reward over 50 games
        if i%50==49:

          print("Average reward: " + str(reward_sum/50))

          if (reward_sum/50)>2500 and (reward_sum/50) <= 3250:
            learning_rate = 0.08
          elif (reward_sum/50)>3250 and (reward_sum/50) <= 4000:
            learning_rate = 0.04
          elif (reward_sum/50)>4000 and (reward_sum/50) <= 4500:
            learning_rate = 0.03
          elif (reward_sum/50) > 4500:
            learning_rate = 0.02
            stop += 1000
          elif (reward_sum/50) < 2500 and (reward_sum/50) >= 2000:
            learning_rate = 0.1
          elif (reward_sum/50) < 2000 and (reward_sum/50) >= 1500:
            learning_rate = 0.15
          elif (reward_sum/50) < 1500:
            learning_rate = 0.2
          
          print("New learning rate: " + str(learning_rate))

          reward_sum = 0
          reward_sum+=reward
        else:
          reward_sum += reward

    #Export Q-table to CSV file
    q_table_final = asarray(q_table)
    savetxt('q_table_new.csv', q_table_final, delimiter=',')

#Run learn
learn()