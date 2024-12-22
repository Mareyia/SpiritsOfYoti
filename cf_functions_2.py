from cf_classes_2 import entity
from cf_list_dicts import A_map

random_character = entity("*", A_map.locations[4])
A_map.add_entity(random_character)
A_map.create_map()

print(A_map)

def lets_move():
	where = input("Choose a destination (0-5): ")
	while int(where) in range(6):
		A_map.move_entity(random_character, A_map.locations[int(where)])
		print(A_map)
		where = input("Choose a destination (0-5): ")

lets_move()
