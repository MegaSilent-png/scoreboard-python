# Project is still not finished

from os.path import exists
import os
import tkinter as tk

# Score Board Records
dir_name = "SBR"
fileNames = ["label", "P1", "scrP1", "P2", "scrP2"]
PATH = "./" +  dir_name + "/"

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

	for file in fileNames:
		filePath = PATH + file + ".txt"
		if not exists(filePath):
			with open(filePath, "w") as f:
				pass
		
def retrieveData():
	global tLabel, p1, p1Scr, p2, p2Scr

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

def callback(P):
	return str.isdigit(P) or P == ""

def switchPlayers():
	global p1, p2
	val = str(p1.get())
	p1.delete(0, tk.END)
	p1.insert(0, p2.get())
	p2.delete(0, tk.END)
	p2.insert(0, val)


def writeScore():
	global tLabel, p1, p1Scr, p2, p2Scr

	with open(PATH + "label.txt", "w") as f:
		f.write(str(tLabel.get()))
	
	with open(PATH + "P1.txt", "w") as f:
		f.write(str(p1.get()))

	p1S = p1Scr.get()
	if callback(p1S):
		with open(PATH + "scrP1.txt", "w") as f:
			f.write(str(p1S))

	with open(PATH + "P2.txt", "w") as f:
		f.write(str(p2.get()))

	p2S = p2Scr.get()
	if callback(p2S):
		with open(PATH + "scrP2.txt", "w") as f:
			f.write(str(p2S))

root = tk.Tk()
root.title("Score Board Editor")
height = 400
width = 600
root.geometry(str(width) + "x" + str(height))

tLabelL = tk.Label(root, text = "Label")
tLabelL.pack()
tLabel = tk.Entry(root, width=20)
tLabel.pack()

p1L = tk.Label(root, text = "Player 1")
p1L.pack()
p1 = tk.Entry(root, width=15)
p1.pack()
p1Scr = tk.Entry(root, width=2)
p1Scr.pack()

p2L = tk.Label(root, text = "Player 2")
p2L.pack()
p2 = tk.Entry(root, width=15)
p2.pack()
p2Scr = tk.Entry(root, width=2)
p2Scr.pack()



submitButton = tk.Button(root,
				   text="Submit",
				   command=writeScore,
				   height=1,
				   padx=10,
				   pady=5,
				   width=5,
				   wraplength=100)

submitButton.pack(side="bottom", padx=20, pady=20)

switchButton = tk.Button(root,
				   text="Switch Players",
				   command=switchPlayers,
				   height=1,
				   padx=10,
				   pady=5,
				   width=15,
				   wraplength=100)

switchButton.pack(side="bottom", padx=20, pady=20)

genDir()
retrieveData()

root.mainloop()
