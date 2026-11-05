from helpers import (
    rectangle_area,
    circle_area,
    average,
    warmest,
    days_above,
    create_report_line
)

assert rectangle_area(10, 10) == 100, "rectangle 10 and 10"
assert circle_area(1) == 3.14, "circle radius 1"
assert average([1, 1]) == 1, "average of 1 and 1"
assert warmest([5, 10]) == 10, "warmest of 5 and 10"
assert days_above([1, 5, 10], 6) == 1, "days above 6"
assert create_report_line("label", "value", "prefix ") == "prefix label: value"

print("All tests passed!!")