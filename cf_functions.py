import time
from cf_list_dicts import decks, attacker_message, ton_of_space, instructions
from cf_classes import Card, Player
from random import randint
from cf_functions_2 import lets_move, npc_move, condition_for_endgame, end_game_message, team_balance_check
from cf_classes_2 import Entity


# here the game starts and ends if any player reaches 0 hp. *The start_turn function returns a bool that changes if the upper condition changes.
def playGame(game_mode, difficulty_of_campaign=None, players_and_positions=None, map_inputed=None):
	#players is an array of every player, every player has a list of two classes, 0 for the card fight and 1 for the map movement
	A_map = map_inputed
	players = {}
	teams = {}
	player_names = []
	

	#if game mode is campaign
	if game_mode.previous_menu.menu_sub_title == 'Campaing':
		teams[1] = []
		teams[2] = []
		for player in players_and_positions:
			if player == 1:
				players["Player " + str(player)] = [set_up(player, player_names), Entity(str(player), A_map.locations[players_and_positions[player]], 1)]
				teams[1].append(players["Player " + str(player)])
			else:
				players["Player " + str(player)] = [computer_set_up(player, player_names), Entity(str(player), A_map.locations[players_and_positions[player]], 2, True)]
				teams[2].append(players["Player " + str(player)])
				#players["Player " + str(player)][0].hp = 1
			A_map.add_entity(players["Player " + str(player)][1])
			player_names.append(players["Player " + str(player)][0].player_name)

	#if game mode is costum
	elif game_mode.previous_menu.previous_menu.menu_sub_title == 'Custom Match':
		if game_mode.previous_menu.menu_title == 'All vs All':
			 
			for player in players_and_positions:
				teams[player] = []
				is_computer = input("Player {} is a computer? (y/n): ".format(player))
				while is_computer.lower() not in ['y', 'n']:
					is_computer = input("Wrong input, try again. Player {} is a computer? (y/n): ".format(player))
				if is_computer == 'y':
					players["Player " + str(player)] = [computer_set_up(player, player_names), Entity(str(player), A_map.locations[players_and_positions[player]], player, True)]
					teams[player].append(players["Player " + str(player)])
				else:
					players["Player " + str(player)] = [set_up(player, player_names), Entity(str(player), A_map.locations[players_and_positions[player]], player)]
					teams[player].append(players["Player " + str(player)])
				A_map.add_entity(players["Player " + str(player)][1])
				player_names.append(players["Player " + str(player)][0].player_name)
		
		elif game_mode.previous_menu.menu_title == 'Players vs Computers':
			teams[1] = []
			teams[2] = []
			for player in players_and_positions:
				is_computer = input("Player {} is a computer? (y/n): ".format(player))
				while is_computer.lower() not in ['y', 'n']:
					is_computer = input("Wrong input, try again. Player {} is a computer? (y/n): ".format(player))
				
				#safe measure in case a player puts all players in one team
				is_computer = team_balance_check(is_computer, teams, player, players_and_positions, to_continue, 'Players vs Computers')
				
				if is_computer == 'y':
					players["Player " + str(player)] = [computer_set_up(player, player_names), Entity(str(player), A_map.locations[players_and_positions[player]], 2, True)]
					teams[2].append(players["Player " + str(player)])
				else:
					players["Player " + str(player)] = [set_up(player, player_names), Entity(str(player), A_map.locations[players_and_positions[player]], 1)]
					teams[1].append(players["Player " + str(player)])
				A_map.add_entity(players["Player " + str(player)][1])
				player_names.append(players["Player " + str(player)][0].player_name)
		
		else:
			how_many_teams = 2
			if len(players_and_positions.keys()) > 2:
				how_many_teams = input("In how many teams the players are devided?: ")
				while int(how_many_teams) < 2 or int(how_many_teams) > len(players_and_positions.keys()) or how_many_teams.isdigit() is False:
					how_many_teams = input("Incorrect input, try again. In how many teams the players are devided? (type from 3 to {}): ".format(how_many_players))

			for i in range(1, int(how_many_teams) + 1):
				teams[i] = []
			for player in players_and_positions:
				is_computer = input("Player {} is a computer? (y/n): ".format(player))
				while is_computer.lower() not in ['y', 'n']:
					is_computer = input("Wrong input, try again. Player {} is a computer? (y/n): ".format(player))
							
				for team in teams:
					print("Team number {} with players: {}".format(team, [p[0].player_name for p in teams[team]]))
				which_team = input("Select a team for Player {} (select a team from 1 to {}): ".format(player, how_many_teams))
				while which_team not in [str(n) for n in range(1, int(how_many_teams) + 1)]:
					which_team = input("Wrong input, try again. Player {} will be in team: (select a team from 1 to {}): ".format(i, how_many_teams))
				
				#safe measure in case a player puts all players in one team
				which_team = team_balance_check(int(which_team), teams, player, players_and_positions, to_continue)
					
				if is_computer == 'y':
					players["Player " + str(player)] = [computer_set_up(player, player_names), Entity(str(player), A_map.locations[players_and_positions[player]], which_team, True)]
					teams[which_team].append(players["Player " + str(player)])
				else:
					players["Player " + str(player)] = [set_up(player, player_names), Entity(str(player), A_map.locations[players_and_positions[player]], which_team)]
					teams[which_team].append(players["Player " + str(player)])
				A_map.add_entity(players["Player " + str(player)][1])
				player_names.append(players["Player " + str(player)][0].player_name)

	#if instructions were selected
	else:
		print(instructions)
		return
	
	
	
	print("")
	for player in players: 
		print(players[player][0])
	A_map.create_map()
	print("")

	#Since I am adding multyple players the condition for this will change
	game_end = False
	while game_end == False:
		game_end = actuall_turn(players, teams, A_map, game_mode.previous_menu)
	A_map.reset_map()
	to_continue()


