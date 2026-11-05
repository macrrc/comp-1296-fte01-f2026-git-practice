from helpers.geometry import rectangle_area, circle_area
from helpers.reports import create_report_line

# execute the main program flow
def main():
    shapes = {
        "first rectangle": rectangle_area(10, 5),
        "second rectangle": rectangle_area(15, 7),
        "first circle": circle_area(4),
        "second circle": circle_area(6)
    }

    for name, area in shapes.items():
       print(create_report_line(name, area, "Area of "))

# main guard clause
if __name__ == "__main__":
    main()