class House:
    def display(self):
        # Create the shape group
        alien = createShape(GROUP)
        # Make two shapes
        body = createShape(RECT, 5, 200, 300, 200)
        body.setFill(color(0))
        door = createShape(RECT, 120, 290, 70, 100)
        door.setFill(color(77))
        roof = createShape(TRIANGLE, -10, 200, 150, 100, 320, 200)
        roof.setFill(color(230))
        window = createShape(RECT, 20, 230, 80, 100)
        window.setFill(color(255))
        # Add the two "child" shapes to the parent group
        alien.addChild(body)
        alien.addChild(door)
        alien.addChild(roof)
        alien.addChild(window)        
        translate(50, 15)
        shape(alien)  # Draw the group

myHouse = House()
myHousex = House()
myHousey = House()
myHousez = House()
houses = [myHouse, myHousex, myHousey, myHousez]    
                          
def setup():
    size(400,400)
    
def draw(): 
    background(255)
    
    houses[0].display()