def actuall_turn(all_player, all_teams, the_map_given, the_game_mode):
	the_alive_teams = condition_for_endgame(all_teams)
	for one_player in all_player:
		#all_player[one_player][1].reset_movement() #Reset movement here if the movement will get reseted every turn
		print(all_player[one_player][1])
		if len(the_alive_teams.keys()) == 1:
			print(end_game_message(the_alive_teams, the_game_mode))
			return True
		if all_player[one_player][1] in the_map_given.entities:
			
			#Death check 1
			death, empty_hand = all_player[one_player][0].check_status()
			if death:
				print(all_player[one_player][0], "died!")
				#remove the player
				if all_player[one_player][1].position:
					the_map_given.remove_entity(all_player[one_player][1])
					#number_of_alive_player -= 1
					the_alive_teams = condition_for_endgame(all_teams, all_player[one_player])
				continue
			choose_your_action = None
			action = 1
			#in case a player dies in its own turn
			if death:
				action = 3
				
			#The two actions of each players turn
			while action != 3:
				all_player[one_player][1].reset_movement() #Reset movement here if the movement will get reseted every action
				#find the adjecent entities for both npcs and players
				adjecent_to_entity = []
				adjecent_enemies = []
				adjecent_alies = []
				adjecent_positions = []
				for destination in all_player[one_player][1].position.alailable_destinacions:
					if destination.entity_ocupation != None:
						adjecent_to_entity.append(destination.entity_ocupation)
						if destination.entity_ocupation.team != all_player[one_player][1].team:
							adjecent_enemies.append(destination.entity_ocupation)
						else:
							adjecent_alies.append(destination.entity_ocupation)
					else:
						adjecent_positions.append(destination)


				if all_player[one_player][0].computer == True:
					print(the_map_given)
					print("{} action {}: Choosing an action".format(all_player[one_player][0].player_name, action))
					to_continue(3)
					if len(adjecent_enemies) == 0:
						while len(adjecent_positions) > 0 and all_player[one_player][1].movement >= min([all_player[one_player][1].position.get_path(destination).distance for destination in all_player[one_player][1].position.alailable_destinacions if destination.entity_ocupation == None]) and len(adjecent_enemies) == 0:
							npc_move(all_player[one_player][1], the_map_given)
							#need to stop the while loop if there is an adjent is found enemy before the movemnt is not enouf
							adjecent_enemies = [destination.entity_ocupation for destination in all_player[one_player][1].position.alailable_destinacions if destination.entity_ocupation != None and destination.entity_ocupation.team != all_player[one_player][1].team]
							
							print(the_map_given)
						if len(adjecent_positions) == 0:
							print("Nowere to move...")
						to_continue(1)
					elif len(adjecent_enemies) == 1:
						start_turn(all_player[one_player][0], all_player["Player " + str(adjecent_enemies[0].character)][0])
					else:
						start_turn(all_player[one_player][0], all_player["Player " + str(adjecent_enemies[randint(0, len(adjecent_enemies) - 1)].character)][0])
				else:
					print(the_map_given)
					available_options = []
					for i in range(len(all_player[one_player][1].position.alailable_destinacions)):
						if all_player[one_player][1].position.alailable_destinacions[i].entity_ocupation is not None:
							continue
						available_options.append(str(i))
					
					choose_your_action = '0'
					#if all_player[one_player][1].movement < min([destination for destination in all_player[one_player][1].position.alailable_destinacions if destination.entity_ocupation == None]):
						
					#if there are no locations available to move, it also means that you are surronded by entities
					if len(available_options) > 0:
						#if there are no enemies to attack means there are only location to go too and freendly entities adjecent to you
						if empty_hand and choose_your_action != '1':
							choose_your_action = '1'
							print("Cannot attack with no cards\nAction {}.".format(action))
						if len(adjecent_enemies) == 0 and choose_your_action != '1':
							choose_your_action = '1'
							print("No enemies around to attack\nAction {}.".format(action))
						if len(adjecent_enemies) > 0 and choose_your_action != '1':
							choose_your_action = input("{}\nYou are at {} (x={}, y={})\nAction {}. Do you want to move or attack? 1/2: ".format(all_player[one_player][0].player_name, all_player[one_player][1].position, all_player[one_player][1].position.location[0], all_player[one_player][1].position.location[1], action))
							while choose_your_action not in ['1', '2']:
								choose_your_action = input("Wrong input trty again: ")
					else:
						choose_your_action = '2'
						print("You are surrounded, can't move!\nAction {}.".format(action))
					
					

						 
					if choose_your_action == '1':
						continue_moving = True
						while all_player[one_player][1].movement >= min([all_player[one_player][1].position.get_path(destination).distance for destination in all_player[one_player][1].position.alailable_destinacions if destination.entity_ocupation == None]) and continue_moving:
							continue_moving = lets_move(all_player[one_player][1], the_map_given)
						print("No movement left")
					else:
						for i in range(1, len(adjecent_enemies) + 1):
							print("Type '{}' for {} in {} at {}".format(i, all_player["Player " + str(adjecent_enemies[i - 1])][0].player_name, adjecent_enemies[i - 1].position, adjecent_enemies[i - 1].position.location)) 
						choose_your_enemy = input("Who do you want to attack?: ")
						while choose_your_enemy not in [str(num_of_option) for num_of_option in range(1, len(adjecent_enemies) + 1)]:
							 choose_your_enemy = input("Invalid option, try again: ")
						start_turn(all_player[one_player][0], all_player["Player " + str(adjecent_enemies[int(choose_your_enemy) - 1].character)][0])
				action += 1
				
				#Death check 2
				for every_player in all_player:
					death_check_2, empty_hand_check_2 = all_player[every_player][0].check_status()
					if death_check_2:
						print(all_player[every_player][0], "died!")
						if every_player == one_player:
							death = death_check_2
						#remove the player
						if all_player[every_player][1].position:
							the_map_given.remove_entity(all_player[every_player][1])
							#number_of_alive_player -= 1
							the_alive_teams = condition_for_endgame(all_teams, all_player[every_player])
				if len(the_alive_teams.keys()) == 1:
					print(end_game_message(the_alive_teams, the_game_mode))
					return True
				#in case a player dies in its own turn
				if death:
					action = 3
	return False



