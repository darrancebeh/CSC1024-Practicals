def getRadius(centerX, centerY, pointX, pointY):
    radius = ((pointX - centerX) ** 2 + (pointY - centerY) ** 2) ** 0.5
    return (radius);

def getDiameter(radius):
    return (2 * radius);

def getCircumference(radius):
    return (2 * 3.14 * radius);

def getArea(radius):
    return (3.14 * radius ** 2);

print("\n\n")
centerX = int(input("Enter the x-coordinate of center of the circle: "));
centerY = int(input("Enter the y-coordinate of center of the circle: "));
pointX = int(input("Enter the x-coordinate of a point on the circle: "));
pointY = int(input("Enter the y-coordinate of a point on the circle: "));

radius = getRadius(centerX, centerY, pointX, pointY);
diameter = getDiameter(radius);
circumference = getCircumference(radius);
area = getArea(radius);

print(f"Radius = {radius}");
print(f"Diameter = {diameter}");
print(f"Circumference = {circumference}");
print(f"Area = {area}");
