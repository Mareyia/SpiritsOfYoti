class Card:
	def __init__(self, name_of_card, type_of_card, ability_score=0):
		self.name_of_card = name_of_card
		self.type_of_card = type_of_card
		self.ability_score = ability_score
	
	def __repr__(self):
		if self.type_of_card == "attack":
			card_representation = "deals {} damage.".format(self.ability_score)
		elif self.type_of_card == "block":
			card_representation = "blocks {} damge.".format(self.ability_score)
		else:
			if self.name_of_card == "Drinking ouiski":
				card_representation = "heals for {} hp.".format(self.ability_score)
			else:
				card_representation = "stops all enemy attacks and abilities."
		return "'{}' card of {}-type ".format(self.name_of_card, self.type_of_card) + card_representation

class Player:
	def __init__(self, player_name, deck, deck_key, initiative):
		self.player_name = player_name
		#self.key to keep the key's name from the dictionary and self.deck for the actuall deck from the value *Possibility to do this by importing the dictionary directly from the file without the need of a class variable maybe?
		self.deck = deck
		self.key = deck_key
		self.initiative = initiative
	def __repr__(self):
		return "Player {}, {} with '{}' deck.".format(self.initiative, self.player_name, self.key)