# a helpfull function inbetwin inputs and prints to not output everything all together and creating chaos to the terminal
## upgraded to continue automaticaly, less types
def to_continue(auto_or_manual=0):
	finishedreading = input("Type anything to continue: ")
	"""
	if auto_or_manual == 0:
		finishedreading = input("Type anything to continue: ")
	else:
		time_to_wait = auto_or_manual
		#waiting_message = ""
		for i in range(time_to_wait):
			#waiting_message += "."
			print(end="\r")
			time.sleep(1)#"""


# function that will get repeated for each plater, accepts the number corresponting to the current player and return a completed player object with randomized deck, name, hand and hp
def set_up(whos_turn, player_names_list):
	#recive the name from the player
	name = input("\nPlayer {} how do you want to be called?: ".format(whos_turn))
	while name in player_names_list:
		name = input("Another player already has this name, pick a difrent one: ")
	print("\nHello {}!!!".format(name))

	#upgrade can now add more decks by just adding them on the cf_list_dicks
	print("\nNow pick a deck\n")
	for i in range(len(list(decks.keys()))):
		print("	{}: '{}'".format(i+1, list(decks.keys())[i]))
	print("\nor 'l' to list every card on each deck")

	#recieve the choise of deck from the player 
	deck_selection = input("Type here: ")
	while deck_selection not in [str(i+1) for i in range(len(list(decks.keys())))]:
		if deck_selection == 'l':
			for deck in decks:
				print("\n\t'{}':".format(deck))
				for card in decks[deck]:
					print(card)
			deck_selection = input("Type here: ")
		else:
			deck_selection = input("Invalid input, type again: ")
	current_player =  Player(name, list(decks[list(decks.keys())[int(deck_selection)-1]]), list(decks.keys())[int(deck_selection)-1], whos_turn)


	#randomize the deck
	current_player.randomize()

	#draw 3 cards
	current_player.draw_cards()

	return current_player

