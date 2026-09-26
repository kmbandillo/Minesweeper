import random
import os
import graphics
import pickle
#Function for putting tabs for multiple lines
def printFormat(n,var):
	for line in var.split("\n"):
		t= "\t"*n
		newformat = "{}{}".format(t,line)
		print(newformat)

#Function for putting tabs for single line
def printFormat_(n,str):
	t= "\t"*n
	newFormat = "{}{}".format(t,str)
	return newFormat

# Function for clearing the terminal
def clear():
	os.system("cls")
clear()

# Function to display the instructions
def instructions():
	print("Instructions:")
	print("1. To reveal a cell, enter row and column (ex. 1 A)")
	print("2. To place a flag, enter row and column followed by 'F' (ex. 1 A F)")
	print("3. To save, enter 'S'. To load enter 'L'. ")
	print("4. To return to menu enter 'M' ")

def error():	#For invalid inputs
	print("INVALID INPUT!")
	print(instructions())
	input("---- Press 'ENTER' to return to game ---- ")

#Functions for game displays
def banner():
	clear()
	b = graphics.banner()
	printFormat(1,b)

def menu():	
	clear()
	banner()
	m = graphics.menu()
	printFormat(2,m)
	choice = input(printFormat_(7,"CHOICE: ")) #Function that display the choice input to the center
	return choice

def noSaved():
	clear()
	banner()
	n = graphics.noSaved()
	printFormat(2,n)

def mainInstructions():
	clear()
	banner()
	i = graphics.instructions()
	printFormat(2,i)
	input()

def saveArt():
	clear()
	banner()
	s = graphics.saveArt()
	printFormat(2,s)
	input()

def loadArt():
	clear()
	banner()
	o = graphics.loadArt()
	printFormat(2,o)
	input()

def win():
	clear()
	banner()
	w = graphics.winArt()
	printFormat(2,w)
	input()

def lose():
	clear()
	banner()
	l = graphics.loseArt()
	printFormat(2,l)
	input()

def exitArt():
	e = graphics.exitArt()
	printFormat(2,e)
	input()

data= {}

#PROGRAM START
#Functions that displays the start of the game
def play(data):
	game(data)

