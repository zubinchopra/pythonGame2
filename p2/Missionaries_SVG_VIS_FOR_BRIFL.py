# Author:  S. Tanimoto / Modified by Anoop Narra
# Purpose: test svgwrite with the new SOLUZION server and client
# Created: 2017
# Python version 3.x

import svgwrite
# Imported h1 here from Missionaries
from p2 import lhs, get_sum
#import random
#from datetime import datetime

DEBUG = False
W=600; H=200
BOAT_LENGTH_FRAC = 0.2  # fraction of overall width W
BOAT_HEIGHT_FRAC = 0.2  # fraction of overall height H
equation = ""

def render_state(s):
    global W,H,BOAT_LENGTH_FRAC, DEBUG, equation

    dwg = svgwrite.Drawing(filename = "test-svgwrite.svg",
                           id = "state_svg",  # Must match the id in the html template.
                           size = (str(W)+"px", str(H)+"px"),
                           debug=True)
    if (lhs[0] == "-"):
        equation += "-"
    for num in range (1, len(lhs)):
        equation += lhs[num]

    # Background rectangle...
    dwg.add(dwg.rect(insert = (0,0),
                     size = (str(W)+"px", str(H)+"px"),
                     stroke_width = "1",
                     stroke = "black",
                     fill = "rgb(192, 150, 129)")) # tan

    dwg.add(dwg.text('Equation: ' + equation + " = " + str(get_sum()) , insert = (250,100),
                     font_size="15",
                     fill="white"))


    equation = ""
    return (dwg.tostring())
