from math import inf
from heapq import heappop, heappush
from random import randint

def lets_move(character, given_map):
	where = None
	available_options = []
	for i in range(len(character.position.alailable_destinacions)):
		if character.position.alailable_destinacions[i].entity_ocupation is not None:
			continue
		available_options.append(str(i))
	#print(given_map)
	#print("You are at {} (x={}, y={}).".format(character.position, character.position.location[0], character.position.location[1]))
	counters = {}
	counter = 0
	for i in range(len(character.position.alailable_destinacions)):
		if character.position.alailable_destinacions[i].entity_ocupation is not None or character.position.get_path(character.position.alailable_destinacions[i]).distance > character.movement:
			continue
		counters[str(counter)] = i
		print("For {} using {} with {} length type '{}'".format(character.position.alailable_destinacions[i], character.position.get_path(character.position.alailable_destinacions[i]), character.position.get_path(character.position.alailable_destinacions[i]).distance, counter))
		counter += 1
	where = input("Choose a destination: ")
	while where not in counters.keys():
		where = input("Wrong inputm, try again: ")
	
	previous_location = character.position
	given_map.move_entity(character, character.position.alailable_destinacions[counters[where]])
	character.change_movement(previous_location.get_path(character.position).distance, False, True)
	print("Movement left:", character.movement)
	
	whant_to_continue_moving = input("Continue moving? (y/n): ")
	while whant_to_continue_moving not in ['y', 'n']:
		whant_to_continue_moving = input("Invalid input, try again. Continue moving? (y/n): ")
	if whant_to_continue_moving == 'y':
		return True 
	else:
		return False

def heuristic(start, goal):
	x_distance = abs(start.location[0] - goal.location[0])
	y_distance = abs(start.location[1] - goal.location[1])
	return x_distance + y_distance

# find_fastest_path_to_player is my implemetation of A* algorith and the part that concludes the requirement of the project. I am using this function to set the recommented path for the npc to find the player in the fastest most efficient way
def find_fastest_path_to_player(given_map, npc, player):
	paths_and_distances = {}
	for location in given_map.locations:
		paths_and_distances[location] = [inf, [npc.position]]
	paths_and_distances[npc.position][0] = 0
	
	locations_to_explore = [(0, npc.position)]
	while locations_to_explore and paths_and_distances[player.position][0] == inf:
		current_distance, current_location = heappop(locations_to_explore)
		for neighbor in current_location.alailable_destinacions:
			if neighbor.entity_ocupation != None:
				if neighbor.entity_ocupation != player:
					continue
			new_distance = current_distance + current_location.get_path(neighbor).distance + heuristic(neighbor, player.position)
			new_path = paths_and_distances[current_location][1] + [neighbor]
			
			if new_distance < paths_and_distances[neighbor][0]:
				paths_and_distances[neighbor][0] = new_distance
				paths_and_distances[neighbor][1] = new_path
				print("last error")
				print(new_distance, neighbor)
				heappush(locations_to_explore, (new_distance, neighbor))
	
	return paths_and_distances[player.position]

def npc_move(npc_to_move, given_map):
	reccomended_choice = [inf, None]
	path_for_every_player = [find_fastest_path_to_player(given_map, npc_to_move, player) for player in given_map.entities if player.team != npc_to_move.team and player.position is not None]
	print()
	for path in path_for_every_player:
		if path[0] < reccomended_choice[0]:
			reccomended_choice = path
	print(reccomended_choice)
	if reccomended_choice[1][1].entity_ocupation is None:
		previous_location = npc_to_move.position
		given_map.move_entity(npc_to_move, reccomended_choice[1][1])
		npc_to_move.change_movement(previous_location.get_path(npc_to_move.position).distance, False, True)


def Fight(attacking_entity, defending_entity):
	pass


def condition_for_endgame(teams_given, new_death=None):
	if new_death is not None:
		for team in teams_given:
			print(team, teams_given[team])
		print(new_death)
		teams_given[new_death[1].team].remove(new_death)
	alive_teams = {}
	for team in teams_given:
		for team_player in teams_given[team]:
			if team_player[1].position is not None:
				alive_teams[team] = teams_given[team]
				break
	return alive_teams


def end_game_message(teams_given, game_mode_given):
	if game_mode_given.menu_sub_title == "Campaing":
		for team in teams_given:
			if team == 1:
				return "\n{} defeated all oponments and WON THE GAME!!!\nCongratsulations!\n".format(teams_given[team][0][0].player_name)
			else:
				return "\nComputers destroyed you\nGAME OVER!!!\n"
	elif game_mode_given.menu_title == "All vs All":
		for team in teams_given:
			return "\n{} defeated all enemies and WON THE GAME!!!\nCongratsulations!\n".format(teams_given[team][0][0].player_name)
	elif game_mode_given.menu_title == "Players vs Computers":
		for team in teams_given:
			if team == 1:
				return "\nTeam {} humans you defeated the computers and WON THE GAME!!!\nCongratsulations!\n".format(team)
			else:
				return "\nComputers destroyed you\nGAME OVER!!!\n"
	else:
		for team in teams_given:
			return "\nTeam {} defeated all enemy teams and WON THE GAME!!!\nCongratsulations!\n".format(team)


def team_balance_check(given_answer, all_the_teams, number_of_player, all_the_players, the_continue_function, mode_of_the_custom_game="Something else"):
	players_left = len(all_the_players.keys()) - number_of_player + 1
	empty_teams = {}
	#print("Hello!")
	for team in all_the_teams:
		if len(all_the_teams[team]) == 0:
			empty_teams[team] = all_the_teams[team]
			#print(empty_teams[team])
			#print(all_the_teams[team])
	if len(empty_teams.keys()) == players_left and given_answer not in list(empty_teams.keys()):
		print("Can't do, some teams will be left empty")
		the_continue_function(1)
		print("Autofilling")
		the_continue_function(1)
		if mode_of_the_custom_game == "Players vs Computers":
			if all_the_teams[1] == empty_teams[1]:
				return "n"
			else:
				return "y"
		else:
			print(empty_teams.keys())
			return list(empty_teams.keys())[randint(0, len(empty_teams.keys())- 1)]
	return given_answer
















