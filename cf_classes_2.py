from cf_list_dicts import decks




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
