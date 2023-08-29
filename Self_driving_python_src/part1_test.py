import picar_4wd as fc
import time
import random
speed = 4

def main():
    while True:
        scan_list = fc.scan_step(20) # The boundary distance to determined status is set to be 20
        if not scan_list:
            continue

        tmp = scan_list[3:8] # tmp is used to detect obstacle in front of the car
        print(tmp)
        if 1 in tmp or 0 in tmp: # If 1 or 0 exist in tmp, an obstacle is detected
            fc.backward(speed) # Back up for 1 second
            time.sleep(1) 
            t = random.random() * 2 - 1 # A random value t is generated between -1 and 1
            if t >= 0:
                # When t is positive, turn right for t seconds
                t = max(0.25, t) # The minimum value of t is 0.25 seconds
                print("Rotate: ", t, "seconds")
                fc.turn_right(80)
                time.sleep(t)
            else:
                # When t is negative, turn left for |t| seconds
                t = min(-0.25, t) # The minimum value of |t| is 0.25 seconds
                print("Rotate: ", t, "seconds")
                fc.turn_left(80)
                time.sleep(-t)
            fc.forward(speed)
        else:
            fc.forward(speed)

if __name__ == "__main__":
    try: 
        main()
    finally: 
        fc.stop()

