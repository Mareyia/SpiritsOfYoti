def death_check()
	death_check_2, empty_hand_check_2 = all_player[every_player][0].check_status()
	if death_check_2:
		print(all_player[every_player][0], "died!")
		#remove the player
		if all_player[every_player][1].position:
			A_map.remove_entity(all_player[every_player][1])
			number_of_alive_player -= 1

def condition_for_endgame(teams_given, game_mode_given, new_death=None):
	if new_death is not None:
		teams_given[new_death.team].remove(new_death)
	alive_teams = []
	for team in teams_given:
		for team_player in teams_given[team]:
			if team_player[1].position is not None:
				alive_teams.append(team)
				break
	return alive_teams


def end_game_message(teams_given, game_mode_given):
	if game_mode_given == "Campaing":
		for team in teams_given:
			if team == 1:
				return "\n{} defeated all oponments and WON THE GAME!!!\nCongratsulations!\n".format(teams_given[team][0][0].player_name)
			else:
				return "\nComputers destroyed you\nGAME OVER!!!\n"

1, 2, 3, 4, 5, 6

[]
[]
[]
[1, 2, 3]


def team_balance_check(given_answer, all_the_teams, number_of_player, all_the_players, mode_of_the_custom_game="Something else"):
	players_left = len(all_the_players.keys()) - number_of_player + 1
	empty_teams = {}
	for team in all_the_teams:
		if len(all_the_teams[team]) == 0:
			empty_teams[team] = all_the_teams[team]
	if empty_teams == players_left:
		print("Can't do, some teams will be left empty")
		to_continue(1)
		print("Autofilling")
		to_continue(1)
		if mode_of_the_custom_game == "Players vs Computers":
			if all_the_teams[1] == empty_teams[1]:
				return "n"
			else:
				return "y"
		else:
			return empty_teams.keys()[randint(range(0, len(empty_teams.keys())- 1))]
	return given_answer

#backup
#possitions refers to all the available places an entity can move to, the roads and the parts of the roads
class Possition:
	def __init__(self, identity, type_of, location, autofill_roads=True):
		self.identity = identity
		#there are 3 types of possitions, the available square for the player/npc, the roads that connects them and the road parts that composes each rode
		self.type_of = type_of
		#depends on the type, location will be a list of two elements, a x and y axis in case of road parts and squarres and whole square classes in case of roads
		self.location = location
		#distance is the total number of road parts that connects two locations. this will be used for the recommendation part (find for the computer the faster way to reach the player)
		self.distance = 0
		self.destinacions = {}
		self.alailable_destinacions = []
		self.entity_ocupation = None
		self.autofill_roads =  autofill_roads
		#if position is a road and you don't want to manually add its parts it can happen automatically autoffilling the map distance
		if self.type_of == "road":
			for loc_1 in location:
				loc_1.add_roads(self)
				for loc_2 in location:
					if loc_1 != loc_2:
						loc_1.alailable_destinacions.append(loc_2)
			if autofill_roads == True:
				location_A_postion_x = self.location[0].location[0]
				location_A_postion_y = self.location[0].location[1]
				location_B_postion_x = self.location[1].location[0]
				location_B_postion_y = self.location[1].location[1]
				x_distance = location_A_postion_x - location_B_postion_x
				y_distance = location_A_postion_y - location_B_postion_y
				self.distance = abs(x_distance) + abs(y_distance)
				copy_of_distance = self.distance
				while copy_of_distance > 0:
					if x_distance > 0:
						location_A_postion_x -= 1
						self.destinacions[copy_of_distance] = Possition("RP_"+str(copy_of_distance), "road_part", [location_A_postion_x, location_A_postion_y])
						copy_of_distance -= 1
						x_distance -= 1
						if x_distance > 0:
							location_B_postion_x += 1
							self.destinacions[copy_of_distance] = Possition("RP_"+str(copy_of_distance), "road_part", [location_B_postion_x, location_B_postion_y])
							copy_of_distance -= 1
							x_distance -= 1
					if y_distance > 0:
						location_A_postion_y -= 1
						self.destinacions[copy_of_distance] = Possition("RP_"+str(copy_of_distance), "road_part", [location_A_postion_x, location_A_postion_y])
						copy_of_distance -= 1
						y_distance -= 1
						if y_distance > 0:
							location_B_postion_y += 1
							self.destinacions[copy_of_distance] = Possition("RP_"+str(copy_of_distance), "road_part", [location_B_postion_x, location_B_postion_y])
							copy_of_distance -= 1
							y_distance -= 1

					if x_distance < 0:
						location_A_postion_x += 1
						self.destinacions[copy_of_distance] = Possition("RP_"+str(copy_of_distance), "road_part", [location_A_postion_x, location_A_postion_y])
						copy_of_distance -= 1
						x_distance += 1
						if x_distance < 0:
							location_B_postion_x -= 1
							self.destinacions[copy_of_distance] = Possition("RP_"+str(copy_of_distance), "road_part", [location_B_postion_x, location_B_postion_y])
							copy_of_distance -= 1
							x_distance += 1
					if y_distance < 0:
						location_A_postion_y += 1
						self.destinacions[copy_of_distance] = Possition("RP_"+str(copy_of_distance), "road_part", [location_A_postion_x, location_A_postion_y])
						copy_of_distance -= 1
						y_distance += 1
						if y_distance < 0:
							location_B_postion_y -= 1
							self.destinacions[copy_of_distance] = Possition("RP_"+str(copy_of_distance), "road_part", [location_B_postion_x, location_B_postion_y])
							copy_of_distance -= 1
							y_distance += 1
