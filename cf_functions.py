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
			print("\nshit\n")#print(lidict.instructions)
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
	
