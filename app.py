# Project basically finished

from os.path import exists
import os
import tkinter as tk

# Score Board Records
# This is the directory names
dir_name = "SBR"

# Path to the SBR directory
PATH = "./" +  dir_name + "/"

# Generate directory if it does not exist.
def genDir():

	try:
		os.mkdir(dir_name)
		print(f"{dir_name} directory created.")
	except FileExistsError:
		print(f"Directory exists")
	except PermissionError:
		print(f"You do not have the permissions to create directory.")
	except Exception as e:
		print(f"Error occured: {e}")

	# File names
	fileNames = ["label", "P1", "scrP1", "P2", "scrP2"]

	# Generate files
	for file in fileNames:
		filePath = PATH + file + ".txt"
		if not exists(filePath):
			with open(filePath, "w") as f:
				pass
		
# Retrieve the data from files and added to the text inputs
def retrieveData():
	global tLabel, p1, p1Scr, p2, p2Scr

	with open(PATH + "label.txt", "r") as f:
		val = f.readline()
	tLabel.insert(0, val)
	
	with open(PATH + "P1.txt", "r") as f:
		val = f.readline()
	p1.insert(0, val)

	with open(PATH + "scrP1.txt", "r") as f:
		val = f.readline()
		if not val:
			val = "0"
	p1Scr.insert(0, val)

	with open(PATH + "P2.txt", "r") as f:
		val = f.readline()
	p2.insert(0, val)

	with open(PATH + "scrP2.txt", "r") as f:
		val = f.readline()
		if not val:
			val = "0"
	p2Scr.insert(0, val)

# Check if value is a number
def isNumber(P):
	return str.isdigit(P) or P == ""

# Switch player position in scoreboard
def switchPlayers():
	global p1, p2
	val = str(p1.get())
	p1.delete(0, tk.END)
	p1.insert(0, p2.get())
	p2.delete(0, tk.END)
	p2.insert(0, val)

# Clear all of the content in each text input
def clearContent():
	global tLabel, p1, p1Scr, p2, p2Scr
	tLabel.delete(0, tk.END)
	p1.delete(0, tk.END)
	p2.delete(0, tk.END)
	p1Scr.delete(0, tk.END)
	p2Scr.delete(0, tk.END)

	# Add 0 as it is the default value
	p1Scr.insert(0, '0')
	p2Scr.insert(0, '0')


# Submit the scores into there respective text files
def writeScore():
	global tLabel, p1, p1Scr, p2, p2Scr

	with open(PATH + "label.txt", "w") as f:
		f.write(str(tLabel.get()))
	
	with open(PATH + "P1.txt", "w") as f:
		f.write(str(p1.get()))

	p1S = p1Scr.get()
	if isNumber(p1S):
		with open(PATH + "scrP1.txt", "w") as f:
			f.write(str(p1S))

	with open(PATH + "P2.txt", "w") as f:
		f.write(str(p2.get()))

	p2S = p2Scr.get()
	if isNumber(p2S):
		with open(PATH + "scrP2.txt", "w") as f:
			f.write(str(p2S))

# Initiate window
root = tk.Tk()
root.title("Score Board Editor")
height = 400
width = 600
root.geometry(str(width) + "x" + str(height))

# Initiate each text input

tLabelL = tk.Label(root, text = "Label")
tLabelL.pack()
tLabel = tk.Entry(root, width=20)
tLabel.pack()

p1L = tk.Label(root, text = "Player 1")
p1L.pack()
p1 = tk.Entry(root, width=30)
p1.pack()
p1Scr = tk.Entry(root, width=2)
p1Scr.pack()

p2L = tk.Label(root, text = "Player 2")
p2L.pack()
p2 = tk.Entry(root, width=30)
p2.pack()
p2Scr = tk.Entry(root, width=2)
p2Scr.pack()

# Initiate switch button

switchButton = tk.Button(root,
				   text="Switch Players",
				   command=switchPlayers,
				   height=1,
				   padx=10,
				   pady=5,
				   width=15,
				   wraplength=100)

switchButton.pack(side="left", padx=20, pady=20)

# Initiate clear button

clearButton = tk.Button(root,
				   text="Clear",
				   command=clearContent,
				   height=1,
				   padx=10,
				   pady=3,
				   width=5,
				   wraplength=100)

clearButton.pack(side="left", padx=20, pady=20)

# Initiate exit button

exitButton = tk.Button(root,
				   text="Exit",
				   command=root.quit,
				   height=1,
				   padx=10,
				   pady=5,
				   width=5,
				   wraplength=100)

exitButton.pack(side="right", padx=20, pady=20)

# Initiate submit button

submitButton = tk.Button(root,
				   text="Submit",
				   command=writeScore,
				   height=1,
				   padx=10,
				   pady=5,
				   width=5,
				   wraplength=100)

submitButton.pack(side="right", padx=20, pady=20)



genDir()
retrieveData()

root.mainloop()
