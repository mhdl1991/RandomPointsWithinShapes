import math
from random import random as rand #smaller name

def random_point_in_circle(c, r):
    """generates a random point (x,y coordinates) that lies within a circle at center c and radius r"""
    x,y = c
    rand_th = rand() * (2 * math.pi) #random angle
    rand_x, rand_y = x + (math.cos(rand_th) * r), y + (math.sin(rand_th) * r)
    
    return (rand_x, rand_y)
    
def random_point_in_rect(x1,y1,x2,y2):
    """generates a random point (x,y coordinates) that lies within a rectangle defined by a two opposing corners (x1,y1) and (x2,y2)"""
    dx, dy = (x2 - x1), (y2 - y1)
    rand_x, rand_y = x1 + (dx * rand()), y1 + (dy * rand())
    
    return (rand_x, rand_y)
    
def random_point_in_tri(*list_points):
    """generates a random point that lies within a triangle defined by three x,y coordinates, with the first point in list treated as a 'corner' vertex"""
    #Some inspiration taken from Wolfram MathWorld
    if len(list_points) is not 3:
        print("improper number of points in the list")
        return None #not sure how else to handle this right now
        
    x0,y0 = list_points[0] #this will be our "corner" vertex and treated as 0,0
    x1,y1 = list_points[1]
    x2,y2 = list_points[2]
    
    dx1, dy1 = x1-x0, y1-y0 #distances of each of the vertexes from the "corner" vertex
    dx2, dy2 = x2-x0, y2-y0
    
    #The method we're using would technically produce a random point in a parallelogram that is comprised of two copies of the original triangle
    #we model this parallelogram as a scaled version of the unit square (0,0,1,1)
    #(rand_x,rand_y) will be a point within this unit square
    #we need to make sure it stays within HALF of said unit square
    
    _x, _y = 0,0
    while True:
        _x, _y = rand(), rand()
        if _x + _y <= 1: break
        
    rand_x, rand_y = x0 + (dx1 * _x) + (dx2 * _x), y0 + (dy1 * _y) + (dy2 * _y)
    
    return (rand_x, rand_y)
