# Takes a length and a width, Returns the rectangles area.
def rectangle_area(length, width):
    return length * width

area_rectangle1 = rectangle_area(10, 5)
area_rectangle2 = rectangle_area(15, 7)

radius1 = 4
area_circle1 = 3.14 * (radius1 ** 2)

radius2 = 6
area_circle2 = 3.14 * (radius2 ** 2)

print("Area of first rectangle:", area_rectangle1)
print("Area of second rectangle:", area_rectangle2)
print("Area of first circle:", area_circle1)
print("Area of second circle:", area_circle2)