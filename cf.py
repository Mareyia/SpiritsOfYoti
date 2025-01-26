from cf_list_dicts import instructions, menuuuu, maps
from cf_functions import playGame, to_continue

print("\n=========================================\n========= Welcome to Card fight =========\n=========================================")
menuuuu.using_menu(playGame, maps)


#old menu

# A terminal main menu giving you 3 options and looping on them until you press the exit option that breaks the loop 
menu = '0' #variable for the selected option, the program just started so the '' corresponds to the choise still hasn't given
#the loop. the option 0 will break the loop aka to exit the game

while menu!='0':
	print("\n\tMain Menu\n")
	print("Type '1' to start the game (local human vs human),\ntype '2' to play against the computer,\ntype '3' for instructions\n\nor type '0' to exit\n")
	menu = input("Type here: ")

	#safety measure wrong type
	while menu not in ['0', '1', '2', '3']:
		print("--Wrong input--\nTry again:\n\nType '1' to start the game,\ntype '2' for instructions\n\nor type '0' to exit\n".format(menu)) 
		menu = input("Type here: ")

	if menu=='3':
		print(instructions)
		to_continue()
	elif menu=='1' or menu=='2':
		playGame(bool(int(menu)-1))
	else:
		print("Bye bye hope you had funnnn, or dont... I actually don't really care.")
