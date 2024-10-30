from cf_classes import Card

light_attack = Card("Punch of focus", "attack", 2)
heavy_attack = Card("Kick of fury", "attack", 3)
ability_attack = Card("Flame spit", "attack", 5)

light_block = Card("Power stance", "block", 1)
heavy_block = Card("Dodje", "block", 3)

light_balander = Card("Throwing rocks", "balander", 3)  
heavy_balander = Card("Shooting hertfull words", "balander", 4)

simple_special = Card("Drinking ouiski", "special", 3)
special_special = Card("Magical web", "special")     

decks = {
"Firefly":[light_attack, heavy_attack, ability_attack, ability_attack, light_block, light_block, light_balander, light_balander, light_balander, heavy_balander, heavy_balander, simple_special],
"Antblue": [light_attack, heavy_attack, light_block, heavy_block, heavy_block, light_balander, light_balander, heavy_balander, heavy_balander, simple_special, special_special, special_special]
}

instructions = """
nothing
at
the
moment
"""
