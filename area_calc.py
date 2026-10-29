# Takes a length and a width, Returns the rectangles area.
def rectangle_area(length, width):
    return length * width

# Takes a radius. Returns the circle's area.
def circle_area(radius):
    return 3.14 * (radius ** 2)

area_rectangle1 = rectangle_area(10, 5)
area_rectangle2 = rectangle_area(15, 7)

area_circle1 = circle_area(4)
area_circle2 = circle_area(6)

print("Area of first rectangle:", area_rectangle1)
print("Area of second rectangle:", area_rectangle2)
print("Area of first circle:", area_circle1)
print("Area of second circle:", area_circle2)