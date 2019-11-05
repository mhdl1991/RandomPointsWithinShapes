import pyglet, itertools
from pyglet.window import mouse
import random_points as r #put this in the same folder

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
NUMBER_POINTS = 10000
window = pyglet.window.Window(width = WINDOW_WIDTH, height = WINDOW_HEIGHT)

#test to see if this kinda import works...
help(r.random_point_in_tri)

#Need to convert that into a list of ints rather than tuples
test_triangle = [(100, 100), (300, 600), (750, 250)]
list_tri = list( itertools.chain(*test_triangle) )

#randomize the number of points 
def random_points(triangle = test_triangle):
    triangle_randompoints = [r.random_point_in_tri(*triangle) for i in range(NUMBER_POINTS)]
    return list( itertools.chain(*triangle_randompoints) ) 
    
list_points = random_points()

#some text to describe what is happening
ft = pyglet.font.load("Terminal", 12)
describe_label = pyglet.font.Text(ft, x = 8, y = 800-16)
describe_label.text = "drawing {} red dots randomly within the white triangle.\n Left-click to generate another set of random points".format(NUMBER_POINTS)


@window.event        
def on_mouse_press(x, y, button, modifiers):
    global list_points
    if button == mouse.LEFT: list_points = random_points()



@window.event
def on_draw():
    window.clear()
    #Descriptive label
    describe_label.draw()
    #Draw the triangle
    pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES, ('v2f', list_tri), ('c3B', (255,255,255) * 3 ) )
    #Draw the points
    pyglet.graphics.draw(NUMBER_POINTS, pyglet.gl.GL_POINTS, ('v2f', list_points ), ('c3B', (255,0,0) * NUMBER_POINTS ) )
    
    
pyglet.app.run()