#pretty much the hole game happens here
def start_turn(current_player, enemy_player):
	#draw cards from their decks for boths players until the have 3 on hand
	current_player.draw_cards()
	enemy_player.draw_cards()

	if not current_player.computer and not enemy_player.computer:
		#some time for the players to see who playes
		to_continue(3)
		#print(ton_of_space)
	#checks if any player reaced 0 hp so the game will end
	condition, cards_finished = current_player.check_status()
	
	# some time to read the players information
	to_continue(4)
	if condition:
		print("""\n\n{} died!

===================================================
!!!!!	------>> {} YOU WIN!
===================================================\n""".format(current_player.player_name, enemy_player.player_name))
		#return True				#with this the hole game needs to ends
	else:
		#in case there are no cards left
		if cards_finished:
			if current_player.hp < enemy_player.hp:
				print("""\n\nno cards left and {} has less hp!

===================================================
!!!!!	------>> {} YOU WIN!
===================================================\n""".format(current_player.player_name, enemy_player.player_name))
				#return True				#with this the hole game needs to ends
			elif current_player.hp > enemy_player.hp:
				print("""\n\nno cards left and {} has less hp!

===================================================
!!!!!	------>> {} YOU WIN!
===================================================\n""".format(enemy_player.player_name, current_player.player_name))
				#return True				#with this the hole game needs to ends
			else:
				print("\n\nno cards left and you have the same hp...\n\tIts a fucking draw!\n")
				#return True				#with this the hole game needs to ends

		#check if the player is the computer
		if current_player.computer:
			card_selected_attacking, replacing = computer_pick_a_card(current_player, enemy_player, True)
		else:
			#asks players to pick a card to play or to replace
			card_selected_attacking, replacing = pick_a_card(current_player, enemy_player, True)
			
		if replacing:
			#when replacing nothing else happens
			replace_card(current_player, card_selected_attacking)
		elif card_selected_attacking == None:
			print("{} had no available cards and loses its turn".format(current_player.player_name))
		else:
			#if not replacing the other player has to pick a card too and the cards fight
			if enemy_player.computer:
				card_selected_defending, not_needed = computer_pick_a_card(enemy_player, current_player, False)
			else:
				card_selected_defending, not_needed = pick_a_card(enemy_player, current_player, False)
			if not current_player.computer and not enemy_player.computer:
				print(ton_of_space)
			fight(current_player, card_selected_attacking, enemy_player, card_selected_defending)
			
			# some time to watch the result of the fight
			if not current_player.computer and not enemy_player.computer:
				to_continue(3)
			else:
				to_continue(3)
		#return False

