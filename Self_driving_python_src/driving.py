import picar_4wd as fc
import time

def move_forward60():
    fc.left_front.set_power(7.6)
    fc.left_rear.set_power(8)
    fc.right_front.set_power(7.5)
    fc.right_rear.set_power(7.5)
    time.sleep(2.38)
    fc.stop()

def move_backward60():
    fc.left_front.set_power(-7.6)
    fc.left_rear.set_power(-8)
    fc.right_front.set_power(-7.5)
    fc.right_rear.set_power(-7)
    time.sleep(2.6)
    fc.stop()

def move_forward20():
    fc.left_front.set_power(7.6)
    fc.left_rear.set_power(8)
    fc.right_front.set_power(7.5)
    fc.right_rear.set_power(7.5)
    time.sleep(0.84)
    fc.stop()

def move_backward20():
    fc.left_front.set_power(-7.6)
    fc.left_rear.set_power(-8)
    fc.right_front.set_power(-7.5)
    fc.right_rear.set_power(-7)
    time.sleep(0.9)
    fc.stop()

def left90():
    fc.left_front.set_power(-10)
    fc.left_rear.set_power(-10)
    fc.right_front.set_power(10)
    fc.right_rear.set_power(10)
    time.sleep(1.68)
    fc.stop()

def right90():
    fc.left_front.set_power(10)
    fc.left_rear.set_power(10)
    fc.right_front.set_power(-10)
    fc.right_rear.set_power(-10)
    time.sleep(1.63)
    fc.stop()

def left45():
    fc.left_front.set_power(-10)
    fc.left_rear.set_power(-10)
    fc.right_front.set_power(10)
    fc.right_rear.set_power(10)
    time.sleep(0.825)
    fc.stop()

def right45():
    fc.left_front.set_power(10)
    fc.left_rear.set_power(10)
    fc.right_front.set_power(-10)
    fc.right_rear.set_power(-10)
    time.sleep(0.825)
    fc.stop()

def left10():
    fc.left_front.set_power(-10)
    fc.left_rear.set_power(-10)
    fc.right_front.set_power(10)
    fc.right_rear.set_power(10)
    time.sleep(0.19)
    fc.stop()

def right10():
    fc.left_front.set_power(10)
    fc.left_rear.set_power(10)
    fc.right_front.set_power(-10)
    fc.right_rear.set_power(-10)
    time.sleep(0.19)
    fc.stop()

if __name__ == "__main__":
   # move_forward60()
   # move_backward60()
    left90()
    #right90()
    #left45()
    #right45()
    move_forward20()
    left90()
    #right90()
    #move_backward20()
    #for i in range(9):
        #left10()
       #right10()
        #fc.stop()
        #time.sleep(0.5)
