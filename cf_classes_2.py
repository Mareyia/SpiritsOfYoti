#from cf_list_dicts import decks


#entity is a class represends either the player or the computer
class Entity:
	def __init__(self, character, starting_position, npc=False):
		self.character = character
		self.position = starting_position
		self.position.entity_ocupation = self
		self.npc = npc
	
	def __repr__(self):
		return self.character
	
	def change_potition(self, new_position):
		self.position.entity_ocupation = None
		self.position = new_position
		self.position.entity_ocupation = self
	
	def remove_from_any_position(self):
		self.position.entity_ocupation = None
		self.position = None



#possitions refers to all the available places an entity can move to, the roads and the parts of the roads
class Possition:
	def __init__(self, identity, type_of, location, autofill_roads=True):
		self.identity = identity
		#there are 3 types of possitions, the available square for the player/npc, the roads that connects them and the road parts that composes each rode
		self.type_of = type_of
		#depends on the type, location will be a list of two elements, a x and y axis in case of road parts and squarres and whole square classes in case of roads
		self.location = location
		#distance is the total number of road parts that connects two locations. this will be used for the recommendation part (find for the computer the faster way to reach the player)
		self.distance = 0
		self.destinacions = {}
		self.alailable_destinacions = []
		self.entity_ocupation = None
		self.autofill_roads =  autofill_roads
		#if position is a road and you don't want to manually add its parts it can happen automatically autoffilling the map distance
		if self.type_of == "road":
			for loc_1 in location:
				loc_1.add_roads(self)
				for loc_2 in location:
					if loc_1 != loc_2:
						loc_1.alailable_destinacions.append(loc_2)
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
						self.destinacions[copy_of_distance] = Possition("RP_"+str(copy_of_distance), "road_part", [location_A_postion_x, location_A_postion_y])
						copy_of_distance -= 1
						x_distance -= 1
						if x_distance > 0:
							location_B_postion_x += 1
							self.destinacions[copy_of_distance] = Possition("RP_"+str(copy_of_distance), "road_part", [location_B_postion_x, location_B_postion_y])
							copy_of_distance -= 1
							x_distance -= 1
					if y_distance > 0:
						location_A_postion_y -= 1
						self.destinacions[copy_of_distance] = Possition("RP_"+str(copy_of_distance), "road_part", [location_A_postion_x, location_A_postion_y])
						copy_of_distance -= 1
						y_distance -= 1
						if y_distance > 0:
							location_B_postion_y += 1
							self.destinacions[copy_of_distance] = Possition("RP_"+str(copy_of_distance), "road_part", [location_B_postion_x, location_B_postion_y])
							copy_of_distance -= 1
							y_distance -= 1

					if x_distance < 0:
						location_A_postion_x += 1
						self.destinacions[copy_of_distance] = Possition("RP_"+str(copy_of_distance), "road_part", [location_A_postion_x, location_A_postion_y])
						copy_of_distance -= 1
						x_distance += 1
						if x_distance < 0:
							location_B_postion_x -= 1
							self.destinacions[copy_of_distance] = Possition("RP_"+str(copy_of_distance), "road_part", [location_B_postion_x, location_B_postion_y])
							copy_of_distance -= 1
							x_distance += 1
					if y_distance < 0:
						location_A_postion_y += 1
						self.destinacions[copy_of_distance] = Possition("RP_"+str(copy_of_distance), "road_part", [location_A_postion_x, location_A_postion_y])
						copy_of_distance -= 1
						y_distance += 1
						if y_distance < 0:
							location_B_postion_y -= 1
							self.destinacions[copy_of_distance] = Possition("RP_"+str(copy_of_distance), "road_part", [location_B_postion_x, location_B_postion_y])
							copy_of_distance -= 1
							y_distance += 1

	def __repr__(self):
		return self.type_of[0].upper() + self.type_of[1:] + " " + self.identity
	
	def __lt__(self, other):
		return self.distance < other.distance
	
	def add_roads(self, road):
		self.destinacions[road.identity] = road
	
	def add_road_parts(self, road_part):
		self.destinacions[road_part.identity] = road_part
		self.distance += 1
	
	def get_path(self, location):
		road_to_use = None
		for connected_road in self.destinacions:
			for connected_location in self.destinacions[connected_road].location:
				if connected_location == location:
					road_to_use = self.destinacions[connected_road]
					return road_to_use



#the "graphical interface with x and y axis to insert the map"
class Playing_grid:
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
		if square.type_of == "road_part":
			square_string = "<>"
		if square.entity_ocupation is not None:
			square_string = square.entity_ocupation.character
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


#the map of the game together with the functionality to interact with it
class The_map:
	def __init__(self, playing_area):
		self.playing_area = playing_area
		self.locations = []
		self.roads = []
		self.entities = []
	
	def __repr__(self):
		return self.playing_area.__repr__()
		
	def add_location(self, location):
		self.locations.append(location)
		
	def add_road(self, road):
		self.roads.append(road)
	
	def add_entity(self, entity):
		self.entities.append(entity)
	
	def create_map(self):
		for road in self.roads:
			self.playing_area.fill_the_road(road)
		for location in self.locations:
			self.playing_area.add_position(location)
	
	def update_map(self, position=None):
		if position is not None:
			self.playing_area.add_position(self.locations[position])
		else:
			for location in self.locations:
				self.playing_area.add_position(location)
				
	def move_entity(self, entity, position):
		entity.change_potition(position)
		self.update_map()
	
	def remove_entity(self, entity):
		entity.remove_from_any_position()
		self.entities.remove(entity)
		self.update_map()
























##### Below lies two classes with methods that creates a massive tree with millions of nodes that represents all the card combinations that can happen; with the perpose of making an ultimate difficulty for the computer that will know exactly what will be the best move in any case.
##### The creation and traversing of this tree even with less than 12 cards is enouph to fill 16gb of ram and freeze the computer, so this methode is not recomended and further development has been terminated.

class Move:
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


class Move_combinations:
	def __init__(self, deck):
		self.first_moves = {}
		self.deck = deck
		
	def adding_first_moves(self):
		for i in range(len(self.deck)):
			self.first_moves[i] = Move(self.deck[i], i)
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

#massive_tree_with_card_game_move_combinations = Move_combinations(decks["Shit"])
#massive_tree_with_card_game_move_combinations.adding_first_moves()
#massive_tree_with_card_game_move_combinations.traverse_everything()
