from cf_classes import Card, Menu_options, All_Menu
from cf_maps import maps

#menu stracture
main_menu = Menu_options("Main menu")
main_menu.add_option("1", Menu_options("New Game", "1", main_menu, "Campaing"))
main_menu.add_option("2", Menu_options("Custom Match", "2", main_menu, "Custom Match"))
main_menu.add_option("3", Menu_options("Instructions", "3", main_menu, "Instructions",  "", "", True))
main_menu.add_option("0", Menu_options("Exit", "0"))
main_menu.options["1"].add_option("1", Menu_options("Easy", "1", main_menu.options["1"], "", "", "", True))
main_menu.options["1"].add_option("2", Menu_options("Normal", "2", main_menu.options["1"],  "", "", "", True))
main_menu.options["1"].add_option("3", Menu_options("Hard", "3", main_menu.options["1"],  "", "", "", True))
main_menu.options["1"].add_option("0", Menu_options("Back", "0"))
main_menu.options["2"].add_option("1", Menu_options("All vs All", "1", main_menu.options["2"], "Select a map"))
main_menu.options["2"].add_option("2", Menu_options("Players vs Computers", "2", main_menu.options["2"], "Select a map"))
main_menu.options["2"].add_option("3", Menu_options("Teams", "3", main_menu.options["2"], "Select a map"))
main_menu.options["2"].add_option("0", Menu_options("Back", "0"))
main_menu.options["3"].add_option("0", Menu_options("Back", "0"))
for i in range(1, len(main_menu.options["2"].options.keys())):	
	for j in range(1, len(maps) + 1):
		main_menu.options["2"].options[str(i)].add_option(str(j), Menu_options(maps[j - 1].name_of_map, str(j), main_menu.options["2"].options[str(i)], "", "", "", True))
	main_menu.options["2"].options[str(i)].add_option("0", Menu_options("Back", "0"))
menuuuu = All_Menu(main_menu)



#Cards
punch_of_focus = Card("Punch of focus", "attack", 2)
kick_of_fury = Card("Kick of fury", "attack", 3)
flame_spit = Card("Flame spit", "attack", 5)
xisia = Card("Xisia", "attack", 8)
headbut = Card("Headbut", "attack", 5)
heavy_attack = Card("Toes on your mouth", "attack", 7)


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
"Shit": [punch_of_focus, kick_of_fury, power_stance, xisia, dodje, throwing_rocks, aima_Periodou, shooting_hertfull_words, shooting_hertfull_words, drinking_ouiski, feet_distraction, feet_distraction],
"Poutsa": [heavy_attack, headbut, headbut, xisia, xisia, feet_distraction, smelly_diaria, smelly_diaria, aima_Periodou, aima_Periodou, aima_Periodou, aima_Periodou]}



#this string gets attached at the end of the print statement showing the cards 
attacker_message = "\nor 'r' to replace card with one with your deck and end your turn"

#this string is required for player against player so the one player can't see the cards of the other player
ton_of_space ="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
