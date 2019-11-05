import math
from random import random as rand #shorter name

def random_point_on_line(x1,y1,x2,y2):
    """generates a random point x,y between the points x1,y1 and x2,y2 using a Lerp method"""
    u = rand()
    rand_x = (u * x1) + ((1-u) * x2)
    rand_y = (u * y1) + ((1-u) * y2)
    return (rand_x, rand_y)
    

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
        return (0,0) #not sure how else to handle this right now
        
    x0,y0 = list_points[0] #this will be our "corner" vertex and treated as 0,0
    x1,y1 = list_points[1]
    x2,y2 = list_points[2]
    
    ux, uy = x1-x0, y1-y0 #distances of each of the vertexes from the "corner" vertex
    vx, vy = x2-x0, y2-y0
    
    #The method we're using would technically produce a random point in a parallelogram that is comprised of two copies of the original triangle
    #we model this parallelogram as a scaled version of the unit square (0,0,1,1)
    #(rand_x,rand_y) will be a point within this unit square
    #we need to make sure it stays within HALF of said unit square
    
    #the total of _x and _y should not be greater than 1
    _u, _v = 0,0
    #This method will likely be slow
    #find a better method
    while True:
        _u, _v = rand(), rand()
        if _u + _v <= 1: break
    
    #This method is worse, it causes the points to "cluster" near the two "opposite" corners
    #if rand() > 0.5:
    #    _u = rand()
    #    _v = (1 - _u) * rand()
    #else:
    #    _v = rand()
    #    _u = (1 - _v) * rand()

        
    rand_x, rand_y = x0 + (ux * _u) + (vx * _v), y0 + (uy * _u) + (vy * _v)
    
    return (rand_x, rand_y)
    
#Create random point in an arbitrary polygon
def random_point_in_poly(*list_points):
    #does not work for empty, single points
    if len(list_points) in (0,1):
        print("That is not enough points to make a polygon")
        return (0,0)
        
    #if you passed in a line
    if len(list_points) is 2:
        print("That is a line segment")
        return random_point_on_line(*list_points)
    
    #if you passed a triangle
    if len(list_points) is 3:
        print("That is a triangle")
        return random_point_in_tri(*list_points)
        

    pass
        
