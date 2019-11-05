import pyglet, itertools
from pyglet.window import mouse
import random_points as r #put this in the same folder

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
NUMBER_POINTS_TRI = 5000
NUMBER_POINTS_LINE = 40
window = pyglet.window.Window(width = WINDOW_WIDTH, height = WINDOW_HEIGHT)

#test to see if this kinda import works...
help(r.random_point_in_tri)
help(r.random_point_on_line)

#Need to convert that into a list of ints rather than tuples
test_triangle = [(100, 100), (300, 450), (600, 250)]
list_tri = list( itertools.chain(*test_triangle) )

test_line = [(1,550), (790,500)]
list_line = list(itertools.chain(*test_line))

#randomize the number of points in the triangle 
def random_points_tri(triangle = test_triangle):
    triangle_randompoints = [r.random_point_in_tri(*triangle) for i in range(NUMBER_POINTS_TRI)]
    return list( itertools.chain(*triangle_randompoints) ) 
    
#randomize the number of points in the line 
def random_points_line(line = test_line):
    x1,y1 = line[0]
    x2,y2 = line[1]
    line_randompoints = [r.random_point_on_line(x1,y1,x2,y2) for i in range(NUMBER_POINTS_LINE)]
    return list( itertools.chain(*line_randompoints) ) 
    
    
list_points_tri = random_points_tri()
list_points_line = random_points_line()

#some text to describe what is happening
ft = pyglet.font.load("Terminal", 12)
describe_label = pyglet.font.Text(ft, x = 8, y = 800-16)
describe_label.text = "Drawing {} red dots randomly within the white triangle.\nDrawing {} blue dots randomly within the line.\nLeft-click to generate another set of random points".format(NUMBER_POINTS_TRI, NUMBER_POINTS_LINE)

@window.event        
def on_mouse_press(x, y, button, modifiers):  
    global list_points_tri, list_points_line
    if button == mouse.LEFT: 
        list_points_tri = random_points_tri()
        list_points_line = random_points_line()
        

@window.event
def on_draw():
    window.clear()
    #Descriptive label
    describe_label.draw()
    #Draw the triangle
    pyglet.graphics.draw(3, pyglet.gl.GL_TRIANGLES, ('v2f', list_tri), ('c3B', (255,255,255) * 3 ) )
    #Draw the line
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES, ('v2f', list_line), ('c3B', (255,255,255) * 2 ) )
    
    #Draw the triangle points
    pyglet.graphics.draw(NUMBER_POINTS_TRI, pyglet.gl.GL_POINTS, ('v2f', list_points_tri ), ('c3B', (255,0,0) * NUMBER_POINTS_TRI ) )
    #Draw the line points
    pyglet.graphics.draw(NUMBER_POINTS_LINE, pyglet.gl.GL_POINTS, ('v2f', list_points_line ), ('c3B', (0,0,255) * NUMBER_POINTS_LINE ) )
    
pyglet.app.run()
