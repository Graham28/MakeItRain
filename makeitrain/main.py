#!/usr/bin/env python
import pygame
from drop import Drop
import random
import os, sys
from functions import view, view_new
import numpy as np
from numpy import loadtxt
random.seed(28)

def main():
    """ Main: Displays Results of Q-Learning """
    
    #Set max distance
    stop = 10000
    play = True
    
    #Load trained Q-table
    q_table = loadtxt('q_table_final.csv', delimiter=',')
    

    while play:

        #Initialize pygame and window
        pygame.init()
        win = pygame.display.set_mode((500,500))
        pygame.display.set_caption('Make It Rain')

        #Set variables of man
        x = 210
        y = 450
        width = 30
        height = 30
        vel = 5
        state_list = []
        
        #Set variable of drops
        vel_rain = 1
        drops = []
        rate = 70        

        #Set loop variables
        run = True
        count = 0
        reward = 0

        while run:
            #Check if window was closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    play = False

            #Generate new drop depending of the set rate
            if count%rate == 0:
                size = random.randint(5,20)
                new_drop = Drop(random.randint(0,490), 0, size, size, vel_rain)
                drops.append(new_drop)
                count += 1
            else:
                count += 1

            #View enviroment & choose best action based on current view state
            vision = view(x,y,width,drops)
            action = np.argmax(q_table[vision])

            #Take action if with bounderies
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
                    game_on = False
                    vel = 0
                    run = False
                    break

            #Clear window. Redraw man. Redraw drops. Update display
            win.fill((0,0,0))
            pygame.draw.rect(win, (255, 255, 255), (x,y,width,height))
            for drop in drops:
                pygame.draw.rect(win, (0, 0, 255), (drop.get_x(),drop.get_y(),drop.get_width(),drop.get_height()))
            pygame.display.update()

            #Increment Reward
            reward +=1

            #Stop game if it has reached finish
            if reward >= stop:
                run = False

        #Quit game and print reward    
        
        print('You scored: ' + str(reward))
    
    pygame.quit()

if __name__ == "__main__":
    main()