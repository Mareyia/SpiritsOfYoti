from cf_list_dicts import decks

class move:
	def __init__(self, card):
		self.card = card
		self.moves = []
	
	def add_move(self, next_card):
		self.moves.append(next_card)
	
	def traverse(self):
		print(self.card)
		for move in self.moves:
			print(move)


class combinations:
	def __init__(self):
		self.moves = []
		
	def traverse(self):
		for move in self.moves:
			move.traverse()




	copy_deck = []
	for card in decks["Firefly"]:
		copy_deck.append(card)

	def creat_comb(self, deck):
		for i in range(len(deck)):
			copy_deck = []
			for card in deck:
				copy_deck.append(card)
				
			self.moves.append(copy_deck.pop())
			for card in copy_deck:
				self.moves[i].add_move(deck[j])

combination1 = combinations()
combination1.traverse()


def a_combinations_for_each_card(deck):
	current_card = self.moves[i]
	
