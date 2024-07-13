print("Rules to win the game ROCK-PAPER-SCISSORS:\n",
      "1.Rock vs Paper --> Paper wins\n",
      "2.Paper vs Scissors --> Scissors win\n",
      "3.Rock vs Scissors --> Rock wins\n")

while True:
  print("select the choice\n1.Rock \n2.Paper \n3.Scissors\n")
  print(".............................................................")
  choice=int(input("Enter the choice:"))
  while choice>3 or choice<1:
    choice=int(input("Please enter the valid choice..."))
    print(".............................................................")  
  if choice==1:
      Choice_name="Rock"
  elif choice==2:
      Choice_name="Paper"
  else:
      Choice_name="Scissors" 

  print("User's choice is ",Choice_name) 

  print(".............................................................")
  print("Now it's Computer's Turn")

  import random
  Comp_Choice=random.randint(1,3)

  while Comp_Choice==choice:
      Comp_Choice=random.randint(1,3)

  if Comp_Choice==1:
        Comp_Choice_name="Rock"
  elif Comp_Choice==2:
        Comp_Choice_name="Paper"
  else:
        Comp_Choice_name="Scissors"

  print("Computer's choice is",Comp_Choice_name)  
  print(".............................................................")

  if choice==Comp_Choice:
        print("IT'S A DRAW")
        result="DRAW"

  if choice==1 and Comp_Choice==2:
        print("Rock VS Paper -->> Paper wins")
        result="Paper"
  elif choice==2 and Comp_Choice==1:
        print("Paer VS Rock -->> Paper wins")
        result="Paper"

  if choice==2 and Comp_Choice==3:
        print("Paper VS Scissors-->> Scissors wins")
        result="Scissors"
  elif choice==3 and Comp_Choice==2:
        print("Paer VS Scissors -->> Scissors wins")
        result="Scissors" 

  if choice==1 and Comp_Choice==3:
        print("Rock VS Scissors -->> Rock wins")
        result="Rock"
  elif choice==2 and Comp_Choice==1:
        print("Rock VS Scissors -->> Rock wins")
        result="Rock"

  if result=="DRAW":
        print("....IT'S TIE....")
  if result==Choice_name:
        print("....USER WINS....")  
  else:
        print("....COMPUTER WINS....")  

  print("Do you want to play again?\n" "YES/NO")
  ans=input().lower()
  if ans=="no":
        break
  print(".............................................................") 
  print(".............................................................") 

print("***THANKS FOR PLAYING***")
