# Hangperson game to guess words
# uses turtle

import random
import turtle
import time

wordList = ['advocate', 'austere','benevolent', 'clout', 'complacent', 'deficient', 'eminent', 'facilitate', \
            'galvanizing', 'incite', 'novel', 'oust', 'retention', 'prohibit', 'undermine', 'tentative', 'vital', \
            'fiscal', 'evoke', 'disparage']

secretWord = random.choice(wordList)
wrongLetters = []
correctLetters = []
# print(wordList)
# DON'T SHOW PEOPLE THIS
print(f"The secret word is {secretWord}")

wrongGuesses = 0
MAX_GUESSES = 10

# set up screen
sWidth = 1200
sHeight = 400
turtle.colormode(255)
screen = turtle.getscreen()
screen.setup(sWidth, sHeight)
screen.bgcolor(114, 70, 235)

# setup turtle
t = turtle.getturtle()
t.shape("turtle")
t.color(242, 242, 208)
t.width(5)
t.speed(0)
t.penup()


# November 11 made new turtle
topFont = 50
topScreenTurtle = turtle.Turtle()
topScreenTurtle.hideturtle()
topScreenTurtle.shape("turtle")
topScreenTurtle.color(242, 242, 208)
topScreenTurtle.width(5)
topScreenTurtle.speed(0)
topScreenTurtle.penup()
topScreenTurtle.goto(-1 * int(sWidth/2) + int(sWidth * 0.1), -1 * int(sHeight/2) + int(sHeight * 0.40))

bottomScreenTurtle = turtle.Turtle()
bottomScreenTurtle.hideturtle()
bottomScreenTurtle.shape("turtle")
bottomScreenTurtle.color(250, 0, 0)
bottomScreenTurtle.width(5)
bottomScreenTurtle.speed(0)
bottomScreenTurtle.penup()
bottomScreenTurtle.goto(-1 * int(sWidth/2) + int(sWidth * 0.1), -1 * int(sHeight/2) + int(sHeight * 0.25))
bottomScreenTurtle.setheading(0)

def drawGallows():

    t.hideturtle()
    t.forward(int(sWidth * 0.125))
    t.right(90)

    t.forward(int(sHeight * 0.25))
    t.left(90)
    #sophie drawing
    t.pendown()
    t.forward(int(sWidth * 0.3))
    t.backward(int(sWidth * 0.125))
    t.left(90)
    t.forward(int(sHeight * 0.6))
    t.left(90)
    t.forward(int(sWidth * 0.125))
    t.left(90)
    t.forward(int(sHeight * 0.1))

def drawHead():
    t.right(90)
    t.circle(int(sHeight * 0.06))

def drawBody():
    t.left(90)
    t.penup()
    t.forward(int(sHeight * 0.06) * 2)
    t.pendown()
    t.forward(int(sHeight * 0.06) * 2)

def drawArm1():
    t.left(120)
    t.forward(40)
    t.backward(int(sHeight * 0.1))

def drawArm2():
    t.left(120)
    t.forward(40)
    t.left(360)
    t.backward(40)

def drawLeg1():
    t.pendown()
    t.left(120)
    t.forward(60)
    t.right(-120)
    t.forward(-40)
    t.right(360)
    t.forward(40)

def drawLeg2():
    t.right(-120)
    t.forward(-40)
    t.right(360)
    t.forward(40)

def drawHand1():
    t.right(60)
    t.forward(60)
    t.left(60)
    t.forward(40)
    t.right(90)
    t.circle(int(sHeight * 0.015))

def drawHand2():
    t.left(90)
    t.forward(-40)
    t.right(120)
    t.forward(40)
    t.right(90)
    t.circle(int(sHeight * 0.015))

def drawFoot1():
    t.left(270)
    t.forward(40)
    t.right(300)
    t.forward(60)
    t.right(60)
    t.forward(40)
    t.right(90)
    t.circle(int(sHeight * 0.019))

def drawFoot2():
    t.right(90)
    t.forward(40)
    t.left(60)
    t.right(120)
    t.forward(40)
    t.right(90)
    t.circle(int(sHeight * 0.019))

def updateDrawing():

    if wrongGuesses == 0:
        drawGallows()
    if wrongGuesses == 1:
        drawHead()
    if wrongGuesses == 2:
        drawBody()
    if wrongGuesses == 3:
        drawArm1()
    if wrongGuesses == 4:
        drawArm2()
    if wrongGuesses == 5:
        drawLeg1()
    if wrongGuesses == 6:
        drawLeg2()
    if wrongGuesses == 7:
        drawHand1()
    if wrongGuesses == 8:
        drawHand2()
    if wrongGuesses == 9:
        drawFoot1()
    if wrongGuesses == 10:
        drawFoot2()

