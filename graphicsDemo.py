#Maia Reynolds
#2/7/18
#graphicsDemo.py - intro to ggame

from ggame import *
red=Color(0xFF0000,1) #this is the color red
green=Color(0x00FF00,1) #Color, red,green,blue , opacity
blue=Color(0x0000FF,1)
black=Color(0x000000,1) #this is the color black

blackOutline=LineStyle(1,black)
redRectangle=RectangleAsset(200,100,blackOutline,red) #width, height, outline, fill
blueCircle=CircleAsset(50,blackOutline,blue) #radius, outline, fill
greenEllipse=EllipseAsset(100,50,blackOutline,green) #width, height, outline, fill

Sprite(redRectangle)
Sprite(blueCircle,(200,0)) #... ,(over x, over y)
Sprite(greenEllipse,(300,0))

App().run()