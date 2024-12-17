from cf_list_dicts import decks


class entity:
	def __init__(self, character, starting_position, npc=False):
		self.character = character
		self.position = starting_position
		self.npc = npc




class possition:
	def __init__(self, identity, x_axis, y_axis, distance=0, entity_ocupied=None):
		self.identity = identity
		self.location = (x_axis, y_axis)
		self.distance = distance
		self.entity_ocupation = entity_ocupied
		self.roads = {}

	def add_roads(self, road):
		self.roads[road.identity] = road



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


a_map = the_map(25, 17)
A_position = possition("Ak", 11, 9)
B_position = possition("Jk", 10, 4)
C_position = possition("Cf", 3, 13)
D_position = possition("Ko", 5, 7)

A1_road = possition("##", 10, 9)
A2_road = possition("##", 9, 9)
A3_road = possition("##", 8, 9)
A4_road = possition("##", 7, 9)
A5_road = possition("##", 6, 9)
A6_road = possition("##", 6, 8)
A7_road = possition("##", 5, 8)

A_position.add_roads(A1_road)
A1_road.add_roads(A_position)
A1_road.add_roads(A2_road)
A2_road.add_roads(A1_road)
A2_road.add_roads(A3_road)
A3_road.add_roads(A2_road)
A3_road.add_roads(A4_road)
A4_road.add_roads(A3_road)
A4_road.add_roads(A5_road)
A5_road.add_roads(A4_road)
A5_road.add_roads(A6_road)
A6_road.add_roads(A5_road)
A6_road.add_roads(A7_road)
A7_road.add_roads(A6_road)
A7_road.add_roads(D_position)
D_position.add_roads(A7_road)


a_map.add_position(A_position)
a_map.add_position(B_position)
a_map.add_position(C_position)
a_map.add_position(D_position)
a_map.add_position(A1_road)
a_map.add_position(A2_road)
a_map.add_position(A3_road)
a_map.add_position(A4_road)
a_map.add_position(A5_road)
a_map.add_position(A6_road)
a_map.add_position(A7_road)

print(a_map)


























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
