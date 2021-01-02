import turtle
from fractions import gcd

class Spiro
    # constructor
    def __init__(self, xc, yc, col, R, r, l):
        # create a turtle object
        self.t = turtle.Turtle()
        # set the cursor shape
        self.t.shape('turtle')
        # set the steps in dgrees
        self.step = 5
        # set drawing complete flag
        self.drawingComplete = False

        # set the parameters
        self.setparams(xc, yc, col, R, r, l)
        # initialize the drawing
        self.restart()

    # set the parameters
    def setparams(self, xc, yc, R, r, l):
        self.xc = xc
        self.yc = yc
        self.R = (int)R
        self.r = (int)r
        self.l = l
        #reduce r/R to smallest form by dividing by GCD
        gcdVal = gcd(self.r, self.R)
        self.nRot = self.r//gcdVal
        # get ratio of radii
        self.k = r/float(R)
        # set the color
        self.t.color (*col)
        # store the current angle
        self.a = 0

    # restart the drawing
    def restart(self):
        