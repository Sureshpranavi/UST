print("\n")

print("*"*50)
print("\t Welcome all to Snake Water Game")
print("*"*50)
print("\n")
player1=input("enter the player name 1 = ")
player2=input("enter the player name 2 = ")


while(True):
	print( "\nSelect your options : \n Snake\n Water\n Gun\n")
	p1_choice=input("enter p1 the option =")
	p2_choice=input("enter p2 the option =")

	if(p1_choice=="Gun" and p2_choice=="Snake"):
		print(player1,"win the game with choice of ",p1_choice)
		break
	elif(p1_choice=="Water" and p2_choice=="Gun"):
		print(player2,"win the game with choice of ",p2_choice)
		break
	elif(p1_choice==p2_choice):
		print("Game was Tie , both selected option : ",p1_choice)
		break

