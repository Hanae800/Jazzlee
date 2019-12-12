

 #3-1. Event

class Car:
    
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
    
    def colorchange(self):
        self.c = color(220,233,200)

    def changeSpeed(self):
        self.xspeed = 5

    def drive(self):
        self.xpos = self.xpos + self.xspeed;
        if self.xpos > width:
            self.xpos = 0

class pedestrian:

    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);

myCar1 = Car(color(255, 0, 0), 0, 100, 2)
myCar2 = Car(color(0, 255, 255), 0, 10, 1)

def setup():
    size(200,200)
    
def keyPressed():
    if (key == CODED):
        if (keyCode == UP):
            myCar1.changeSpeed()
        elif (keyCode == DOWN):
            myCar1.changeColor()
    
def draw(): 
    background(255)
    myCar1.drive()
    myCar1.display()
    myCar2.drive()
    myCar2.display()
 

  #3-2. Interactivity           
class Click(object):

    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed
  
  #3-3.New Object
    def updatelocation(self, xpos, ypos):
        self.xpos = xpos
        self.ypos =ypos
        
    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10);
myClick1 = Click(color(22 , 22, 22), 0, 0, 10)

def keyPressed():
    if (key == CODED):
        if (keyCode == UP):
            myCar1.changeSpeed()
        elif (keyCode == DOWN):
            myCar1.changeColor() 
             
def setup():
    size(200,200)
    
def draw():
    background(255)    
    myCar1.drive()
    myCar1.display()
    myCar2.drive()
    myCar2.display()
    
    if ((keyPressed) and (key == ' ')):
        myCar2.colorchange(color(random(255), random(255), random(255)))

 
