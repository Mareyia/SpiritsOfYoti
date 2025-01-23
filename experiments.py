def camplaign_mode():

	
	players["Player " + str(i)] = [set_up(i, player_names), Entity(str(i), list_of_available_locations[randint(0, len(list_of_available_locations) - 1)])]



	def difficulty_genaretion(user_input):
		number_of_players_and_positions = {}
		the_chosen_map = None
		number_of_players_and_positions[0] = location
		number_of_players_and_positions[1] = location
		number_of_players_and_positions[2] = location
		if user_input == 2:
			number_of_players_and_positions[3] = location
			number_of_players_and_positions[4] = location
		if user_input == 3:
			number_of_players_and_positions[5] = location
			number_of_players_and_positions[6] = location
		the_chosen_map = maps[user_input]
		return number_of_players_and_positions, the_chosen_map


def normal_mode():




def hard_mode():
