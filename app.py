# Project is still not finished

from os.path import exists
import os
import tkinter as tk

def genDir():
	# Score Board Records
	dir_name = "SBR"
	try:
		os.mkdir(dir_name)
		print(f"{dir_name} directory created.")
	except FileExistsError:
		print(f"Directory exists")
	except PermissionError:
		print(f"You do not have the permissions to create directory.")
	except Exception as e:
		print(f"Error occured: {e}")

	PATH = "./" +  dir_name + "/"
	
	fileNames = ["label", "P1", "scrP1", "P2", "scrP2"]

	for file in fileNames:
		filePath = PATH + file + ".txt"
		if not exists(filePath):
			with open(filePath, "w") as f:
				pass

def callback(P):
	return str.isdigit(P) or P == ""

def writeScore():
	pass

root = tk.Tk()
root.title("Score Board Editor")
height = 400
width = 600
root.geometry(str(width) + "x" + str(height))

p1L = tk.Label(root, text = "Player 1")
p1L.pack()
p1 = tk.Text(root, height=1, width=15)
p1.pack()

p2L = tk.Label(root, text = "Player 2")
p2L.pack()
p2 = tk.Text(root, height=1, width=15)
p2.pack()

button = tk.Button(root,
				   text="Submit",
				   command=writeScore,
				   height=1,
				   padx=10,
				   pady=5,
				   width=5,
				   wraplength=100)

button.pack(side="bottom", padx=20, pady=20)

genDir()

root.mainloop()
