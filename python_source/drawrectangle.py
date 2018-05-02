from graphics import *

def plotSquare(win, side):
    rect=Rectangle(Point(side//2,side//2), Point(side,side))

    rect.setWidth(5)
    rect.draw(win)

def main ():
    win=GraphWin("My Window", 500, 500)
    win.setCoords(0, 0, 500, 500)
    win.width=500
    win.height=500
    side=eval(input("What is the size of one side of the square (0<n<500): "))

    plotSquare(win, side)

    win.getMouse()
    win.close

main()