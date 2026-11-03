from helpers import rectangle_area, circle_area

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