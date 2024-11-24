#**********************************************claasss ********************
#we are given 2D coordinates of following points (0,1), (2,4), (3,6), and (7,7).
#diatance
# p1 = (3,4)
# p2 = (7,7)
# p3 =(3,4)
# p4 =(7,7)

#OR******
import math
p1 = {"x" :0 , "y":1 }
p2 = {"x" :2 , "y":4 }
p3 = {"x" :3 , "y":6 }
p4 = {"x" :7 , "y":7 }
p5 = {"x" :3 , "y":4 }

def distance(p4,p5):
    
    # x1 = p1[0]
    # x2 = p2[0]
    # y1 = p1[1]
    # y2 = p2[1]
    
    x1 = p1["x"]
    x2 = p2["x"]
    y1 = p1["y"]
    y2 = p2["y"]
    d = (((x2 -x1)**2) +((y2-y1)**2))**(1/2)
    return d
print(distance(p1,p2))


