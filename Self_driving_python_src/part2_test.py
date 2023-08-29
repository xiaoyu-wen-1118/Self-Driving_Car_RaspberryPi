import picar_4wd as fc
import numpy as np
import matplotlib.pyplot as plt
from measure_dist import *
from driving import *
from mapping import *
from my_detect import *
import cv2
from tflite_support.task import core
from tflite_support.task import processor
from tflite_support.task import vision
import utils
import argparse
import sys
import time

def driveTo(curr_loc, goal, map, direction):
    stop = False
    # Up: 0, Right: 1, Down: 2, Left: 3
    direction_list = ['Forward', 'Right', 'Backward', 'Left']
    turn_list = ['No turn', 'Turn Right', 'Turn over', 'Turn left']
    while curr_loc != goal:
        # Scan the environment and update the map
        print("Enter While loop.\n Curr loc: ", curr_loc, "; Direction:", direction_list[direction])
        grid = draw()
        for grid_y in range(len(grid)):
            for grid_x in range(len(grid[0])):
                # In grid, the car is at [100, 0]
                map_x = grid_x + curr_loc[0] - 100 
                map_y = grid_y + curr_loc[1]
                if map_x >= 0 and map_x < len(map[0]) and map_y >=0 and map_y < len(map):
                    if grid[grid_y][grid_x] == 1:
                        map[map_y][map_x] = 1

        # Find the path to goal
        came, cos = a_star_search(map, curr_loc, goal)
        path = []
        path.append(goal)
        tmp = goal
        while(tmp != curr_loc):
            tmp = came[tmp[0]][tmp[1]]
            path.append(tmp)
        path.reverse()
        print("Current path:")
        print(path)

        for i in range(1, min(6, len(path))): 
            # Arrive the goal or has run for 5*20 cm
            # Detect stop sign and stop for 5 seconds when detected.
            if not stop:
                stop = detectStop()
                if stop:
                    print("Stop Sign!")
                    fc.stop()
                    time.sleep(5)
                else:
                    print("Don't Stop")
                    
            next_loc = path[i]
            print("From", curr_loc, "To", next_loc)
            # Get the direction to go
            if next_loc[0] > curr_loc[0]:
                go_direction = 1
            elif next_loc[0] < curr_loc[0]:
                go_direction = 3
            elif next_loc[1] > curr_loc[1]:
                go_direction = 0
            elif next_loc[1] < curr_loc[1]:
                go_direction = 2

            # Get how much turns it need
            turn = (go_direction - direction) % 4
            print("Curr direction: ", direction_list[direction], "  Go direction:", direction_list[go_direction], ";", turn_list[turn])
            if turn == 0:
                move_forward20()
            elif turn == 1: 
                right90()
                move_forward20()
            elif turn == 2:
                right90()
                time.sleep(0.5)
                right90()
                move_forward20()
            elif turn == 3:
                left90()
                move_forward20()
            direction = go_direction
            curr_loc = next_loc

        if direction == 1:
            print("Turn left, back to forward direction.")
            left90()
        if direction == 2:
            print("Turn over, back to forward direction.")
            right90()
            time.sleep(0.5)
            right90()
        if direction == 3:
            print("Turn right, back to forward direction.")
            right90()
        direction = 0
            
if __name__ == "__main__":
    try:
        print("Start Part 2 test.")
        map = np.zeros((501, 301))
        # Only in map and grid, use y as the 1st index, x as the 2nd index
        # In all other 2D arrays, use x as the 1st index, y as the 2nd index
        curr_loc = [100, 0] 
        goal_1 = [100, 140] # The distance is 140 cm
        direction = 0
        driveTo(curr_loc, goal_1, map, direction)
        print("Arrive the first goal location.")
        time.sleep(5)
        curr_loc = goal_1
        goal_2 = [100, 260]
        driveTo(curr_loc, goal_2, map, direction)
        print("Arrive the second goal location.")
        # The map is saved as image
        plt.imshow(map, origin = 'lower')
        plt.savefig("map.png")

    finally:
        fc.stop()
