from cf_list_dicts import decks
#from math import abs


class entity:
	def __init__(self, character, starting_position, npc=False):
		self.character = character
		self.position = starting_position
		self.npc = npc




class possition:
	def __init__(self, identity, type_of, location, entity_ocupied=None, autofill_roads=True):
		self.identity = identity
		self.type_of = type_of
		self.location = location
		self.distance = 0
		self.destinacions = {}
		self.entity_ocupation = entity_ocupied
		self.autofill_roads =  autofill_roads
		#if position is a road and you don't want to manually add its parts it can happen automatically autoffilling the map distance
		if self.type_of == "road":
			for loc in location:
				loc.add_roads(self)
			if autofill_roads == True:
				location_A_postion_x = self.location[0].location[0]
				location_A_postion_y = self.location[0].location[1]
				location_B_postion_x = self.location[1].location[0]
				location_B_postion_y = self.location[1].location[1]
				x_distance = location_A_postion_x - location_B_postion_x
				y_distance = location_A_postion_y - location_B_postion_y
				self.distance = abs(x_distance) + abs(y_distance)
				copy_of_distance = self.distance
				while copy_of_distance > 0:
					if x_distance > 0:
						location_A_postion_x -= 1
						self.destinacions[copy_of_distance] = possition("RP_"+str(copy_of_distance), "road_part", [location_A_postion_x, location_A_postion_y])
						copy_of_distance -= 1
						x_distance -= 1
						if x_distance > 0:
							location_B_postion_x += 1
							self.destinacions[copy_of_distance] = possition("RP_"+str(copy_of_distance), "road_part", [location_B_postion_x, location_B_postion_y])
							copy_of_distance -= 1
							x_distance -= 1
					if y_distance > 0:
						location_A_postion_y -= 1
						self.destinacions[copy_of_distance] = possition("RP_"+str(copy_of_distance), "road_part", [location_A_postion_x, location_A_postion_y])
						copy_of_distance -= 1
						y_distance -= 1
						if y_distance > 0:
							location_B_postion_y += 1
							self.destinacions[copy_of_distance] = possition("RP_"+str(copy_of_distance), "road_part", [location_B_postion_x, location_B_postion_y])
							copy_of_distance -= 1
							y_distance -= 1

					if x_distance < 0:
						location_A_postion_x += 1
						self.destinacions[copy_of_distance] = possition("RP_"+str(copy_of_distance), "road_part", [location_A_postion_x, location_A_postion_y])
						copy_of_distance -= 1
						x_distance += 1
						if x_distance < 0:
							location_B_postion_x -= 1
							self.destinacions[copy_of_distance] = possition("RP_"+str(copy_of_distance), "road_part", [location_B_postion_x, location_B_postion_y])
							copy_of_distance -= 1
							x_distance += 1
					if y_distance < 0:
						location_A_postion_y += 1
						self.destinacions[copy_of_distance] = possition("RP_"+str(copy_of_distance), "road_part", [location_A_postion_x, location_A_postion_y])
						copy_of_distance -= 1
						y_distance += 1
						if y_distance < 0:
							location_B_postion_y -= 1
							self.destinacions[copy_of_distance] = possition("RP_"+str(copy_of_distance), "road_part", [location_B_postion_x, location_B_postion_y])
							copy_of_distance -= 1
							y_distance += 1

	def add_roads(self, road):
		self.destinacions[road.identity] = road
	
	def add_road_parts(self, road_part):
		self.destinacions[road_part.identity] = road_part
		self.distance += 1
		




