from cf_classes_2 import Possition, Playing_grid, The_map

A_map = The_map(Playing_grid(17, 18), "Test Map")

#Maps available locations
A_map.add_location(Possition("A", "location", [11, 6]))
A_map.add_location(Possition("B", "location", [8, 12]))
A_map.add_location(Possition("C", "location", [17, 18]))
A_map.add_location(Possition("D", "location", [1, 14]))
A_map.add_location(Possition("E", "location", [7, 3]))
A_map.add_location(Possition("F", "location", [14, 10]))
A_map.add_location(Possition("G", "location", [2, 17]))
A_map.add_location(Possition("H", "location", [16, 2]))

#Maps roads that conncets the map locations
A_map.add_road(Possition("A", "road", [A_map.locations[0], A_map.locations[1]]))
A_map.add_road(Possition("B", "road", [A_map.locations[2], A_map.locations[3]]))
A_map.add_road(Possition("C", "road", [A_map.locations[0], A_map.locations[5]]))
A_map.add_road(Possition("D", "road", [A_map.locations[1], A_map.locations[5]]))
A_map.add_road(Possition("E", "road", [A_map.locations[4], A_map.locations[3]]))
A_map.add_road(Possition("F", "road", [A_map.locations[4], A_map.locations[0]]))
A_map.add_road(Possition("G", "road", [A_map.locations[2], A_map.locations[5]]))
A_map.add_road(Possition("H", "road", [A_map.locations[3], A_map.locations[1]]))
A_map.add_road(Possition("I", "road", [A_map.locations[2], A_map.locations[6]]))
A_map.add_road(Possition("J", "road", [A_map.locations[1], A_map.locations[6]]))
A_map.add_road(Possition("K", "road", [A_map.locations[7], A_map.locations[4]]))
A_map.add_road(Possition("L", "road", [A_map.locations[7], A_map.locations[1]]))
A_map.add_road(Possition("M", "road", [A_map.locations[7], A_map.locations[2]]))
A_map.add_road(Possition("N", "road", [A_map.locations[7], A_map.locations[0]]))

#Here I can edit where each player will begin inside the map using either random_starting_positions() for random position or manually using .starting_positions to pust specific positions for each players. example A_map.starting_positions[player_number] = location_position_in_list
A_map.random_starting_positions()

A_map.create_map()
print(A_map)




cimetrical = The_map(Playing_grid(31, 27), "Cimetrical Map")

for x in range(2, 31, 4):
	for y in range(2, 27, 4):
		cimetrical.add_location(Possition(chr(x + 63) + chr(y + 63), "location", [x, y]))


for i in range(0, len(cimetrical.locations)):
	#if not at the right-most positions
	if cimetrical.locations[i].location[1] != 26:
		#+1 for right
		cimetrical.add_road(Possition(chr(i + 65) + chr(65), "road", [cimetrical.locations[i], cimetrical.locations[i + 1]]))
		#if not at the down-most positions
		if cimetrical.locations[i].location[0] != 30:
			#+10 for right/down
			cimetrical.add_road(Possition(chr(i + 65) + chr(67), "road", [cimetrical.locations[i], cimetrical.locations[i + 8]]))
	#if not at the down-most positions
	if cimetrical.locations[i].location[0] != 30:
		#+9 for down
		cimetrical.add_road(Possition(chr(i + 65) + chr(66), "road", [cimetrical.locations[i], cimetrical.locations[i + 7]]))
	#if not at the left-most positions and down-most positions
	if cimetrical.locations[i].location[1] != 2 and cimetrical.locations[i].location[0] != 30:
		#+8 for left/down
		cimetrical.add_road(Possition(chr(i + 65) + chr(68), "road", [cimetrical.locations[i], cimetrical.locations[i + 6]]))

cimetrical.random_starting_positions()

cimetrical.create_map()
print(cimetrical)


#position 0, 1 and 2 should be the easy, normal and hard map
maps = [A_map, A_map, A_map, A_map, A_map, A_map, A_map, A_map, cimetrical, A_map]
