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


combination1 = combinations()

copy_deck = []
for card in decks["Firefly"]:
	copy_deck.append(card)

for i in range(len(decks["Firefly"])):
	combination1.moves.append(move(decks["Firefly"][i]))
	for j in range(len(decks["Firefly"])):
		if i == j:
			continue
		combination1.moves[i].add_move(decks["Firefly"][j])

combination1.traverse()

def a_combinations_for_each_card(deck):
	current_card = self.moves[i]
	
