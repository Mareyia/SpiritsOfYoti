from cf_list_dicts import decks
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
	#initiative: checks to see if the current_player is in the attack
	if initiative:
		print("""\nNow pick a card: 

		1:		{}
		2:		{}
		3:		{}

or 'r' to replace card with one with your deck and end your turn deck
""".format(current_player.hand[0], current_player.hand[1], current_player.hand[2]))
		card_selection = input("Pick a/an card/option: 1/2/3/r: ")
		#in case the player wants to replace a card
		if card_selection == 'r':
			card_selection = input("Pick a card to replace: 1/2/3: ")
			need_replacement = True
	#this function will continue with else when current player is the defending player 
	else:
		print("\ncurrent hp: {}".format(current_player.hp))
		print("""Now pick a card: 

		1:		{}
		2:		{}
		3:		{}

""".format(current_player.hand[0], current_player.hand[1], current_player.hand[2]))
		card_selection = input("Pick a card: 1/2/3: ")
		
	card_selection = current_player.hand[int(card_selection) - 1]
	#if no card is going to replaced, the chosen hard needs to be removed from the hand for the game to progress
	if not need_replacement:
		current_player.remove_card(card_selection)
	return card_selection, need_replacement


#function that replace the selected card with a random one from the deck
def replace_card(player_choosed_to_replace, card_to_replace):
	random_new_card_place = randint(0, len(player_choosed_to_replace.ready_deck)-1)
	player_choosed_to_replace.hand.append(player_choosed_to_replace.ready_deck.pop(random_new_card_place))
	player_choosed_to_replace.ready_deck.insert(random_new_card_place, card_to_replace)
	player_choosed_to_replace.hand.remove(card_to_replace)
	print("\nReplaced: {}\n".format(card_to_replace))


#CARDFIGHT! here is the function that applies the name of the game! The two card objects are getting compared and the result of the comparison modifies the player objects 
def fight(attacking_player, attacking_card, defending_player, defending_card):
	#the situation in wich the defender doesn't have any cards to block with
	#if defending_card.type_of_card == 
	defending_card.block_damage(attacking_card.deal_damage(defending_card), defending_player)
	
	
	
	#print("\n{} vs {}\n".format(attacking_card, defending_card))
	