def drawWrongLetters():
    topScreenTurtle.hideturtle()
    topScreenTurtle.clear()
    letterString = "Wrong Letters: "
    for l in wrongLetters:
        letterString += l + ","
    letterString = letterString[0 : len(letterString)-1]
    topScreenTurtle.write(letterString, move=False, align="left", font=("Arial", topFont, "normal"))


def drawWord():

     # step one -- save turtle position info
    #currentLoc = t.position()
    #currentHead = t.heading()
    bottomScreenTurtle.hideturtle()
    bottomScreenTurtle.clear()
    bottomScreenTurtle.hideturtle()
    bottomScreenTurtle.color(0, 250, 0)
    #bottomScreenTurtle.penup()
    bottomScreenTurtle.goto(-1 * int(sWidth/2) + int(sWidth * 0.1), -1 * int(sHeight/2) + int(sHeight * 0.25))
    #bottomScreenTurtle.showturtle()
    bottomScreenTurtle.setheading(0)

    screenWord = ""
    for letter in secretWord:
        if letter in correctLetters:
            screenWord += letter + " "
        else:
            screenWord += "_" + " "

    bottomScreenTurtle.write(screenWord, move=False, align="left", font=("Arial", 60, "normal"))
    #t.goto(currentLoc)
    #t.setheading(currentHead)
    #bottomScreenTurtle.showturtle()


def getGuess():
    badLetterString = ""
    for letter in wrongLetters:
        badLetterString += letter + " , "

    boxTitle = "Letters Used: " + badLetterString

    theGuess = screen.textinput(boxTitle, "Enter a letter or type $$ to guess the word")
    return theGuess

def writeErrorMessage(msg):
    topScreenTurtle.clear()
    topScreenTurtle.write(msg, move=False, align="left", font=("Arial", topFont, "normal"))
    time.sleep(2)
    topScreenTurtle.clear()


def printWinOrLose(win):
    topScreenTurtle.clear()

    if win:
        topScreenTurtle.write("You Win!!", move=False, align="left", font=("Arial", topFont, "normal"))

    else:
        topScreenTurtle.write("I'm sorry. Game over!", move=False, align="left", font=("Arial", topFont, "normal"))


def getWordGuess():

    playerWordGuess = screen.textinput("Guess It", "Enter your guess of the word?")

    if playerWordGuess.lower() == secretWord:
        # celebrate win !!
        #print("Win!!")
        printWinOrLose(True)
        return False # false means gameover
    else:
        # celebrate failure :(
        #print("Lose!!")
        printWinOrLose(False)
        time.sleep(1)
        writeErrorMessage("The secret word is: " + secretWord)
        return False


# Now we play game...


gameOn = True
updateDrawing()
while gameOn:

    drawWord()

    guess = getGuess()

    if guess == "$$":
        gameOn = getWordGuess()
    elif len(guess) != 1:
        writeErrorMessage("I need a single letter. Guess again.")
    elif guess.lower() not in "abcdefghijklmnopqrstuvwxyz":
        writeErrorMessage("I need a letter. Guess again.")
        drawWrongLetters()
    elif guess.lower() in wrongLetters:
        writeErrorMessage("You already guessed " + guess + ". Guess Again")
        drawWrongLetters()
    elif guess.lower() in correctLetters:
        writeErrorMessage(guess + " is in the word. Guess Again")
        drawWrongLetters()
    else:
        #if the letter is good . . .
        if guess.lower() in secretWord.lower():
            correctLetters.append(guess.lower())
            drawWord()
        else:
            #if the letter is bad . . .
            wrongLetters.append(guess.lower())
            wrongGuesses += 1
            drawWrongLetters()
            updateDrawing()

        if(wrongGuesses >= MAX_GUESSES):
            writeErrorMessage("You are out of guesses. Game Over")
            gameOn = False
            writeErrorMessage("The secret word is: " + secretWord)


    

    # get a guess
    # check the guess

    # if guess is letter
    # check the letter
    # tell them if right or wrong
    # if its wrong show it on screen
    # if its wrong take away a chance
    # if its wrong add a body part
    # if its right show letter
    # if you are wrong and you are out of chances then stop the game

    # if they guess the word
    # if they are right they win
    # if they are wrong they lose

turtle.mainloop()