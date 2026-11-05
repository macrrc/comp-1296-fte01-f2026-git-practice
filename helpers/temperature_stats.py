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

if __name__ == "__main__":
    pass