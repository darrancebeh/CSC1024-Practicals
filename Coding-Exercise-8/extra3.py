def getRadius(center, point):
    return (point - center);

def getDiameter(center, point):
    diameter = (point - center) * 2
    return (diameter);

def getCircumference(radius):
    return (2 * 3.14 * radius);

def getArea(radius):
    return (3.14 * radius ** 2);

center = int(input("Enter the center of the circle: "));
point = int(input("Enter the point on the circle: "));

radius = getRadius(center, point);
diameter = getDiameter(center, point);
circumference = getCircumference(radius);
area = getArea(radius);

print(f"Radius = {radius}");
print(f"Diameter = {diameter}");
print(f"Circumference = {circumference}");
print(f"Area = {area}");
