import picar_4wd as fc
def scan(step = 5):
    dist_list = []
    fc.get_distance_at(-90)
    time.sleep(0.5)
    for angle in range(-90, 91, step):
        dist_tmp = fc.get_distance_at(angle)
        if dist_tmp > 0 and dist_tmp < 150:
            print("Angle: ", angle, "Dist: ", dist_tmp)
            dist_list.append([angle, dist_tmp])
        else:
            print("Angle: ", angle, "Dist: ", dist_tmp)
            dist_list.append([angle, 200])
    return dist_list
if __name__ == "__main__":
    res = scan()
    for val in res:
        print(val[1])
