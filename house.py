#Maia Reynolds
#2/8/18
#house.py - make a house

from ggame import *
basecolor=Color(0x00B2EE,1)
outlinecolor=Color(0x00688B,1)
roofoutlinecolor=Color(0x00688B,1)
roofcolor=Color(0x696969,1)
baseoutline=LineStyle(1,outlinecolor)
roofoutline=LineStyle(1,roofoutlinecolor)

front=PolygonAsset([(400,200),(500,100),(600,200),(600,300),(400,300)],baseoutline,basecolor)
side=PolygonAsset([(400,300),(300,250),(300,150),(400,200)],baseoutline,basecolor)
roof=PolygonAsset([(500,100),(390,210),(290,160),(400,50)],roofoutline,roofcolor)

500,100)(390,210)(290,160)(400,50)

Sprite(front,(400,100))
Sprite(side,(300,150))
Sprite(roof,(290,50))
App().run()

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