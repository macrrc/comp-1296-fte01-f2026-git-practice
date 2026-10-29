# Takes a length and a width, Returns the rectangles area.
def rectangle_area(length, width):
    return length * width

# Takes a radius. Returns the circle's area.
def circle_area(radius):
    return 3.14 * (radius ** 2)

# Takes a shape's name and it's area. Prints one line report.
def print_area(name, area):
    print(f"Area of {name}: {area}")

shapes = {
    "first rectangle": rectangle_area(10, 5),
    "second rectangle": rectangle_area(15, 7),
    "first circle": circle_area(4),
    "second circle": circle_area(6)
}

for name, area in shapes.items():
    print_area(name, area)