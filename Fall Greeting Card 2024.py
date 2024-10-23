from graphics import*
import time

def pumpkinOneBody(win):
#this creates the first pumpkin circle
    pumpkinBase1 = Circle(Point(500, 450), 100)
    #this makes the circle orange
    pumpkinBase1.setFill("Orange")
    #this draws the circle in the window
    pumpkinBase1.draw(win)

    #this creates the second pumpkin circle
    pumpkinBase2 = Circle(Point(400, 450), 100)
    #this colors the circle orange
    pumpkinBase2.setFill("Orange")
    #this draws the circle in the window
    pumpkinBase2.draw(win)

    #this creates the third pumpkin circle
    pumpkinBase3 = Circle(Point(450, 450), 100)
    #this makes the circle orange
    pumpkinBase3.setFill("Orange")
    #this draws the pumpkin in the window
    pumpkinBase3.draw(win)

def pumpkinOneFeatures(win):
    #this creates the first pumpkin eye (triangle)
    pumpkinEye1 = Polygon(Point(400,450),Point(450,450),Point(425,400))
    #makes the triangle black
    pumpkinEye1.setFill("black")
    #draws the pumpkin eye in the window
    pumpkinEye1.draw(win)

    #creates pumpkin eye 2 as a clone of pumpkin eye 1
    pumpkinEye2 = pumpkinEye1.clone()
    #moves it to the right by 75 pixels
    pumpkinEye2.move(75, 0)
    #draws pumpkin eye 2 in the window
    pumpkinEye2.draw(win)

    #moves pumpkin eye 1 to the left by 25 pixels (needed a little more space between the eyes)
    pumpkinEye1.move(-25,0)

    #creates pumpkin nose from as a clone of pumpkin eye 2
    pumpkinNose = pumpkinEye2.clone()
    #moves it left 50 pixels and down 30 pixels
    pumpkinNose.move(-50, 30)
    #draws pumpkinNose in the window
    pumpkinNose.draw(win)

    #creates the pumpkinMouth (circle)
    pumpkinMouth = Circle(Point(450, 510), 20)
    #sets the color to black
    pumpkinMouth.setFill("black")
    #draws pumpkinMouth in window
    pumpkinMouth.draw(win)

    #returns variables as a list
    return [pumpkinEye1, pumpkinEye2, pumpkinMouth, pumpkinNose]

def pumpkinOneHat(win):
    #this creates an oval for the first hat base
    hatBase = Oval(Point(600, 325),Point(300, 375))
    #this sets the color to black
    hatBase.setFill("black")
    #this draws hatBase in the window
    hatBase.draw(win)

    #this creates the hatTop (triangle)
    hatTop = Polygon(Point(550,350), Point(450, 100), Point(350,350))
    #this sets the color to black
    hatTop.setFill("black")
    #this draws hatTop in the window
    hatTop.draw(win)

def pumpkinBodyTwo(win):
    #this creates one of the circles for the smaller pumpkin
    secondPumpkinB2 = Circle(Point(115, 500), 50)
    #this makes the circle orange
    secondPumpkinB2.setFill("Orange")
    #this draws the circle in the window
    secondPumpkinB2.draw(win)

    #this creates one of the circles for the smaller pumpkin by cloning the secondPumpkinB2
    secondPumpkinB3 = secondPumpkinB2.clone()
    #this moves it 70 pixels on the x axis (to the right)
    secondPumpkinB3.move(70,0)
    #this draws the circle in the window
    secondPumpkinB3.draw(win)

    #this creates the middle circle (so that it is on top of the other two) for the smaller pumpkin
    secondPumpkinB1 = Circle(Point(150, 500), 50)
    #this makes it orange
    secondPumpkinB1.setFill("Orange")
    #this draws the circle in the window
    secondPumpkinB1.draw(win)

