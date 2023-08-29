# Self-Driving_Car_RaspberryPi
## Topology:
The following figure shows the topology of the car. The figure was drawn using Fritzing. The Pi camera is directly connected to the Raspberry Pi 4B. The 4WD Hat is connected to the GPIO of Raspberry Pi 4B. The motors, ultrasonic sensor, servo, photo interrupter, gray scale sensor, Pi camera, and batteries are connected to the 4WD Hat.
![image](https://github.com/xiaoyu-wen-1118/Self-Driving_Car_RaspberryPi/assets/57936592/832e28db-54fa-40f1-977a-c433a61cca1f)

## Design Consideration
Firstly, the OS was installed on the Raspberry Pi. Then, the WiFi connection and remote access were configured for the Raspberry Pi. The car assembly was done by following the SunFounder’s instructions. Before the top and bottom plates were assembled, all the other parts were tested. The Pi camera was connected to the Raspberry Pi before the 4WD Hat was installed on the Raspberry Pi.
![image](https://github.com/xiaoyu-wen-1118/Self-Driving_Car_RaspberryPi/assets/57936592/802ebe1c-eed3-46fc-9b74-1a82ed2481b3)


## Naive Mapping
The mapping is done by detecting the distance in the angle between 54° and 126° in front of the car, which is stored in tmp = scan_list[3: 8]. The status 2, 1, and 0 indicate the distance is more than 20 cm, between 20 cm and 10 cm, less than 10 cm. In our test we found the ultrasonic sensor may not be sensitive enough. Thus, to avoid hitting obstacles, the critical distance is set to be 20 cm. When any 0 or 1 exists in the tmp, an obstacle is detected.

## Naive Self-driving:
When an obstacle is detected. The car will back up for 1 second. Then a random float point number t is generated between -1 and 1. If t is positive, the minimum value of t is set to be 0.25. Then the car will rotate right for t seconds and keep going forward until another obstacle is detected. If t is negative, the maximum value of t is set to be -0.25. Then the car will rotate left for t seconds and keep going forward until another obstacle is detected.

## Advanced Mapping
The distance is measured at each 5 degrees. The angle and measured distance are stored in a list. If the measured distance is too large or abnormal, the distance will be set as 200 which means very far from the car. A 2D array grid with a dimension of 101*201 is created as the surrounding map. It should be noted that when accessing the grid it should use grid[y][x], because in the map the horizontal axis is x, but in the 2D array the second index is for the horizontal direction. The locations of detected obstacles are calculated by using the trigonometry method. Occupied locations are marked as 1. Unoccupied locations are marked as 0. The points between adjacent points are filled using the fillPoints() function to generate a rough map. The car has its size, so clearance areas are added to all occupied locations using the addClearance() function. While running, the car will copy the information from the surrounding map to the whole map. In the surrounding map, the car is at [100, 0].

## Routing
The best route is calculated by the A* algorithm. The A* algorithm is similar to Dijkstra's algorithm. In the A* algorithm it examines the vertex n that has the lowest f(n) = g(n) + h(n), where g(n) is the exact cost from the start point to the vertex, h(n) is the heuristic cost from the vertex to the goal. To reduce ties, a penalty of 0.5 is added to the cost if a tie is added to the path.

## Full Self-driving
After obtaining a path. The car will first follow the path to go forward, turn left, turn right, or turn over. It will detect the “STOP” sign each time before moving. The car rescans its surrounding environment after it has run 5*20 cm. After scanning, the map is updated, and then a new path is calculated by using the A* algorithm. In the whole driving process, the current location and direction are updated every time the car does some actions. The full self-driving is implemented in the following code. 

## The map generated in the test:
![image](https://github.com/xiaoyu-wen-1118/Self-Driving_Car_RaspberryPi/assets/57936592/b74f0030-1799-46b2-880c-7eec148ae93a)

