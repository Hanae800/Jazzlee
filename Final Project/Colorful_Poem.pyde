import re
def setup():
    global f
    size(1000,800) 
    fill(255, 200, 200)
    f = createFont("Arial",30)
    noLoop() # I Called this method to stop the draw() method from looping

def theguy():
    rectMode(CENTER)
    rect(700,400,20,100)
    ellipse(700,320,60,60)
    ellipse(680,285,15,20)
    fill(255, 165, 0) 
    ellipse(720,285,15,20)
    fill(255, 200, 200)

    #Here I associated the colors in text with random shapes to emphasize how looking at a word of a color could also trigger a shape 
    # Orange
    fill(255, 165, 0)
    rect(280, 105, 20, 15)
    # Blue
    fill(0, 0, 255)
    ellipse(325, 140, 20, 15)
    # Orange
    fill(255, 165, 0)
    rect(280, 500, 70, 15)
    # Green 
    fill(0, 255, 0)
    ellipse(170, 305, 20, 15)
    # Blue
    fill(0, 0, 255)
    rect(155,390,16,15)
    # Red
    fill(202, 0, 42)
    rect(250,530,50,20)

def findColorInStr(searchString, pos):     
    color_list = ["red", "blue", "orange", "green" ]
    red = color(202, 0, 42) #change the color of text by specifying a value of the color red. 
    blue = color(0, 0, 255) #change the color of text by specifying a value of the color blue. 
    orange = color(255, 165, 0) #change the color of text by specifying a value of the color orange. 
    green = color(0, 255, 0) #change the color of text by specifying a value of the color green. 
    black = color(0, 0, 0) #change the color of text by specifying a value of the color black. 
    sumWidth = 18
    colorsFound = []
    
    if re.compile('|'.join(color_list),re.IGNORECASE).search(searchString): #used compile method that allows to join an array of words into a string (compile) 
      #extract colors from the string and store them somewhere then check other colors 
      wordList = searchString.split() #split the color and color it differently. searchs the string for the existence of a word that represents a color.
      for x in wordList: 
        if (x in color_list): #find which colors were found and check the color
          colorsFound.append(x) #Add the rest of the sentence  
          
      for y in wordList:
          if (y in colorsFound and y == 'red'):
            fill(red)
            text(y, sumWidth, pos)
          elif (y in colorsFound and y == 'blue'):          
            fill(blue)
            text(y, sumWidth, pos)
          elif (y in colorsFound and y == 'green'):
            fill(green)
            text(y, sumWidth, pos)
          elif (y in colorsFound and y == 'orange'):
            fill(orange)
            text(y, sumWidth, pos)
          else:
            fill(black)
            text(y, sumWidth, pos)
          sumWidth = sumWidth + textWidth(y) + 2
    else: 
      fill(black)
      text(searchString, sumWidth, pos) #Displays the text
            
def draw():
    global f
    background(255, 300, 0)
    textFont(f,16)            
    fill(0)                 
    colors = loadStrings('colors.txt')
    pos = 18
    for lineText in colors:     
       findColorInStr(lineText, pos)
       pos = pos +18
    theguy()
    
