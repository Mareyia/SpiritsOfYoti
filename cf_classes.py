from random import randint

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
		elif self.type_of_card == "balander":
			card_representation = "deals or blocks {} damge.".format(self.ability_score)
		else:
			if self.name_of_card == "Drinking ouiski":
				card_representation = "heals for {} hp.".format(self.ability_score)
			else:
				card_representation = "stops all enemy attacks and abilities."
		return "'{}' card of {}-type ".format(self.name_of_card, self.type_of_card) + card_representation

class Player:
	def __init__(self, player_name, deck, deck_key, player_turn):
		self.player_name = player_name
		#self.key to keep the key's name from the dictionary and self.deck for the actuall deck from the value *Possibility to do this by importing the dictionary directly from the file without the need of a second seperate class variable to hold the name maybe?
		self.deck = deck						#raw deck from the dictionary, sorted
		self.deck_key = deck_key				#name of the deck using dictionary's key
		#self.initiative = False				#attacking or defnding
		self.player_turn = player_turn			#player1 or player2
		self.ready_deck = []					#cards from the deck in random order 
		self.hand = []							#the 3 available cards for the player to play
		self.hp = 10
	def __repr__(self):
		return "Player {}, {} with '{}' deck.".format(self.player_turn, self.player_name, self.deck_key)
	
	
	# randomize is a method that uses the ordered self.deck to add its cards in random order inside the self.ready_deck list
	def randomize(self):
		while len(self.deck) > 0: 
			random_index_of_card = randint(0, len(self.deck)-1)
			self.ready_deck.append(self.deck.pop(random_index_of_card))
			
	# draw three cards to from the randomized deck available for pick
	def draw_cards(self):
		if (len(self.ready_deck)) > 0:
			while len(self.hand) < 3:
				self.hand.append(self.ready_deck.pop())
		# if the deck is empty, the player starts taking damge every turn
		else:
			self.hp -= 1
		
	def remove_card(self, card_selected_to_be_removed):
		if len(self.hand) > 0:
			self.hand.remove(card_selected_to_be_removed)
	
	
	
	#this check needs to be called after the self.hp is possible affected (possible affected from other functions that are changing its value in sertain conditions): draw_cards, 
	def check_status(self):
		print("""
{}'s turn
hp: {}
cards left on deck: {}""".format(self.player_name, self.hp, len(self.ready_deck)))
		if self.hp <= 0:
			return True						#that means that the current player is dead
		return False
	
	
	
	
