#Maia Reynolds
#2/8/18
#house.py - make a house

from ggame import *
basecolor=Color(0x00B2EE,1)
outlinecolor=Color(0x00688B,1)
roofoutlinecolor=Color(0x00688B,1)
roofcolor=Color(0x696969,1)
baseoutline=LineStyle(3,outlinecolor)
roofoutline=LineStyle(3,roofoutlinecolor)
grasscolor=Color(0x66CD00,1)
grassoutline=LineStyle(1,grasscolor)
doorcolor=Color(0xCD2626,1)
dooroutlinecolor=Color(0x8B1A1A,1)
dooroutline=LineStyle(5,dooroutlinecolor)
skycolor=Color(0x9AC0CD,.6)
skyoutline=LineStyle(1,skycolor)

front=PolygonAsset([(400,200),(500,100),(600,200),(600,300),(400,300)],baseoutline,basecolor)
side=PolygonAsset([(400,300),(300,250),(300,150),(400,200)],baseoutline,basecolor)
roof=PolygonAsset([(500,100),(390,210),(290,160),(400,50)],roofoutline,roofcolor)
grass=RectangleAsset(1100,400,grassoutline,grasscolor)
door=RectangleAsset(35,70,dooroutline,doorcolor)
roofline=LineAsset(110,110,roofoutline)
sky=RectangleAsset(1100,500,skyoutline,skycolor)
window=RectangleAsset(35,35,dooroutline,roofcolor)

Sprite(sky)
Sprite(grass,(0,200))
Sprite(front,(400,100))
Sprite(side,(300,150))
Sprite(roof,(290,50))
Sprite(door,(482.5,230))
Sprite(roofline,(500,100))
Sprite(window,(427.5,240))
Sprite(window,(537.5,240))
App().run()