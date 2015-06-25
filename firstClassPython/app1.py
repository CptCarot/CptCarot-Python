#!/Python27/python

import math

import external_classes
        

myNewRectangle = external_classes.rectangle(5,6)
myNewSquare = external_classes.square(6)
mySecondSquare = external_classes.square(4)
myNewCircle = [ external_classes.circle(i+1) for i in range(5) ]

print("Content-type: text/html")
print("")
print("<html>")
print("<head>")
print("<title>Python27 Dan1 CGI</title>")
print("</head>")
print("<body>")

print("<div>")
print("NRec Perimeter = " + str(myNewRectangle.perimeter()))
print("NRec Area = " + str(myNewRectangle.area()))
print("</div>")

print("<div>")
print("NSq Perimeter = " + str(myNewSquare.perimeter()))
print("NSq Area = " + str(myNewSquare.area()))
print("</div>")

print("<div>")
print("2ndSq Perimeter = " + str(mySecondSquare.perimeter()))
print("2ndSq Area = " + str(mySecondSquare.area()))
print("</div>")

print("<div>")
mySecondSquare.changeX(20)
print("2ndSq" + "(20)" + "  Area = " +str(mySecondSquare.area()))
print("</div>")

for i in range(5):
    print("<div>")
    print(" Radius = " + str(myNewCircle[i].x))
    print(" Area = " + str(myNewCircle[i].area()))
    print(" Perimeter = " + str(myNewCircle[i].perimeter()))
    print("</div>")

print("</body>")
print("</html>") 
