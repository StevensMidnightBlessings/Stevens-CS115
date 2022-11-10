# mandelbrot.py
'''
Created on 11/10/22
@author:   
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 9
'''

# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:


def mult(c, n):
    '''mult uses only a loop and addition to multiply c by the integer n'''
    result = 0
    for x in range(n):
        y = result + c
        result = y
    return result

def update(c, n):
    '''update starts with z=0 and runs z = z**2 + c for a total of n times. It returns the final z.'''
    z = 0
    for x in range(n):
        z = z**2 + c
    return z

def weWantThisPixel( col, row ): 
    """ a function that returns True if we want 
        the pixel at col, row and False otherwise 
    """ 
    if col%10 == 0  and  row%10 == 0: 
        return True 
    else: 
        return False 
 
def test(): 
    """ a function to demonstrate how 
        to create and save a png image 
    """ 
    width = 300 
    height = 200 
    image = PNGImage(width, height) 
 
    # create a loop in order to draw some pixels 
     
    for col in range(width): 
        for row in range(height): 
            if weWantThisPixel( col, row ) == True: 
                image.plotPoint(col, row) 
 
    # we looped through every image pixel; we now write the file 
 
    image.saveFile() 

def inMSet(c, n):
    '''inMSet takes in  
        c for the update step of z = z**2+c 
        n, the maximum number of times to run that step 
      Then, it should return  
        False as soon as abs(z) gets larger than 2 
        True if abs(z) never gets larger than 2 (for n iterations) '''
    z = 0
    for x in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

def scale(pix, pixMax, floatMin, floatMax): 
    ''' scale takes in 
            pix, the CURRENT pixel column (or row) 
            pixMax, the total # of pixel columns 
            floatMin, the min floating-point value 
            floatMax, the max floating-point value 
        scale returns the floating-point value that 
            corresponds to pix '''
    x = 1.0 * pix / pixMax
    flo = floatMax - floatMin
    return flo * x + floatMin

def mset(): 
    ''' creates a 300x200 image of the Mandelbrot set ''' 
    width = 300 
    height = 200
    image = PNGImage(width, height) 
 
    # create a loop in order to draw some pixels 
     
    for col in range(width): 
        for row in range(height): 
            # here is where you will need 
            # to create the complex number, c!
            n = 25
            x = scale(col, width, -2.0, 1.0)
            y = scale(row, height, -1.0, 1.0)
            c =  x + y * 1j
            if inMSet( c, n ) == True: 
                image.plotPoint(col, row) 
 
    # we looped through every image pixel; we now write the file 
 
    image.saveFile()

print(mset())

import unittest
class Test(unittest.TestCase):
    def testMult(self):
        self.assertEqual(mult(6, 7), 42)
        self.assertEqual(mult(1.5, 28), 42.0)
    def testUpdate(self):
        self.assertEqual(update(1, 3), 5)
        self.assertEqual(update(-1, 3), -1)
        self.assertEqual(update(1, 10), 3791862310265926082868235028027893277370233152247388584761734150717768254410341175325352026)
        self.assertEqual(update(-1, 10), 0)
    def testImSet(self):
        self.assertEqual(inMSet(0 + 0j, 25), True)
        self.assertEqual(inMSet(3 + 4j, 25), False)
        self.assertEqual(inMSet(0.3 + -0.5j, 25), True)
        self.assertEqual(inMSet(-0.7 + 0.3j, 25), False)
        self.assertEqual(inMSet(0.42 + 0.2j, 25), True)
        self.assertEqual(inMSet(0.42 + 0.2j, 50), False)
    def testScale(self):
        self.assertEqual(scale(100, 200, -2.0, 1.0), -0.5)
        self.assertEqual(scale(100, 200, -1.5, 1.5), 0.0)
        self.assertEqual(scale(100, 300, -2.0, 1.0), -1.0)
        self.assertEqual(scale(25, 300, -2.0, 1.0), -1.75)
        self.assertEqual(scale(299, 300, -2.0, 1.0), 0.9900000000000002)
unittest.main()

