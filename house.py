#Maia Reynolds
#2/8/18
#house.py - make a house

from ggame import *
basecolor=Color(0x00B2EE,1)
outlinecolor=Color(0x00688B,1)
baseoutline=LineStyle(1,outlinecolor)

front=RectangleAsset(200,100,baseoutline,basecolor)
front2=PolygonAsset([(400,200

Sprite(front,(400,200))

blackOutline=LineStyle(1,black)
redRectangle=RectangleAsset(200,100,blackOutline,red) #width, height, outline, fill
blueCircle=CircleAsset(50,blackOutline,blue) #radius, outline, fill
greenEllipse=EllipseAsset(100,50,blackOutline,green) #width, height, outline, fill
blackLine=LineAsset(500,100,blackOutline) #to x over, to y over, lineStyle
purpleTriangle=PolygonAsset([(0,100),(50,200),(100,100)],blackOutline,purple) #endpoints, outline, fill
text=TextAsset("Maia", fill=blue, style="bold 60pt Times") #What you want, other options

Sprite(redRectangle)
Sprite(blueCircle,(200,0)) #... ,(over x, over y)
Sprite(greenEllipse,(300,0))
Sprite(blackLine)
Sprite(purpleTriangle)
Sprite(text,(600,0))

App().run()