#ask each player to pick a card
def pick_a_card(current_player, enemy_player, initiative):
	need_replacement = False				#on/of if the player wants to replace a card
	if not enemy_player.computer:
		print("{}{} is about to pick a card {} don't look!".format(ton_of_space, current_player.player_name, enemy_player.player_name))
		to_continue()
	#for#testing#print("{} is about to pick a card {} don't look!".format(current_player.player_name, enemy_player.player_name))
	if not current_player.computer and not enemy_player.computer:
		print("\nHP: {}, cards left on deck: {}\n".format(current_player.hp, len(current_player.ready_deck)))
	display_hand_first, display_hand_second, valid_options_total, valid_options_no_r_first, valid_options_no_r_second = show_hand(current_player.hand, initiative)
	#valid_options_total for ssafety measure1 if the replacing option selected
	#initiative: checks to see if the current_player is in the attack
	if initiative:

		#valid_options_no_r_first for ssafety measure2 
		print(display_hand_first) #shows hand
		if len(valid_options_no_r_first) == 0 and len(current_player.deck) == 0:
			print("No available card to select")
			card_selection = None
			to_continue(2)
		else:
			card_selection = input("Pick a/an card/option here: ")

			#safety measure0, if player types something wrong or r
			while card_selection not in valid_options_no_r_first:

				#in case the player wants to replace a card
				if card_selection == 'r':
					card_selection = input("Pick a card to replace: ")
					need_replacement = True
				
					#safety measure1, if player types something wrong
					while card_selection not in valid_options_total:
						print("Invalid option")
						card_selection = input("Type again: ")
					break

				#player doesn't want to replace any card
				else:
					
					if card_selection in valid_options_total:
						#safety measure2, if player attemps to pick an invalid card
						if current_player.hand[int(card_selection) - 1].type_of_card == "block":
							print("Cannot play a defenfing (BLOCK-type) card on your initiative")
							card_selection = input("Pick again: ")
					#resolution of measure0
					else:
						print("Invalid option")
						card_selection = input("Type again: ")

	#this function will continue with else when current player is the defending player 
	else:
		print("current hp: {}".format(current_player.hp))
		print(display_hand_second)

		#if there are no available cards to defend with
		if len(valid_options_no_r_second) == 0:
			print("No available card to select")
			card_selection = None
			to_continue(2)
		else:
			card_selection = input("Pick a card here: ")

			#safety measure1, if player types something wrong
			#valid_options_no_r_second for safety measure2 
			while card_selection not in valid_options_no_r_second:

				#safety measure2, if player attemps to pick an invalid card
				if card_selection in valid_options_total:
					if current_player.hand[int(card_selection) - 1].type_of_card == "attack":
						print("Cannot play an attacking (ATTACK-type) card on your oponment's initiative")
						card_selection = input("Pick again: ")
				#resolution of measure1
				else:
					print("Invalid option")
					card_selection = input("Type again: ")

	#picking the card
	if card_selection !=None:
		card_selection = current_player.hand[int(card_selection) - 1]
		#if no card is going to replaced and a card was available to pick, the chosen card needs to be removed from the hand for the game to progress
		if not need_replacement:
			current_player.remove_card(card_selection)
	return card_selection, need_replacement


#function that replace the selected card with a random one from the deck
def replace_card(player_choosed_to_replace, card_to_replace):
	if len(player_choosed_to_replace.ready_deck) > 0:
		random_new_card_place = randint(0, len(player_choosed_to_replace.ready_deck)-1)
		player_choosed_to_replace.hand.append(player_choosed_to_replace.ready_deck.pop(random_new_card_place))
		player_choosed_to_replace.ready_deck.insert(random_new_card_place, card_to_replace)
		player_choosed_to_replace.hand.remove(card_to_replace)
		print("\nReplaced: {}\n".format(card_to_replace))
	else:
		print("No cards left")


#CARDFIGHT! here is the function that applies the name of the game! The two card objects are getting compared and the result of the comparison modifies the player objects 
def fight(attacking_player, attacking_card, defending_player, defending_card):	
	if attacking_card.type_of_card == "attack" or attacking_card.type_of_card == "balander":
		attacking_card.attacking(attacking_player, defending_card, defending_player)
	elif attacking_card.name_of_card == "Drinking ouiski":
		attacking_card.healing(attacking_player, defending_card, defending_player)
	else: #if .name_of_card() == "Magical web"
		attacking_card.canceling(attacking_player, defending_card, defending_player)


#show_hand customize the print statement, when its time to show the 3 hands of its player, depending on the players position(attacker, diffender) and player number of cards(in case deck is empty and hand is forced to be reduced lower than 3)
def show_hand(players_hand, player_initiative):
	if player_initiative:
		print("\nYou are ATTACKING")
	else:
		print("\nYou are DEFENDING")
	show_cards_1 = "Now pick a card:\n\n"
	valid_options = []
	valid_options_no_r_1 = []
	valid_options_no_r_2 = []
	for i in range(len(players_hand)):
		#creating these nessery lists to return for the pick_card's safety measures to work
		valid_options.append(str(i+1))
		if players_hand[i].type_of_card != "block":
			valid_options_no_r_1.append(str(i+1))
		if players_hand[i].type_of_card != "attack":
			valid_options_no_r_2.append(str(i+1))
		#costomising the print statement dependent on the number of cards on hand
		show_cards_1 += "	{}:	{}\n".format(i+1, players_hand[i])
	show_cards_1 += "\n"
	
	show_cards_2 = show_cards_1
	#if the player is the attacking one there should be outputed an option for replace
	show_cards_1 += attacker_message

	return show_cards_1, show_cards_2, valid_options, valid_options_no_r_1, valid_options_no_r_2









#### NPC FUNCTIONS


