import random
import math

class point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_dist_from_origin(self):
        dist_from_origin = math.sqrt((self.x ** 2) + (self.y ** 2))
        return dist_from_origin
    
def for_loop():
    for i in range(5):
        point_x = random.random()
        point_y = random.random()
        coord = point(point_x, point_y)
        print("Sample " + str(i) + " is: ( " + str(point_x) + " , " + str(point_y) + " )")
        print("Distance from origin: " + str(coord.get_dist_from_origin()))

def million():
    count = 0
    for i in range(1000000):
        point_x = random.random()
        point_y = random.random()
        coord = point(point_x, point_y)
        place = coord.get_dist_from_origin()
        if place <= 1:
            count += 1
    estimated_pi = count/250000.00
    difference = math.pi - estimated_pi
    print(str(count) + " of the 1000000 are inside")
    print("actual pi is about " + str(math.pi))
    print("estimated pi is about " + str(estimated_pi))
    print("monte carlo simulation is off by " + str(difference))
        
for_loop()
million()
