from helpers import average, warmest, days_above

readings = [12.5, 14.0, 9.8, 16.2, 18.4, 15.1, 11.3]

# Takes a list of readings. Prints the weekly summary.
def print_summary(readings):
    print(f"Days recorded:   {len(readings)}")
    print(f"Average:         {average(readings)}°C")
    print(f"Warmest:         {warmest(readings)}°C")
    print(f"Days above 15°C: {days_above(readings, 15)}")

if __name__ == "__main__":
    print_summary(readings)