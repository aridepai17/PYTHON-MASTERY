numDays = int(input("How many day's temperature: "))
total = 0
for i in range(1, numDays + 1):
    temperature = float(input(f"Enter the temperature for day {i}: "))
    total += temperature
average = total / numDays

print(f"The average temperature for {numDays} days is: {average:.2f}°C")
