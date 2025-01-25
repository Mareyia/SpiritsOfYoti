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
		return "'{}' card of {}-type ".format(self.name_of_card, self.type_of_card.upper()) + card_representation


	def attacking(self, attacker, defender_card, defender_player):
		if defender_card == None:
			print("{} used '{}' to deal {} damage! ---> {} had no available card!".format(attacker.player_name, self.name_of_card, self.ability_score, defender_player.player_name))
			defender_player.hp -= self.ability_score
			if defender_player.hp < 0:
					defender_player.hp = 0
			print("{} recieved all the damage! {}'s hp: {}".format(defender_player.player_name, defender_player.player_name, defender_player.hp))
		#case a
		elif defender_card.type_of_card == "block" or defender_card.type_of_card == "balander":
			print("{} used '{}' to deal {} damage! ---> {} used '{}' to block {} damage!".format(attacker.player_name, self.name_of_card, self.ability_score, defender_player.player_name, defender_card.name_of_card, defender_card.ability_score))
			damge_delt = self.ability_score - defender_card.ability_score
			if damge_delt > 0:
				new_defender_hp = defender_player.hp - damge_delt
				if new_defender_hp < 0:
					defender_player.hp = 0
				else:
					defender_player.hp = new_defender_hp
				print("{} recieved {} damage! {} hp: {}".format(defender_player.player_name, damge_delt, defender_player.player_name, defender_player.hp))
			else:
				print("{} blocked all the damage!".format(defender_player.player_name))
		#case b
		elif defender_card.name_of_card == "Drinking ouiski":
			print("{} used '{}' to deal {} damage! ---> but {} used '{}' to heal {} points!".format(attacker.player_name, self.name_of_card, self.ability_score, defender_player.player_name, defender_card.name_of_card, defender_card.ability_score))
			defender_player.hp -= self.ability_score
			defender_player.hp += defender_card.ability_score
			if defender_player.hp > Player.total_hp:
				defender_player.hp = Player.total_hp
			print("{} recieved all the damage but healed imidietly after! {}'s hp: {}".format(defender_player.player_name, defender_player.player_name, defender_player.hp))
		#case c
		elif defender_card.name_of_card == "Magical web":
			print("{} used '{}' to deal {} damage! ---> {} used '{}' and nutrialized the attack!".format(attacker.player_name, self.name_of_card, self.ability_score, defender_player.player_name, defender_card.name_of_card))


	def healing(self, attacker, defender_card, defender_player):
		if defender_card == None:
			attacker.hp += self.ability_score
			if attacker.hp > Player.total_hp:
				attacker.hp = Player.total_hp
			print("{} used '{}' to heal {} points! ---> {} had no available card! {}'s hp: {}".format(attacker.player_name, self.name_of_card, self.ability_score, defender_player.player_name, attacker.player_name, attacker.hp))
		#case d
		elif defender_card.type_of_card == "block" or defender_card.type_of_card == "balander":
			attacker.hp += self.ability_score
			if attacker.hp > Player.total_hp:
				attacker.hp = Player.total_hp
			print("{} used '{}' to heal {} points! ---> {} used '{}' to block, but there was nothing to block! {}'s hp: {}".format(attacker.player_name, self.name_of_card, self.ability_score, defender_player.player_name, defender_card.name_of_card, attacker.player_name, attacker.hp))
		#case e
		elif defender_card.name_of_card == "Drinking ouiski":
			attacker.hp += self.ability_score
			defender_player.hp += defender_card.ability_score
			if attacker.hp > Player.total_hp:
				attacker.hp = Player.total_hp
			if defender_player.hp > Player.total_hp:
				defender_player.hp = Player.total_hp
			print("{} used '{}' to heal {} points! ---> {} also used '{}' to {} points!\n{}'s hp: {}\n{}'s hp: {}".format(attacker.player_name, self.name_of_card, self.ability_score, defender_player.player_name, defender_card.name_of_card, defender_card.ability_score, attacker.player_name, attacker.hp, defender_player.player_name, defender_player.hp))
		#case c
		elif defender_card.name_of_card == "Magical web":
			print("{} used '{}' to heal {} points! ---> {} used '{}' and interupted the healing!".format(attacker.player_name, self.name_of_card, self.ability_score, defender_player.player_name, defender_card.name_of_card))


	def canceling(self, attacker, defender_card, defender_player):
		if defender_card == None:
			print("{} had no cards so {} used '{}' to counter nothing!".format(defender_player.player_name, attacker.player_name, self.name_of_card))
		#case f
		elif defender_card.type_of_card == "block" or defender_card.type_of_card == "balander" or defender_card.name_of_card == "Drinking ouiski":
			print("{} used '{}' to counter {}'s action ---> {} used '{}' but got countered!".format(attacker.player_name, self.name_of_card, defender_player.player_name, defender_player.player_name, defender_card.name_of_card))
		#case g
		elif defender_card.name_of_card == "Magical web":
			print("Both players used '{}' and countered each other!".format(self.name_of_card))