def game(data):

	n = data["n"]
	mines_no = data["mines_no"]

	#GRID
	def print_grid(data):
		clear()
		mine_values = data["mine_values"]
		n = data["n"]

		print()
		

		l = "   "
		letters = ["A","B","C","D","E","F","G","H","I","J"]
		
		for i in range(0,n):
			l = l + "      " + str(letters[i])

		printFormat(3,l)	

		# l = lines
		# r = row
		# c = column
		for r in range(n+1):
			l = "     "
			if r == 0:
				for c in range(n+1):
					if c == 0:
						l = l + "╔══════"
					elif c < n-1:
						l = l + "╦══════"
					elif c == n:
						l = l + "╦══════╗"
				printFormat(3,l)		

				#Provides the vertical number in the left side of the grid
				l = "  " + str(r+1) + "  "    
				for c in range(n):
					l = l + "║   " + str(mine_values[r][c]) + "  "
				printFormat(3,l + "║")		

				#Provide spaces for the grid
				l = "     "					
				for c in range(n):
					l = l + "║      "
				printFormat(3,l + "║")

			#Provide lines for the lowest part of the grid
			elif r == n:						
				l = "     "
				for c in range(n):
					if c == 0:
						l = l + "╚══════"
					elif c < n-1:
						l = l + "╩══════"
					elif c == n-1:
						l = l + "╩══════╝"
				printFormat(3,l)

			#Provides lines in the middle part of the grid
			elif r < n:							
				l = "     "
				for c in range(n+1):
					if c == 0:
						l = l + "╠══════"
					elif c < n-1:
						l = l + "╬══════"
					elif c == n:
						l = l + "╬══════╣"
				printFormat(3,l)

				if r + 1 < 10:
					l = "  " + str(r+1) + "  "    #Provides the vertical number in the left side of the grid
					for c in range(n):
						l = l + "║   " + str(mine_values[r][c]) + "  "
					printFormat(3,l + "║")
				
				if r + 1 == 10:
					l = " " + str(r+1) + "  "    #Provides the vertical number in the left side of the grid
					for c in range(n):
						l = l + "║   " + str(mine_values[r][c]) + "  "
					printFormat(3,l + "║")

				l = "     "			#Provide spaces for the grid
				for c in range(n):
					l = l + "║      "
				printFormat(3,l + "║")

		print()
		return data
	
	global checked
	# Function for setting up Mines
	def set_mines(data):
		numbers = data["numbers"]
		mines_no = data["mines_no"]
		n = data["n"]

		mine_count = 0

		while mine_count < mines_no:
			val = random.randint(0, n * n - 1)
			r = val // n
			c = val % n

			if numbers[r][c] != -1:
				numbers[r][c] = -1
				mine_count += 1

		return data

	# Function for setting up the other grid values
	def set_values(data):

		numbers = data["numbers"]
		n = data["n"]
		# Loop for counting each cell value

		for r in range(n):
			for c in range(n):

				# Skip, if it contains a mine
				if numbers[r][c] == -1:
					continue
				
				#upper-left	
				if r > 0 and c > 0 and numbers[r-1][c-1] == -1:
					numbers[r][c] = numbers[r][c] + 1
				#up	
				if r > 0 and numbers[r-1][c] == -1:
					numbers[r][c] = numbers[r][c] + 1
				#upper-right
				if r > 0 and c < n-1 and numbers[r-1][c+1] == -1:
					numbers[r][c] = numbers[r][c] + 1
				#right
				if c < n-1 and numbers[r][c+1] == -1:
					numbers[r][c] = numbers[r][c] + 1
				#left
				if c > 0 and numbers[r][c-1] == -1:
					numbers[r][c] = numbers[r][c] + 1
				#lower-left	
				if r < n-1 and c > 0 and numbers[r+1][c-1] == -1:
					numbers[r][c] = numbers[r][c] + 1
				#down	
				if r < n-1  and numbers[r+1][c] == -1:
					numbers[r][c] = numbers[r][c] + 1
				#lower-right
				if r < n-1 and c < n-1 and numbers[r+1][c+1] == -1:
					numbers[r][c] = numbers[r][c] + 1
		return data

	# Shows cells with value of zero
	def surrounding_cells(r, c):
		n = data["n"]
		mine_values = data["mine_values"]
		numbers = data["numbers"]
		global checked

		# To check if the cell has not yet been visited
		if [r,c] not in checked:

			# Mark the cell visited
			checked.append([r,c])

			if numbers[r][c] == 0:

				# Reveals the value on grid
				mine_values[r][c] = numbers[r][c]

				# Recursive calls for the surrounding cells
				if r > 0:
					surrounding_cells(r-1, c)
				if r < n-1:
					surrounding_cells(r+1, c)
				if c > 0:
					surrounding_cells(r, c-1)
				if c < n-1:
					surrounding_cells(r, c+1)	
				if r > 0 and c > 0:
					surrounding_cells(r-1, c-1)
				if r > 0 and c < n-1:
					surrounding_cells(r-1, c+1)
				if r < n-1 and c > 0:
					surrounding_cells(r+1, c-1)
				if r < n-1 and c < n-1:
					surrounding_cells(r+1, c+1)	

			# If the cell is not zero-valued 			
			if numbers[r][c] != 0:
				mine_values[r][c] = numbers[r][c]
		return data

	# Function to check for completion of the game
	def game_finished():
		mine_values = data["mine_values"]
		n = data["n"]
		mines_no = data["mines_no"]

		count = 0

		for r in range(n):
			for c in range(n):

				# Checking if cell is empty or flagged
				if mine_values[r][c] != ' ' and mine_values[r][c] != "F":
					count = count + 1
				
		if count == n * n - mines_no:
			return True  
		else:
			return False
						
	def reveal_values(data): #Reveals values when the game is over
		mine_values = data["mine_values"]
		numbers = data["numbers"]
		n = data["n"]

		for r in range(n):
			for c in range(n):
				if numbers[r][c] == -1:
					mine_values[r][c] = "*"
				else:
					mine_values[r][c] = numbers[r][c]
		return data
								
	if __name__ == "__main__":
		n = data["n"]

		# Values of the grid
		data["numbers"] = [[0 for y in range(int(n))] for x in range(int(n))] 
		# The display values of the grid
		data["mine_values"] = [[' ' for y in range(int(n))] for x in range(int(n))]
		
		# The positions that have been flagged
		f = []
		data["flags"] = f
		flags = data["flags"]

		numbers = data["numbers"]
		mine_values = data["mine_values"]

		set_mines(data)

		set_values(data)

		# Maintains the game loop
		over = False

		while not over:
			print_grid(data)
			printFormat(2, "To save enter 'S'. To load previous game enter 'L'.")

			# Input from the user
			input_ = input(printFormat_(2,"Enter row number and column name (ex. 1 A), flag the cell by adding 'F' (ex. 1 A F) = ")).split()
			data['input'] = input_
			raw_input = data['input']
			row_name = ["1","2","3","4","5","6","7","8","9","10"]   #Valid row names
			col_name = ["A","B","C","D","E","F","G","H","I","J","a","b","c","d","e","f","g","h","i","j"]	#Valid column names

			def save(data):

				if data["n"] == 8:
					filename = "easy"

				elif data["n"] == 9:
					filename = "average"

				elif data["n"] == 10:
					filename = "hard"

				else:
					return data

				game = open(filename, "w")

				# Board dimension
				game.write(str(data["n"]) + "\n")

				# Number of mines
				game.write(str(data["mines_no"]) + "\n")

				# Flags
				game.write(str(data["flags"]) + "\n")

				# mine_values
				for row in data["mine_values"]:
					game.write(",".join(map(str, row)) + "\n")

				# numbers
				for row in data["numbers"]:
					game.write(",".join(map(str, row)) + "\n")

				game.close()

				saveArt()

				return data
					
			if len(raw_input) == 1:
				if raw_input[0] == "s" or raw_input[0] == "S":	#FOR SAVING
					save(data)
					continue

				if raw_input[0] == "l" or raw_input[0] == "L":
					load(data)

					# Update local variables after loading
					n = data["n"]
					mines_no = data["mines_no"]
					numbers = data["numbers"]
					mine_values = data["mine_values"]
					flags = data["flags"]

					loadArt()
					continue

				if raw_input[0] == "m" or raw_input[0] == "M":	#FOR RETURNING TO MENU
					data.clear()
					break

				else:
					error()
					continue
					
			if len(raw_input) == 2:	#Replaces 0 in the val list
				
				if raw_input[1] not in col_name or len(raw_input[1]) != 1:
					error()

				else: #Converts column name(letter) into a digit by using its index
					for e in col_name:									      
						e = raw_input[1].lower()
						int_input = col_name.index(e)

				Input = [0,0]
				Input[0] = int(raw_input[0])
				Input[1] = int_input + 1

				# For picking cell positions
				if raw_input[0] not in row_name:  
					error()
					continue

				if raw_input[1] not in col_name:
					error()
					continue

				if len(raw_input[1]) != 1:
					error()
					continue

				if len(raw_input) < 1:
					error()
					continue
				
				else:
					try: 
						val = list(map(int, Input))

					except ValueError:
						error()
						continue

			# FOR SETTING FLAGS
			elif len(raw_input) == 3:
				if raw_input[2] != 'F' and raw_input[2] != 'f':	 
					error()
					continue
				
				elif raw_input[0] not in row_name:
					error()
					continue

				elif raw_input[1] not in col_name:
					error()
					continue

				elif len(raw_input[1]) != 1:
					error()
					continue

				else:
					for e in col_name:	#Converts column name(letter) into a digit by using its index								      
						e = raw_input[1].lower()
						int_input = col_name.index(e)
				
				#For picking cell positions and for other options while on game loop
				Input = [0,0,0]
				Input[0] = int(raw_input[0])
				Input[1] = int_input + 1
				Input[2] = raw_input[2]

				# Displays error when input is invalid
				try: 
					val = list(map(int, Input[:2]))

				except ValueError:
					error()
					continue

				# Get row and column numbers
				if len(Input) == 2 or len(Input) == 3:
					r = val[0]-1
					c = val[1]-1

				# If cell already been flagged
				if [r, c] in flags:
					clear()
					print_grid(data)
					printFormat(6,"Flag already set")
					input()
					continue

				# If cell already been displayed
				if mine_values[r][c] != ' ':
					clear()
					print_grid(data)
					printFormat(6,"Value already known")
					input()
					continue

				# Check the number for flags 	
				if len(flags) < mines_no:
					
					# Adding flag to the list
					flags.append([r, c])
					
					# Set the flag for display
					mine_values[r][c] = "F"
					continue
				else:
					clear()
					print_grid(data)
					printFormat(5,"Flags finished")
					input()
					continue	 
			else: 
				error()
				continue
				
			# Get row and column number
			r = val[0]-1
			c = val[1]-1

			# Unflag the cell if already flagged
			if [r, c] in flags:
				flags.remove([r, c])

			# If landing on a mine --- GAME OVER	
			if numbers[r][c] == -1:
				mine_values[r][c] = '*'
				reveal_values(data)
				print_grid(data)
				input()
				lose()
				data.clear()
				over = True
				continue

			# Reveals the cell value of surrounding zero-value or cell without mines around, when 0 is selected
			elif numbers[r][c] == 0:
				checked = []
				mine_values[r][c] = '0'
				surrounding_cells(r, c)

			# Reveals the value of cells with neighboring mines
			else:	
				mine_values[r][c] = numbers[r][c]

			# Check for game completion	
			if(game_finished()):
				reveal_values(data)
				print_grid(data)
				input()
				win()
				data.clear()
				over = True
				continue
			clear()
	return data

