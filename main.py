from p5 import *

rectangle = None

def setup():
        size(640, 260)
        rectangle = PShape()
        with rectangle.edit():
                rectangle.add_vertex((0, 0))
                rectangle.add_vertex((50, 0))
                rectangle.add_vertex((50, 100))
                rectangle.add_vertex((0, 100))

        rectangle.stroke = color(255)
        rectangle.stroke_weight = 4
        rectangle._fill = color(127)

def draw():
        background(51)
        translate(mouse_x, mouse_y)
        rectangle.set_fill(color(remap(mouse_x, (0, width), (0, 255))))
        draw_shape(rectangle)

if __name__ == '__main__':
    run()
