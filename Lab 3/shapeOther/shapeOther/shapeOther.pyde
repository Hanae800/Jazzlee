class Shape:

    def __init__(self, c, x, y, r):
        self.c = c
        self.x = x
        self.y = y
        self.r = r
        
    def display(self):
        stroke(255)
        fill(self.c)
        ellipse(self.x, self.y, self.r * 2, self.r * 2);
        
class ShapeX:

    def __init__(self, c, x, y, w, h):
        self.c = c
        self.x = x
        self.y = y        
        self.w = w
        self.h = h        
        
    def display(self):
        stroke(255)
        fill(self.c)
        rect(self.x, self.y, self.w, self.h)
        
myShape = Shape(color(23, 25, 255), 100, 80, 50)

def setup():
    size(300,300)

def keyPressed():
    if (key == CODED):
        if (keyCode == UP):
             x = ShapeX(color(2, 255, 20), 100, 100, 80, 80)
             x.display()

def draw(): 
    background(255)
    myShape.display()
