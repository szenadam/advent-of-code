with open("input.txt") as f:
	inp = f.read().splitlines()

first_wire, second_wire = inp
first_wire = first_wire.split(",")
second_wire = second_wire.split(",")

def add_all_path_coordinates(wire, s = dict):
	r = 0
	c = 0
	count = 0

	for segment in wire:
		direction = segment[0]
		length = int(segment[1:])

		if direction == "U":
			for i in range(length):
				r -= 1
				count += 1
				s[(r, c)] = count
		elif direction == "D":
			for i in range(length):
				r += 1
				count += 1
				s[(r, c)] = count
		elif direction == "L":
			for i in range(length):
				c -= 1
				count += 1
				s[(r, c)] = count
		elif direction == "R":
			for i in range(length):
				c += 1
				count += 1
				s[(r, c)] = count

		print(segment, r, c)

first_wire_coordinates = dict()
second_wire_coordinates = dict()

add_all_path_coordinates(first_wire, first_wire_coordinates)
print()
add_all_path_coordinates(second_wire, second_wire_coordinates)

intersections = set(first_wire_coordinates.keys()).intersection(set(second_wire_coordinates.keys()))

print(intersections)

m = None

def man(x):
	return abs(x[0]) + abs(x[1])

for position in intersections:
	if m is None or first_wire_coordinates[position] + second_wire_coordinates[position] < first_wire_coordinates[m] + second_wire_coordinates[m]:
		m = position

print(first_wire_coordinates[m], second_wire_coordinates[m])
foo = []

for i in intersections:
    foo.append(man(i))

print(min(foo))