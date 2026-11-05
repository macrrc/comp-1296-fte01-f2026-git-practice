# Takes a length and a width, Returns the rectangles area.
def rectangle_area(length, width):
    return length * width

# Takes a radius. Returns the circle's area.
def circle_area(radius):
    return 3.14 * (radius ** 2)

# Takes a list of numbers. Returns their average, rounded to 1 decimal.
def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return round(total / len(numbers), 1)

# Takes a list of numbers. Returns the largest one.
def warmest(numbers):
    highest = numbers[0]
    for number in numbers:
        if number > highest:
            highest = number
    return highest

# Takes a list of numbers and a limit. Returns how many are above the limit.
def days_above(numbers, limit):
    count = 0
    for number in numbers:
        if number > limit:
            count += 1
    return count

def create_report_line(label, value, prefix=None):
    return f"{prefix}{label}: {value}"

# main guard clause
if __name__ == "__main__":
    print(rectangle_area(10, 10)) # outputs 100
    print(circle_area(1)) # outputs 3.14
