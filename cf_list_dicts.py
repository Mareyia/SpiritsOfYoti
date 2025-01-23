from cf_classes import Card, Menu_options, All_Menu
from cf_classes_2 import Possition, Playing_grid, The_map

main_menu = Menu_options("Main menu")
main_menu.add_option("1", Menu_options("New Game", "1", main_menu, "Campaing"))
main_menu.add_option("2", Menu_options("Custom Match", "2", main_menu, "Custom Match"))
main_menu.add_option("3", Menu_options("Instructions", "3", main_menu, "Instructions"))
main_menu.add_option("0", Menu_options("Exit", "0"))
main_menu.options["1"].add_option("1", Menu_options("Easy", "1", main_menu.options["1"], "", "", "", True))
main_menu.options["1"].add_option("2", Menu_options("Normal", "2", main_menu.options["1"],  "", "", "", True))
main_menu.options["1"].add_option("3", Menu_options("Hard", "3", main_menu.options["1"],  "", "", "", True))
main_menu.options["1"].add_option("0", Menu_options("Back", "0"))
main_menu.options["2"].add_option("1", Menu_options("All vs All", "1", main_menu.options["2"]))
main_menu.options["2"].add_option("2", Menu_options("Players vs Computers", "2", main_menu.options["2"]))
main_menu.options["2"].add_option("3", Menu_options("Teams", "3", main_menu.options["2"]))
main_menu.options["2"].add_option("0", Menu_options("Back", "0"))
main_menu.options["3"].add_option("0", Menu_options("Back", "0"))
menuuuu = All_Menu(main_menu)


A_map = The_map(Playing_grid(17, 18))

A_map.add_location(Possition("A", "location", [11, 6]))
A_map.add_location(Possition("B", "location", [8, 12]))
A_map.add_location(Possition("C", "location", [17, 18]))
A_map.add_location(Possition("D", "location", [1, 14]))
A_map.add_location(Possition("E", "location", [7, 3]))
A_map.add_location(Possition("F", "location", [14, 10]))
A_map.add_location(Possition("G", "location", [2, 17]))
A_map.add_location(Possition("H", "location", [16, 2]))

A_map.add_road(Possition("A", "road", [A_map.locations[0], A_map.locations[1]]))
A_map.add_road(Possition("B", "road", [A_map.locations[2], A_map.locations[3]]))
A_map.add_road(Possition("C", "road", [A_map.locations[0], A_map.locations[5]]))
A_map.add_road(Possition("D", "road", [A_map.locations[1], A_map.locations[5]]))
A_map.add_road(Possition("E", "road", [A_map.locations[4], A_map.locations[3]]))
A_map.add_road(Possition("F", "road", [A_map.locations[4], A_map.locations[0]]))
A_map.add_road(Possition("G", "road", [A_map.locations[2], A_map.locations[5]]))
A_map.add_road(Possition("H", "road", [A_map.locations[3], A_map.locations[1]]))
A_map.add_road(Possition("I", "road", [A_map.locations[2], A_map.locations[6]]))
A_map.add_road(Possition("J", "road", [A_map.locations[1], A_map.locations[6]]))
A_map.add_road(Possition("K", "road", [A_map.locations[7], A_map.locations[4]]))
A_map.add_road(Possition("L", "road", [A_map.locations[7], A_map.locations[1]]))
A_map.add_road(Possition("M", "road", [A_map.locations[7], A_map.locations[2]]))
A_map.add_road(Possition("N", "road", [A_map.locations[7], A_map.locations[0]]))

#position 0, 1 and 2 should be the easy, normal and hard map
maps = [A_map, A_map, A_map, A_map, A_map, A_map, A_map, A_map, A_map, A_map]

punch_of_focus = Card("Punch of focus", "attack", 2)
kick_of_fury = Card("Kick of fury", "attack", 3)
flame_spit = Card("Flame spit", "attack", 5)
xisia = Card("Xisia", "attack", 8)
headbut = Card("Headbut", "attack", 5)


power_stance = Card("Power stance", "block", 1)
dodje = Card("Dodje", "block", 3)
feet_distraction = Card("Feet distraction", "block", 5)
smelly_diaria = Card("Smelly Diaria", "block", 0)

throwing_rocks = Card("Throwing rocks", "balander", 3)  
shooting_hertfull_words = Card("Shooting hertfull words", "balander", 4)
aima_Periodou = Card("Aima Periodou", "balander", 6)

drinking_ouiski = Card("Drinking ouiski", "special", 3)
magical_web = Card("Magical web", "special")     

decks = {
"Firefly":[punch_of_focus, kick_of_fury, flame_spit, flame_spit, power_stance, power_stance, throwing_rocks, throwing_rocks, throwing_rocks, shooting_hertfull_words, shooting_hertfull_words, drinking_ouiski],
"Antblue": [punch_of_focus, kick_of_fury, power_stance, dodje, dodje, throwing_rocks, throwing_rocks, shooting_hertfull_words, shooting_hertfull_words, drinking_ouiski, magical_web, magical_web], 
"Shit": [punch_of_focus, kick_of_fury, power_stance, dodje, dodje, throwing_rocks, throwing_rocks, shooting_hertfull_words, shooting_hertfull_words, drinking_ouiski, magical_web]
}
#"Poutsa": [heavy_attack, headbut, headbut, xisia, xisia, feet_distraction, smelly_diaria, smelly_diaria, aima_Periodou, aima_Periodou, aima_Periodou, aima_Periodou]


instructions = """
--Card Fight is a turn-based game for two local players, were they put their cards the one against the other and tries to kill their oppement. 
1--Choose a name and deck.
--The first player that chosed previously will be the first player
--Each player starts with 10 health points and 12 cards on their deck

2--When the decks have been choosen each player will draw 3 cards automaticly.
--Every turn consists o two parts, a attacking and a defending part in order.

3--In any part the players have to select a card that will use to battle.
--There are 4 types of cards:
		ATTACK  --deals damage to the enemy.  Can only be played on the attacking part of the turn
		BLOCK  --blocks incoming damage from enemy.  Can only be played on the defending part of the turn
		BALANDER  --can be used both for attacking and blocking and can be played in any part
		SPECIAL  --there are two types of special in this version, both can be played in any part 
			"Drinking ouiski" that heals you
			"Magical web" that cancels all enemy actions
	*The damage that is dealt, blocked or heal depens on the card and are points described in its card. Some cards are stronger than others, choose wisely...
	attacking player can also swap a card from their hand to the deck

4--When the cards have been choosen the fight will begin.

5--The stronger card will use the remaining points after the fight to damage the health of the player.
	*Attacking 2 > Defending 1 = Attacking won and with the remaining 1 point will deal damage to the player

6--The turns will be repeated until the end, when a player reaches 0 hp or where there is no card available to play.
"""
#this string gets attached at the end of the print statement showing the cards 
attacker_message = "\nor 'r' to replace card with one with your deck and end your turn"

#this string is required for player against player so the one player can't see the cards of the other player
ton_of_space ="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
