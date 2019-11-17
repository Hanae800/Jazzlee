

# This exercice is following the instructions on Processing Tutorials on how to generate colors and draw shapes 
#https://py.processing.org/tutorials/color/
#https://py.processing.org/tutorials/drawing/

size(200,200)
rectMode(CENTER)
rect(100,100,20,100)
ellipse(100,70,60,60)
ellipse(81,70,16,32) 
ellipse(119,70,16,32) 
line(90,150,80,160)
line(110,150,120,160)

# Here i painted the different parts of the boy with different colors by alligning the positions
#(x,y) with the same of the created forms.  
# Bright red
fill(255, 0, 0)
rect(100, 70, 60, 60)

# Dark red
fill(127, 0, 0)
ellipse(81,70,16,32)

# Pink (pale red)
fill(255, 200, 200)
ellipse(119,70,16,32)

#Add other shapes whith the same colors on the boy to the surrounding environement.
# Bright red
fill(255, 0, 0)
rect(150, 30, 70, 15)
# Here I am playing with the numbers to generate different colors than the one in the tutorials. 
# Brown 
fill(100, 0, 0)
ellipse(30,30,20,60)

# Pink (pale red)
fill(255, 200, 200)
rect(180,180,16,32)

# Dark Pink (dark red)
fill(255, 100, 100)
rect(30,150,20,50)
