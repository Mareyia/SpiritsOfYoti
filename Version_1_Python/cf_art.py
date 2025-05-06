card_img = ["", 
"╔═════════════════════════════════╗",
"║║                               ║║", ##line2 Icon begining
"║║                               ║║",
"║║                               ║║",
"║║                               ║║",
"║║                               ║║",
"║║                               ║║",
"║║                               ║║",
"║║                               ║║",
"║║                               ║║",
"║║                               ║║",
"║║                               ║║",
"║║                               ║║",
"║║                               ║║",
"║║                               ║║", #line15 Icon ending
"║╙───────────────────────────────╜║",
"║│                               │║", #line17 Name
"║│                               │║", #line18 Type
"║│                               │║", #line19 Ability points
"║│                               │║", 
"║│                               │║", #line21 Discription line1
"║│                               │║", #line22 Discription line2
"║│                               │║", #line23 Discription line3
"║└───────────────────────────────┘║", 
"╚═════════════════════════════════╝"]




#def insert_image(any_imag, card_img):
#	string_len = len(card_img[1]) - 4
#	new_lines = []
#	ending_space = ""
#	times = 1
#	if len(any_imag) > string_len:
#		new_lines.append("║║" + any_imag[0:string_len] + "║║")
#		times += 1
#		multistring_len = string_len * 2
#		while len(any_imag) > multistring_len:
#			new_lines.append("║║" + any_imag[string_len*(times-1):string_len*times] + "║║")
#			times += 1
#			multistring_len += string_len
#			if times == 14:
#				break
#	ending_spaces_needed = (string_len * times) - len(any_imag)
#	for i in range(ending_spaces_needed):
#		ending_space += " "
#	new_lines.append("║║" + any_imag[string_len*(times-1):] + ending_space + "║║")
#	return new_lines



def center_text_string(any_text, string_len):
	string_len -= 4
	centered = ""
	starting = "║│"
	ending = any_text
	spaces_needed = string_len - len(any_text)
	if spaces_needed % 2 != 0:
		starting += " "
	for i in range(int(spaces_needed/2)):
		starting += " "
		ending += " "
	centered = starting + ending + "│║"
	return centered

def multiple_lines_descreption(any_text, line_string):
	string_len = len(line_string) - 4
	new_lines = []
	ending_space = ""
	times = 1
	if len(any_text) > string_len:
		new_lines.append("║│" + any_text[0:string_len] + "│║")
		times += 1
		multistring_len = string_len * 2
		while len(any_text) > multistring_len:
			new_lines.append("║│" + any_text[string_len*(times-1):string_len*times] + "│║")
			times += 1
			multistring_len += string_len
	ending_spaces_needed = (string_len * times) - len(any_text)
	for i in range(ending_spaces_needed):
		ending_space += " "
	new_lines.append("║│" + any_text[string_len*(times-1):] + ending_space + "│║")
	if len(new_lines) > 3:
		new_lines.append("║└───────────────────────────────┘║")
		new_lines.append("╚═════════════════════════════════╝")
	return new_lines

#Testing
card_img[17] = center_text_string("Flaming Spit", len(card_img[17]))
card_img[18] = center_text_string("5", len(card_img[18]))
card_img[19] = center_text_string("ATTACK", len(card_img[19]))
description_lines = multiple_lines_descreption("You spit flames against your   opoments face dealing 5 damage!", card_img[21])
#card_image = insert_image("  .-*%#-=:. .:-.-: .-:*%+++*-. -#@#*%*@@@@- .-+++*%@@@@@@@%+.*#+.=:=+=-@%##@@@@@@@@@@@@@#+ +*: ::+%@@@*@@@@@@@@@@@###*+- :*-.-=+++++==##**-.:--#.       =*=.:-==+++=. +=....:=        .:+#*-+#=---:=%+   ..:       ....:::-::...:::::    .      " ,card_img)

#for i in range(len(card_image)):
#	card_img[5 + i] = card_image[i]
                       ..   .         .-:.::.      
    .:-=++==-:              :      .:-+=:.-::=-:   
   .:-+=::-*=:+****=.       :    .:=++*=-:=+***+-: 
   :-+.. -:  +*=:-+=     ...+=::=++***#*+****#*+=: 
  -::.:  .   ::    *-:-.:-+===+**#########*****=:..
  ::- .      ..   ::+:..-++*#############***+++=:. 
  :::        :+**+**= =*#########*****#*+==----:.  
   :-       ...:=--:  =**#+==-.       .=.          
   .::    . ........    .*- +-         =           
    :.:            .  :..   -.        .:           
    .-..          ..  .     -          .           
         .:-..-:      .   .-=-                     
       .:::.   .-:         ==.                     
            .:.                                    
               . ...                               



for i in range(len(description_lines)):
	if 21 + i < len(card_img):
		card_img[21 + i] = description_lines[i]
	else:
		card_img.append(description_lines[i])



for line in card_img:
	print(line)
