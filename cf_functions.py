from cf_list_dicts import decks, attacker_message
from cf_classes import Card, Player
from random import randint


# here the game starts and ends if any player reaches 0 hp. *The start_turn function returns a bool that changes if the upper condition changes.
def playGame():
	player_1 = set_up(1)
	player_2 = set_up(2)

	game_end = False
	while not game_end:
		game_end = start_turn(player_1, player_2)
		if not game_end:
			game_end = start_turn(player_2, player_1)
	to_continue()



# a helpfull function inbetwin inputs and prints to not output everything all together and creating chaos to the terminal   
def to_continue():
	finishedreading = input("Type anything to continue: ") 


# function that will get repeated for each plater, accepts the number corresponting to the current player and return a completed player object with randomized deck, name, hand and hp
def set_up(whos_turn):
	#recive the name from the player
	name = input("\nPlayer {} how do you want to be called?: ".format(whos_turn))
	print("\nHello {}!!!".format(name))
	print("""\nNow pick a deck: 

   'Firefly'    'Antblue'
       1            2
 
or 'l' to list every card on each deck
""")
	#recieve the choise of deck from the player 
	deck_selection = input("Type here 1/2/l: ")
	while deck_selection == 'l':
		print(decks)
		deck_selection = input("Type here 1/2/: ")
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
	
	#checks if any player reaced 0 hp so the game will end
	condition = current_player.check_status()
	if condition:
		print("{} died! {} YOU WIN!".format(current_player.player_name, enemy_player.player_name))
		return True				#with this the hole game needs to ends
	else:
		#asks players to pick a card to play or to replace
		card_selected_attacking, replacing = pick_a_card(current_player, enemy_player, True)
		if replacing:
			#when replacing nothing else happens
			replace_card(current_player, card_selected_attacking)
		else:
			#if not replacing the other player has to pick a card too and the cards fight
			card_selected_defending, not_needed = pick_a_card(enemy_player, current_player, False)
			fight(current_player, card_selected_attacking, enemy_player, card_selected_defending)
		return False

#ask each player to pick a card
def pick_a_card(current_player, enemy_player, initiative):
	need_replacement = False				#on/of if the player wants to replace a card
	print("{} is about to pick a card {} don't look!".format(current_player.player_name, enemy_player.player_name))
	to_continue()
	
	display_hand_first, display_hand_second, valid_options_total, valid_options_no_r_first, = show_hand(current_player.hand, initiative)
	#print(display_hand_first)
	#print(display_hand_second)
	#print(valid_options_total)
	#print(valid_options_no_r_first)
	#print(valid_options_no_r_second)
	
	#valid_options_total for ssafety measure1 if the replacing option selected
	#initiative: checks to see if the current_player is in the attack
	if initiative:
		
		#valid_options_no_r_first for ssafety measure2 
		print(display_hand_first) #shows hand
		card_selection = input("Pick a/an card/option: 1/2/3/r: ")
		
		#safety measure0, if player types something wrong or r
		while card_selection not in valid_options_no_r_first:
			
			#in case the player wants to replace a card
			if card_selection == 'r':
				card_selection = input("Pick a card to replace: 1/2/3: ")
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
		print("\ncurrent hp: {}".format(current_player.hp))
		print(display_hand_second)
		
		#if there are no available cards to defend with
		if current_player.hand[0].type_of_card == "attack" and current_player.hand[1].type_of_card == "attack" and current_player.hand[2].type_of_card == "attack":
			print("No available card to select")
			card_selection = None
			to_continue()
		else:
			card_selection = input("Pick a card: 1/2/3: ")
			
			#safety measure1, if player types something wrong
			#valid_options_total for safety measure1 
			while card_selection not in valid_options_total:
				
				#safety measure1, if player attemps to pick an invalid card
				if card_selection in valid_options_total:
					if current_player.hand[int(card_selection) - 1].type_of_card == "attack":
						print("Cannot play an attacking (ATTACK-type) card on your oponment's initiative")
						card_selection = input("Pick again: ")
				#resolution of measure1
				else:
					print("Invalid option")
					card_selection = input("Type again: ")
			
		
	if card_selection !=None:
		card_selection = current_player.hand[int(card_selection) - 1]
	#if no card is going to replaced, the chosen hard needs to be removed from the hand for the game to progress
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
	show_cards_1 = "\nNow pick a card:\n\n"
	valid_options = []
	valid_options_no_r = []
	for i in range(len(players_hand)):
		#creating these nessery lists to return for the pick_card's safety measures to work
		valid_options.append(str(i+1))
		if players_hand[i].type_of_card != "block":
			valid_options_no_r.append(str(i+1))
		
		#costomising the print statement dependent on the number of cards on hand
		show_cards_1 += "	{}:	{}\n".format(i+1, players_hand[i])
	show_cards_1 += "\n"
	
	show_cards_2 = show_cards_1
	#if the player is the attacking one there should be outputed an option for replace
	show_cards_1 += attacker_message
	
	return show_cards_1, show_cards_2, valid_options, valid_options_no_r
