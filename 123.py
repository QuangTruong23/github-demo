from random import randint
print ("Nhap Dam, La, Keo: ")

player = str (input())
computer = randint(0,2)

if computer == 0:
	computer = "Dam"
if computer == 1:
	computer = "La"
if computer == 2:
	computer = "Keo"
print("-----")
print("You choose "+ player)
print("computer Chooses "+ computer)
print("-----")
if plyer == compuer :
	print("Draw")
else:
	if player == "Keo":
		if computer == "Dam":
			print("Lose")
		if computer == "La":
			print("Win")
	if player == "Dam":
		if computer == "Keo":
			print("Win")	
		if computer == "La":
			print("Lose")		
	if player == "La":
		if computer == "Keo":
			print("Lose")
		if computer == "Dam":
			print("Win")