class Player:
	total_hp = 10
	def __init__(self, player_name, deck, deck_key, player_turn, computer=False):
		self.player_name = player_name
		#self.key to keep the key's name from the dictionary and self.deck for the actuall deck from the value *Possibility to do this by importing the dictionary directly from the file without the need of a second seperate class variable to hold the name maybe?
		self.deck = deck						#raw deck from the dictionary, sorted
		self.deck_key = deck_key				#name of the deck using dictionary's key
		#self.initiative = False				#attacking or defnding
		self.player_turn = player_turn			#player1 or player2
		self.ready_deck = []					#cards from the deck in random order 
		self.hand = []							#the 3 available cards for the player to play
		self.hp = self.total_hp
		self.computer = computer
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
		is_dead = False
		no_cards_left = False
		if self.hp <= 0:
			is_dead = True						#that means that the current player is dead
			self.hp = 0
		else:
			if len(self.hand) == 0:
				no_cards_left = True
		print("""
{}
hp: {}
cards left on deck: {}""".format(self, self.hp, len(self.ready_deck)))
		return is_dead, no_cards_left


class Menu_options:
	def __init__(self, menu_title, option_number="", previous_menu=None, menu_sub_title="", title_cosmetics="", sub_title_cosmetics="", activatable=None):
		self.options = {}
		self.menu_title = menu_title
		self.menu_sub_title = menu_sub_title
		if self.menu_sub_title == "":
			self.menu_sub_title = self.menu_title
		self.title_cosmetics = title_cosmetics
		self.sub_title_cosmetics = sub_title_cosmetics
		self.option_number = option_number
		#activatble needs to handle the start of the game
		self.activatable = activatable
		#previous_menu neeeds to handle the exit as-well
		self.previous_menu = previous_menu
	
	def __repr__(self):
		representation = "\n" + self.title_cosmetics + " " + self.menu_title + " " + self.title_cosmetics + "\n"
		if self.menu_sub_title != "" and self.menu_sub_title != self.menu_title:
			representation += "\n" + self.sub_title_cosmetics + " " + self.menu_sub_title + " " + self.sub_title_cosmetics + "\n"
		return representation
	
	def add_option(self, option, option_class):
		self.options[option] = option_class
	
	#returns the numbers for every available menu or sub-menu option
	def get_options(self):
		return [self.options[option].option_number for option in self.options]
	
	def selecting_option(self):
		print(self)
		for option in self.options:
			print(option + " " + self.options[option].menu_title)
		number_of_option = input("\nType here your option and then press enter: ")
		while number_of_option not in self.get_options():
			number_of_option = input("Invalid Input, try again: ")
		return self.options[number_of_option], int(number_of_option)
		
	def difficulty_genaretion(self, user_input, all_maps):
		number_of_players_and_positions = {}
		the_chosen_map = all_maps[user_input]
		#this is the players variable
		number_of_players_and_positions[1] = 7
		number_of_players_and_positions[2] = 0
		number_of_players_and_positions[3] = 1
		number_of_players_and_positions[4] = 2
		dificulty = 'Easy'
		if user_input == 2 or user_input == 3:
			number_of_players_and_positions[5] = 3
			number_of_players_and_positions[6] = 4
			dificulty = 'Normal'
		if user_input == 3:
			number_of_players_and_positions[7] = 5
			number_of_players_and_positions[8] = 6
			dificulty = 'Hard'
		
		
		return dificulty, number_of_players_and_positions, the_chosen_map
	
	def map_selection(self):
		pass
	
	#def activating_option(self):
	#	player_selection = self.selecting_option()
	#	if self.options[0].menu_title == Ex

class All_Menu:
	def __init__(self, starting_menu):
		self.starting_menu = starting_menu
		self.current_menu = starting_menu
	
	def using_menu(self, game_function, all_maps, player_selection=None, player_selection_number=None):
		if self.current_menu == None:
			print("Bye bye hope you had funnnn, or dont... I actually don't really care.")
		else:
			if self.current_menu.activatable == None:
				player_selection, player_selection_number = self.current_menu.selecting_option()
				if player_selection.option_number == '0':
					self.current_menu = self.current_menu.previous_menu
				else:
					self.current_menu = player_selection
			else:
				dificulty_mode, players_and_positions, apropriet_map = self.current_menu.difficulty_genaretion(player_selection_number, all_maps)
				game_function(self.current_menu, dificulty_mode, players_and_positions, apropriet_map)
				self.current_menu = self.starting_menu
			self.using_menu(game_function, all_maps, player_selection, player_selection_number)
	


		
		