#copy of pick_a_card for computer
def computer_pick_a_card(current_player, enemy_player, initiative):
	need_replacement = False				#on/of if the player wants to replace a card
	print("{} is picking a card...".format(current_player.player_name))
	to_continue(1)

	valid_options_no_r_first, valid_options_no_r_second = computer_hand(current_player.hand, initiative, current_player.hp, len(current_player.ready_deck))

	if initiative:
		#valid_options_no_r_first for computer attacking options 
		if len(current_player.ready_deck) == 0:
			if len(valid_options_no_r_first) == 0:
				card_selection = None
			else:
				card_selection = valid_options_no_r_first[randint(0, len(valid_options_no_r_first)-1)]
		else:
			want_r = randint(0, 9)
			#the chanses of choosing to replace a card (want_r<2 = 20%)
			if len(valid_options_no_r_first) == 0 or want_r < 2:
				need_replacement = True
				card_selection = current_player.hand[randint(0, len(current_player.hand)-1)]
			else:
				#picking the card
				card_selection = valid_options_no_r_first[randint(0, len(valid_options_no_r_first)-1)]



	#this function will continue with else when current player is the defending player 
	else:
		if not current_player.computer:
			print("current hp: {}".format(current_player.hp))

		#valid_options_no_r_second for computer defending options 
		#if there are no available cards to defend with
		if len(valid_options_no_r_second) == 0:
			card_selection = None
		else:
			#picking the card
			card_selection = valid_options_no_r_second[randint(0, len(valid_options_no_r_second)-1)]

	if card_selection !=None:
		if not need_replacement:
			current_player.remove_card(card_selection)
	#TEST#print("\nComputer picked: {}\n".format(card_selection))
	return card_selection, need_replacement



#copy of show_hand for computer
def computer_hand(players_hand, player_initiative, players_hp, cards_left_ondeck):
	valid_options_no_r_1 = []
	valid_options_no_r_2 = []
	for card in players_hand:
		#available attacking cardds for computer
		if card.type_of_card != "block":
			#forr computer to not use the healing card if its not required
			if card.name_of_card == "Drinking ouiski":
				if players_hp <= 7 or cards_left_ondeck == 0:
					valid_options_no_r_1.append(card)
			else:
				valid_options_no_r_1.append(card)
		#available ddefending cardds for computer
		if card.type_of_card != "attack":
			valid_options_no_r_2.append(card)
				
	#STARTTEST#print("\n\nComputer Hand:")
	#for card in players_hand:
	#	print(card)
	#print("\nAvailable ATTAcking options:")
	#for card in valid_options_no_r_1:
	#	print(card)
	#print("\nAvailable DEFFending options:")
	#for card in valid_options_no_r_2:
	#ENDTEST#	print(card)


	return valid_options_no_r_1, valid_options_no_r_2
	
	
	
	
#copy of setup for computer
def computer_set_up(whos_turn, player_names_list):
	#recive the name for the computer
	name = input("\nPlayer {} is a computer! Do you want to give it a name?\n(if not leave blank and press ENTER it will be called 'Computer (n)'): ".format(whos_turn))
	if name == "":
		name = "Computer"
		computer_number = 1
		while name in player_names_list:
			computer_number += 1
			name = "Computer"
			name += " " + str(computer_number)
	while name in player_names_list:
		name = input("Another player already has this name, pick a difrent one: ")

	#upgrade can now add more decks by just adding them on the cf_list_dicks
	print("\nNow pick a deck for the computer")
	for i in range(len(list(decks.keys()))):
		print("	{}: '{}'".format(i+1, list(decks.keys())[i]))
	print("\nor 'l' to list every card on each deck")

	deck_selection = input("(Or if you want the computer to pick one for itself leave blank and press ENTER: ")
	#recieve the choise of deck from the player for the coomputer
	while deck_selection not in [str(i+1) for i in range(len(list(decks.keys())))] and deck_selection != "":
		if deck_selection == 'l':
			for deck in decks:
				print("\n\t'{}':".format(deck))
				for card in decks[deck]:
					print(card)
			deck_selection = input("Type here: ")
		else:
			deck_selection = input("Invalid input, type again: ")
	#allow the computer to pick for it self
	if deck_selection == "":
		deck_selection = randint(0, len(list(decks.keys()))-1)


	current_player =  Player(name, list(decks[list(decks.keys())[int(deck_selection)-1]]), list(decks.keys())[int(deck_selection)-1], whos_turn, True)

	#randomize the deck
	current_player.randomize()

	#draw 3 cards
	current_player.draw_cards()

	return current_player
