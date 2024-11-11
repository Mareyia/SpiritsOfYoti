import time
from cf_list_dicts import decks, attacker_message, ton_of_space
from cf_classes import Card, Player
from random import randint


# here the game starts and ends if any player reaches 0 hp. *The start_turn function returns a bool that changes if the upper condition changes.
def playGame(computerPlay):
	if computerPlay:
		who_playes_first = input("Do you want to play first or second?\nType here '1' for first or '2' for second: ")
		while who_playes_first not in ['1', '2']:
			who_playes_first = input("Invalid pick again: ")
		if who_playes_first == '1':
			player_1 = set_up(1)
			player_2 = computer_set_up(2, player_1.player_name)
		else:
			player_1 = computer_set_up(1)
			player_2 = set_up(2, player_1.player_name)
	else:
		player_1 = set_up(1)
		player_2 = set_up(2, player_1.player_name)
	print("")
	print(player_1)
	print(player_2)
	print("")

	game_end = False
	while not game_end:
		game_end = start_turn(player_1, player_2)
		if not game_end:
			game_end = start_turn(player_2, player_1)
	to_continue()



# a helpfull function inbetwin inputs and prints to not output everything all together and creating chaos to the terminal
## upgraded to continue automaticaly, less types
def to_continue(auto_or_manual=0):
	if auto_or_manual == 0:
		finishedreading = input("Type anything to continue: ")
	else:
		time_to_wait = auto_or_manual
		#waiting_message = ""
		for i in range(time_to_wait):
			#waiting_message += "."
			print(end="\r")
			time.sleep(1)


# function that will get repeated for each plater, accepts the number corresponting to the current player and return a completed player object with randomized deck, name, hand and hp
def set_up(whos_turn, player_1st=None):
	#recive the name from the player
	name = input("\nPlayer {} how do you want to be called?: ".format(whos_turn))
	if player_1st !=None:
		while name == player_1st:
			name = input("player 1 already has this name, pick a difrent one: ")
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
		return True				#with this the hole game needs to ends
	else:
		#in case there are no cards left
		if cards_finished:
			if current_player.hp < enemy_player.hp:
				print("""\n\nno cards left and {} has less hp!

===================================================
!!!!!	------>> {} YOU WIN!
===================================================\n""".format(current_player.player_name, enemy_player.player_name))
				return True				#with this the hole game needs to ends
			elif current_player.hp > enemy_player.hp:
				print("""\n\nno cards left and {} has less hp!

===================================================
!!!!!	------>> {} YOU WIN!
===================================================\n""".format(enemy_player.player_name, current_player.player_name))
				return True				#with this the hole game needs to ends
			else:
				print("\n\nno cards left and you have the same hp...\n\tIts a fucking draw!\n")
				return True				#with this the hole game needs to ends

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
		return False

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









#### MODE VS COMPUTER


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
def computer_set_up(whos_turn, player_1st=None):
	#recive the name for the computer
	name = input("\nPlayer {} is the computer! Do you want to give it a name?\n(if not leave blank and press ENTER it will be called 'Computer'): ".format(whos_turn))
	if name == "":
		name = "Computer"
	if player_1st !=None:
		while name == player_1st:
			name = input("player 1 already has this name, pick a difrent one: ")

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
