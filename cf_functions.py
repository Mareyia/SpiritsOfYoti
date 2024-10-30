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