def pumpkinTwoFeatures(win):
    #draws the pumpkin eye for the smaller pumpkin (triangle)
    smPumpkinEye1 = Polygon(Point(110,495),Point(130,495),Point(120,475))
    #colors it black
    smPumpkinEye1.setFill("black")
    #draws smPumpkinEye1 in the window
    smPumpkinEye1.draw(win)

    #makes smPumpkinEye2 from a clone of smPumpkinEye1
    smPumpkinEye2 = smPumpkinEye1.clone()
    #moves it to the right by 50 pixels
    smPumpkinEye2.move(50, 0)
    #draws it in the window
    smPumpkinEye2.draw(win)

    #creates a pumpkin nose for the smaller pumpkin 
    #from a clone of smPumpkinEye2
    smPumpkinNose = smPumpkinEye2.clone()
    #moves it left 25 pixels and down 20 pixels
    smPumpkinNose.move(-25, 20)
    #draws it in the window
    smPumpkinNose.draw(win)

    #creates the small pumpkin mouth (circle)
    smPumpkinMouth = Circle(Point(145, 530), 7)
    #colors it black
    smPumpkinMouth.setFill("black")
    #draws it in the window
    smPumpkinMouth.draw(win)

    #returns variables as a list
    return [smPumpkinEye1, smPumpkinEye2, smPumpkinMouth, smPumpkinNose]

def pumpkinTwoHat(win):
    #this creates an oval for the second hat base
    hatBase2 = Oval(Point(50, 425),Point(250, 475))
    #this sets the color to black
    hatBase2.setFill("black")
    #this draws hatBase2 in the window
    hatBase2.draw(win)

    #this creates the second hat top (triangle)
    hatTop2 = Polygon(Point(200,450), Point(150, 300), Point(100,450))
    #this sets the color to black
    hatTop2.setFill("black")
    #this draws hatTop2 in the window
    hatTop2.draw(win)

#function to make the pumpkins flicker
def flickeringElement(pumpkinOneFeatures, pumpkinTwoFeatures):
    #combines both function lists (so that they flicker together)
    allFeatures = pumpkinOneFeatures + pumpkinTwoFeatures 

    for i in range(5):
        # Set all features to yellow
        for feature in allFeatures:
            feature.setFill("yellow")
        time.sleep(0.5)
        
        # Set all features back to black
        for feature in allFeatures:
            feature.setFill("black")
        time.sleep(0.5)

def fallCard():
    myWin = GraphWin("Fall Greeting Card", 700, 700)
    myWin.setBackground(color_rgb(90, 40, 145))

    #This creates the text "fall is here!" at the specified point
    textBox1 = Text(Point(350,75), "Fall is here!")
    #this changes the text color to black
    textBox1.setFill("black")
    #this changes the font to courier
    textBox1.setFace("courier")
    #this changes the text size to 24
    textBox1.setSize(24)
    #this sets the text to bold
    textBox1.setStyle("bold")
    #this actually draws the text in the window
    textBox1.draw(myWin)

    #this tells the user to click the window to make the light flicker
    textBox2 = Text(Point(500, 625), "Click to make the light flicker \n inside the pumpkin!")
    #this changes the text color to black
    textBox2.setFill("black")
    #this draws the text in the window
    textBox2.draw(myWin)

    #calls function with myWin as parameter
    pumpkinOneBody(myWin)
    #calls function with myWin as parameter
    pumpkinBodyTwo(myWin)

    #calls function with myWin as parameter
    pumpkinOneHat(myWin)
    #calls function with myWin as parameter
    pumpkinTwoHat(myWin)

    #calls function with myWin as parameter
    pumpkinOneFeatures(myWin)
    #calls function with myWin as parameter
    pumpkinTwoFeatures(myWin)

    #defines variables as feature functions with myWin as parameter
    faceOne = pumpkinOneFeatures(myWin)
    faceTwo = pumpkinTwoFeatures(myWin)

    #waits for mouse click
    myWin.getMouse()

    #calls function with faceOne and faceTwo as parameters
    flickeringElement(faceOne, faceTwo)

    #undraws textBox2
    textBox2.undraw()

    #redraws textBox2 so that it says "Click anywehre to quit."
    textBox2 = Text(Point(500, 625), "Click anywhere to quit.").draw(myWin)

    #waits for mouse click
    myWin.getMouse()
    
    #when user clicks mouse the window will close
    myWin.close()

def main():
    fallCard()

main()





