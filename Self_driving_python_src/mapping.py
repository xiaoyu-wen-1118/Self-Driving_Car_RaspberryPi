import numpy as np
from measure_dist import *
import matplotlib.pyplot as plt
import sys
from queue import PriorityQueue

def fillPoints(p1, p2, grid, point_list):
    # Fill all the points between these two points
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x_diff = x2-x1
    y_diff = y2-y1
    if x_diff == 0 and y_diff != 0:
        curr_x = x1
        y_step = int(y_diff/abs(y_diff))
        for i in range(abs(y_diff)):
            curr_y = int(y1 + i*y_step)
            grid[curr_y][curr_x] = 1
            point_list.append([curr_x, curr_y])
        return
    if y_diff == 0 and x_diff != 0:
        curr_y = y1
        x_step = int(x_diff/abs(x_diff))
        for i in range(abs(x_diff)):
            curr_x = int(x1 + i*x_step)
            grid[curr_y][curr_x] = 1
            point_list.append([curr_x, curr_y])
        return
    if x_diff == 0 and y_diff == 0:
        return 0
    
    slope = y_diff/x_diff
    if np.abs(y_diff) > np.abs(x_diff):
        y_step = int(y_diff/abs(y_diff))
        x_step = y_step/slope
        for i in range(abs(y_diff)):
            curr_y = int(y1 + i*y_step)
            curr_x = int(x1 + i*x_step)
            grid[curr_y][curr_x] = 1
            point_list.append([curr_x, curr_y])
    else:
        x_step = int(x_diff/abs(x_diff))
        y_step = x_step*slope
        for i in range(abs(x_diff)):
            curr_x = int(x1 + i*x_step)
            curr_y = int(y1 + i*y_step)
            grid[curr_y][curr_x] = 1
            point_list.append([curr_x, curr_y])

def addClearance(grid, point_list):
    # Add clearance to avoid collision
    clear_range = 3
    for point in point_list:
        for x in range(-clear_range, clear_range+1):
            for y in range(-clear_range, clear_range+1):
                newx = point[0]+x
                newy = point[1]+y
                newP = [newx, newy]
                if calDistance(point, newP)<=clear_range and newx>=0 and newx<len(grid[0]) and newy>=0 and newy<len(grid):
                    grid[newy][newx] = 1
                           
def calDistance(p1, p2):
    # Get the Distance between two points
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def heuristic(curr, start, goal):
    return ( np.abs(curr[0] - goal[0]) + np.abs(curr[1] - goal[1]))

def a_star_search(map, start, goal):
    frontier = PriorityQueue()
    frontier.put((0, start))
    cost = np.ones((len(map[0]), len(map))) * -1
    cost[start[0]][start[1]] = 0
    came_from = []
    for i in range(len(map[0])):
        came_from.append([])
    for row in came_from:
        for i in range(len(map)):
            row.append([])
    came_from[start[0]][start[1]] = start

    while not frontier.empty():
        curr_loc = frontier.get()[1]
        if curr_loc == goal:
            print("Path is found.")
            break
        neighbors = []
        for x,y in [[20, 0], [-20, 0], [0, 20], [0, -20]]:
            newx = curr_loc[0]+x
            newy = curr_loc[1]+y
            if newx >= 0 and newx < len(map[0]) and newy >= 0 and newy < len(map):
                OK = True
                if x != 0:
                    for dx in range(21):
                        tmp_x = curr_loc[0] + dx*int(x/20)
                        tmp_y = curr_loc[1]
                        if map[tmp_y][tmp_x] == 1:
                            OK = False
                            break
                else:
                    for dy in range(21):
                        tmp_x = curr_loc[0]
                        tmp_y = curr_loc[1] + dy*int(y/20)
                        if map[tmp_y][tmp_x] == 1:
                            OK = False
                            break
                if OK:
                    neighbors.append([newx, newy])
        for next in neighbors:
            new_cost = cost[curr_loc[0]][curr_loc[1]] + 1
            if curr_loc != start:
                older_loc = came_from[curr_loc[0]][curr_loc[1]]
                if older_loc[0] != next[0] and older_loc[1] != next[1]:
                    new_cost += 0.5
            if cost[next[0]][next[1]] == -1 or new_cost < cost[next[0]][next[1]] :
                cost[next[0]][next[1]] = new_cost
                priority = new_cost + heuristic(next, start, goal)
                frontier.put((priority, next))
                came_from[next[0]][next[1]] = curr_loc
    if frontier.empty():
        print("ERROR: Path is not found!")
    return came_from, cost

def draw():
    dist_list = scan(5)
    grid = np.zeros((101, 201))
    point_list = []
    for idx in range(len(dist_list)):
        angle = dist_list[idx][0]
        rad = np.radians(angle)
        dist = dist_list[idx][1]
        y = int(dist * np.cos(rad))
        x = 100 - int(dist * np.sin(rad))
        if x >= 0 and x <= 200 and y >= 0 and y <= 100:
            grid[y][x] = 1
            point_list.append([x,y])      

    for idx in range(1, len(point_list)):
        p1 = point_list[idx-1]
        p2 = point_list[idx]
        pDist = calDistance(p1, p2)
        if pDist <= 15:
            fillPoints(p1, p2, grid, point_list)
    addClearance(grid, point_list)
    return grid

if __name__ == "__main__":
    map = draw()
    plt.imshow(map, origin = 'lower')
    plt.savefig("drwaTest.png")
    plt.show()

