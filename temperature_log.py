readings = [12.5, 14.0, 9.8, 16.2, 18.4, 15.1, 11.3]

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

# Takes a list of readings. Prints the weekly summary.
def print_summary(readings):
    print(f"Days recorded:   {len(readings)}")
    print(f"Average:         {average(readings)}°C")
    print(f"Warmest:         {warmest(readings)}°C")
    print(f"Days above 15°C: {days_above(readings, 15)}")

print_summary(readings)