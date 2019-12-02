from math import floor

def calculate_required_fuel(mass):
    return floor(mass / 3) - 2

data = open('./input.txt', 'r')

result = 0

for i in data.readlines():
    n = int(i.strip())
    result += n

print(result)