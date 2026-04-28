import colorama
from colorama import Fore, Back, Style
colorama.init()

def run_program():
	valid_fore_colors = {
		"red": Fore.RED,
		"cyan": Fore.CYAN,
		"yellow": Fore.YELLOW
	}

	valid_back_colors = {
		"magenta": Back.MAGENTA,
		"white": Back.WHITE,
		"blue": Back.BLUE
	}

	valid_styles = {
		"dim": Style.DIM,
		"normal": Style.NORMAL,
		"bright": Style.BRIGHT
	}

	# Fore is foreground and Back is background and Style is just style
	# The above function will initialize the module

	print(Style.RESET_ALL + Fore.YELLOW + '\nWelcome to the colorama app!')

	user_fore_blue = input(Style.RESET_ALL + '\nEnter something: ' + Style.RESET_ALL)
	print(Fore.BLUE + user_fore_blue + Style.RESET_ALL + " is in blue color.")

	user_back_cyan = input('\nEnter something: ')
	print(Back.CYAN + user_back_cyan + Style.RESET_ALL + ' is in Cyan background color' + Style.RESET_ALL)

	user_style_dim = input('\nEnter something: ')
	print(Style.DIM + user_style_dim + Style.RESET_ALL + ' has a dim style\n' + Style.RESET_ALL)

	print("Now let's kick it up a notch. Please choose a Fore color (Red, Cyan, Yellow): ")
	while True:
		user_type1 = input().strip().lower()

		if user_type1 in valid_fore_colors:
			print(valid_fore_colors[user_type1] + f"This is your fore color.")
			break
		else:
			print("Invalid Color. Try again." + Style.RESET_ALL)

	print("\nYou're doing great! Now please pick a background color (Magenta, White, Blue): ")
	while True:
		user_type2 = input().strip().lower()

		if user_type2 in valid_back_colors:
			print(valid_back_colors[user_type2] + f"This is your background color.")
			break
		else:
			print("Invalid Color. Try again.")

	print("\nAwesome! Now just choose a style (Dim, Normal, Bright) and this program should be done...")
	while True:
		user_type3 = input().strip().lower()

		if user_type3 in valid_styles:
			print(valid_styles[user_type3] + f"This is your style and finsihed product.")
			break
		else:
			print("Invalid Stlye. Try again.")

while True:
	run_program()

	while True:
		repeat = input("\nDo you want to run this program again? (yes/no): ").strip().lower()
		
		if repeat in ['yes', 'y']:
			break
		elif repeat in ['no', 'n']:
			print("\nProgram terminated.")
			exit()
		elif repeat in ['theflag']:
			print("\n{here_is_your_flag}")
		else:
			print("Invalid Input.")