#EXIT GAME	
def exit():		
	clear()
	exitArt()

#LOAD GAME
def load(data):

    n = data["n"]

    if n == 8:
        filename = "easy"

    elif n == 9:
        filename = "average"

    elif n == 10:
        filename = "hard"

    else:
        return data

    game = open(filename, "r")

    data.clear()

    # n
    data["n"] = int(game.readline().strip())

    # mines
    data["mines_no"] = int(game.readline().strip())

    # flags
    flags_text = game.readline().strip()

    data["flags"] = []

    if flags_text != "[]":
        flags_text = flags_text.strip("[]")

        for flag in flags_text.split("], ["):
            flag = flag.replace("[", "").replace("]", "")
            r, c = map(int, flag.split(","))
            data["flags"].append([r, c])

    # mine_values
    data["mine_values"] = []

    for i in range(data["n"]):
        row = game.readline().rstrip("\n").split(",")

        row = [
            int(x.strip()) if x.strip() != "" else " "
            for x in row
        ]

        data["mine_values"].append(row)

    # numbers
    data["numbers"] = []

    for i in range(data["n"]):
        row = game.readline().rstrip("\n").split(",")

        row = [int(x.strip()) for x in row]

        data["numbers"].append(row)

    game.close()

    return data

#MAIN MENU
def main_menu():
	while True:
		choice = menu()
		if choice == "1":
			data["n"] = 8
			data["mines_no"] = 10
			play(data)
		elif choice == "2":
			data["n"] = 9
			data["mines_no"] = 20
			play(data)
		elif choice == "3":
			data["n"] = 10
			data["mines_no"] = 40
			play(data)
		elif choice == "4":
			mainInstructions()
		elif choice == "5":
			exit()
			break	
		else:
			print("INVALID INPUT")

main_menu()