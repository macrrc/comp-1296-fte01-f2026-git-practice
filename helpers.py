# Takes a length and a width, Returns the rectangles area.
def rectangle_area(length, width):
    return length * width

# Takes a radius. Returns the circle's area.
def circle_area(radius):
    return 3.14 * (radius ** 2)

# main guard clause
if __name__ == "__main__":
    print(rectangle_area(10, 10)) # outputs 100
    print(circle_area(1)) # outputs 3.14