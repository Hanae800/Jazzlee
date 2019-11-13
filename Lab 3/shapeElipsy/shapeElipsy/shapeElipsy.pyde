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
        
myShape = Shape(color(23, 25, 255), 100, 80, 50)

def setup():
    size(300,300)

def draw(): 
    background(255)
    myShape.display()
    if (mousePressed == True):
        x = Shape(color(23, 25, 255), mouseX, mouseY, 50)
        x.display()