class the_map:
	def __init__(self, x_length, y_length):
		self.number_of_digits_for_spacing = 0
		self.string_for_spacing = ""
		self.find_digit = y_length
		if x_length > y_length:
			self.find_digit = x_length
		while self.find_digit > 0:
			self.find_digit = self.find_digit // 10
			self.number_of_digits_for_spacing += 1
		for i in range(self.number_of_digits_for_spacing):
			self.string_for_spacing += " "
		
		self.map_positions = []
		for x in range(x_length+1):
			self.map_positions.append([])
			for y in range(y_length+1):
				space_needed = self.number_of_digits_for_spacing
				if x == 0:
					current_number = y
					while current_number > 0:
						space_needed -= 1
						current_number = current_number // 10
					if (x == 0 and y == 0):
						space_needed -= 1
					added_space = ""
					for i in range(space_needed):
						added_space += " "
					self.map_positions[x].append(added_space + str(y))
				elif y == 0:
					current_number = x
					while current_number > 0:
						space_needed -= 1
						current_number = current_number // 10
					added_space = ""
					for i in range(space_needed):
						added_space += " "
					self.map_positions[x].append(added_space + str(x))
				else:
					self.map_positions[x].append(self.string_for_spacing)

	def __repr__(self):
		string_repr = ""
		for square_in_x in self.map_positions:
			string_repr += "\n||-|-"
			for square_in_y in square_in_x:
				string_repr += square_in_y + "-|-"
			string_repr += "||"
		string_repr += "\n"

		return string_repr
		
	def add_position(self, square):
		square_string = square.identity
		if len(square_string) > self.number_of_digits_for_spacing:
			square_string = square_string[0]
		space_needed = self.number_of_digits_for_spacing - len(square_string)
		adding_space = ""
		if space_needed > 0:
			for i in range(space_needed):
				adding_space += " "
		
		self.map_positions[square.location[0]][square.location[1]] = adding_space + square_string
		
	def fill_the_road(self, road):
		for road_part in road.destinacions:
			self.add_position(road.destinacions[road_part])




location_A = possition("A_l", "location", [11, 6])
location_B = possition("B_l", "location", [8, 12])
road_A = possition("A_r", "road", [location_A, location_B])

location_C = possition("C_l", "location", [17, 25])
location_D = possition("D_l", "location", [1, 17])
road_B = possition("B_r", "road", [location_C, location_D])

location_E = possition("E_l", "location", [7, 3])
location_F = possition("F_l", "location", [14, 10])
road_C = possition("C_r", "road", [location_E, location_F])

A_map = the_map(17, 25)

A_map.fill_the_road(road_A)
A_map.fill_the_road(road_B)
A_map.fill_the_road(road_C)
A_map.add_position(location_A)
A_map.add_position(location_B)
A_map.add_position(location_C)
A_map.add_position(location_E)
A_map.add_position(location_D)
A_map.add_position(location_F)

print(A_map)





















##### Below lies two classes with methods that creates a massive tree with millions of nodes that represents all the card combinations that can happen; with the perpose of making an ultimate difficulty for the computer that will know exactly what will be the best move in any case.
##### The creation and traversing of this tree even with less than 12 cards is enouph to fill 16gb of ram and freeze the computer, so this methode is not recomended and further development has been terminated.

class move:
	def __init__(self, card, i=0):
		self.move = card
		self.moves = []
		self.number = i
	
	def add_next_move(self, next_move):
		self.moves.append(next_move)
		
	def traverse(self, print_helper=""):
		print(print_helper + self.move.name_of_card)
		print_helper += "|-->"
		if len(self.moves) == 0:
			print("reached the end")
		else:
			for the_move in self.moves:
				the_move.traverse(print_helper)


class move_combinations:
	def __init__(self, deck):
		self.first_moves = {}
		self.deck = deck
		
	def adding_first_moves(self):
		for i in range(len(self.deck)):
			self.first_moves[i] = move(self.deck[i], i)
			self.adding_rest_of_the_moves(self.deck, self.first_moves[i])



	def adding_rest_of_the_moves(self, currnet_deck, current_move):
		if len(currnet_deck) == 0:
			None
			#print("cards finished")
		else:
			#print(current_move.move)
			index_of_current_move = None
			for i in range(len(currnet_deck)):
				if current_move.move == currnet_deck[i] and index_of_current_move == None:
					index_of_current_move = i
					continue
				current_move.add_next_move(move(currnet_deck[i], i))
				
			currnet_deck.pop(index_of_current_move)
			for next_move in current_move.moves:
				self.adding_rest_of_the_moves(currnet_deck, next_move)
			currnet_deck.insert(index_of_current_move, current_move.move)
			
	def traverse_everything(self):
		for current_move in self.first_moves:
			self.first_moves[current_move].traverse()


#####___DANGER ZONE DON'T ACTIVATE__ (Unless you have a stronger computer or just want to have fun watching you computer froze)
#####___ The specs I used that wasn't capable of running the program were:
##### Proccesor: Intel® Core™ i5-4690K CPU @ 3.50GHz (4-cores/4-threds)
##### Memory: 16GB 1333MHz (4x4GB)

#massive_tree_with_card_game_move_combinations = move_combinations(decks["Shit"])
#massive_tree_with_card_game_move_combinations.adding_first_moves()
#massive_tree_with_card_game_move_combinations.traverse_everything()
