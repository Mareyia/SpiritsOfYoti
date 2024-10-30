from cf_list_dicts import instructions, decks
from cf_classes import Card, Player 

# main_menu function for a terminal main menu giving you 3 options an looping on them until you press the exit option that breaks the loop 
def main_menu():
	menu = "" #variable for the selected option, the program just started so the '' corresponds to the choise still hasn't given
	#the loop. the option 0 will break the loop aka to exit the game
	print("\n=========================================\n========= Welcome to Card fight =========\n=========================================")
	while menu!='0':
		print("\n\tMain Menu\n")
		print("Type '1' to start the game,\ntype '2' for instructions\n\nor type '0' to exit\n")
		menu = input("Type here: ")
		while menu not in ['0', '1', '2']:
			print("\n--You entered '{}'-- wich is not a valid option.\nTry again:\nType '1' to start the game,\ntype '2' for instructions\n\nor type '0' to exit\n".format(menu)) 
			menu = input("Type here: ")
		if menu=='2':
			print(instructions)
			to_continue()
		elif menu=='1':
			playGame()
		else:
			print("Bye bye hope you had funnnn, or dont... I actually don't really care.")
      
      
      
# a helpfull function inbetwin inputs and prints to not output everything all together and creating chaos to the terminal   
def to_continue():
	finishedreading = input("Type anything to continue: ") 


def playGame():
	print("Played!")
	pass
	

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


def start_turn(current_player, enemy_player):
	current_player.draw_cards()
	enemy_player.draw_cards()
	condition = current_player.check_status()
	if condition:
		print("{} died! {} YOU WIN!".format(current_player.player_name, enemy_player.player_name))
		#return break				#with this the hole game needs to ends
	card_selected_attacking, replacing = pick_a_card(current_player, enemy_player, True)
	if replacing:
		replace_card(card_selected_attacking)
	else:
		card_selected_defending, not_needed = pick_a_card(enemy_player, current_player, False)
		fight(card_selected_attacking, card_selected_defending)

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
		if card_selection == 'r':
			card_selection = input("Pick a card to replace: 1/2/3: ")
			need_replacement = True
	else:
		print("\ncurrent hp: {}".format(current_player.hp))
		print("""Now pick a card: 

		1:		{}
		2:		{}
		3:		{}

""".format(current_player.hand[0], current_player.hand[1], current_player.hand[2]))
		card_selection = input("Pick a card: 1/2/3: ")
		
	card_selection = current_player.hand[int(card_selection) - 1]
	if not need_replacement:
		current_player.remove_card(card_selection)
	return card_selection, need_replacement

def replace_card(card_to_replace):
	print("n\replaced: {}\n".format(card_to_replace))
	pass
	
	
def fight(attacking_card, defending_card):
	print("\n{} vs {}\n".format(attacking_card, defending_card))
	pass













