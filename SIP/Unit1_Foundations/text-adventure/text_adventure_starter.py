start = """
You are walking home from your friend's house one day.
You come to a crossroads, and can go either left or right.
Type 'left' to go left or 'right' to go right.
"""
print(start)
user_input = input()
if user_input == "left":
    print("You decide to go left and find a large dog.") # finished the story by writing what happens
    print("The dog is skin and bones, and looks up at you, whining. Do you take the dog home or to a shelter?")
    doggy=input("Type 'home' to take the dog home or 'shelter' to take the dog to a shelter:" )
    if doggy=="home":
        print ("After you take the dog home, the dog changes into a man and thanks you for opening your home to him. Do you kick him out, or allow him to stay?")
        home=input ("Type 'Kick him out' to kick him out or type 'Stay' to allow him to stay.")
        if home=="Kick him out":
            print("You scream and try to push him out of your house. Two days later, when you dare leave your house to get groceries, a dog that looks similar approaches. You bend down to pet him, and he jumps up to bite your cheek. You bleed out in the street.")
            print("The End!")
        elif home=="Stay":
            print("You allow the man to stay, and never suffer from burglaries because you have a large guard dog. Eventually, you start charging him rent, and now have a large disposable income, in addition to your salary from your job.")
    elif doggy=="shelter":
        print("You take the dog to the local shelter. The caretaker promises to take good care of him, and you leave. As you leave, you pet the dog once again, and continue on your way home.")
        print("The End!")
    else:
        print ("Please choose an answer that will continue the story.")

elif user_input == "right":
    print("You choose to go right and find a young boy staring at you.") # finished the story writing what happens
    print("You approach the boy. You're shocked to see that he's floating off of the ground.")
    fear=input("Do you show any signs of fear. Type 'scream' for yes, and 'shock' for no.")
    if fear=="scream":
        print ("You scream and bolt from the boy. You run back to your home. You're shocked to see the boy float through the wall not two minutes later.")
        listen=input("You resign yourself to his haunting, but he says he only wants you to listen to his story. Do you want to  listen? Yes or No?")
        if listen=="no" or listen=="yes":
            print("He begins to talk. He tells you that his name was Dylan, and he was 13 years old.")
            print("He was murdered, and his killer was never found. His body was dumped in a river, and never found.")
            print("He tells you that you were the only person to ever listen to his story, and as a result, his wandering has ended.")
    elif fear=="shock":
        print ("You take a step backwards, and the boy follows. You walk back to the corner, and he follows again. You can either lead him to your home, or an exorcist.")
        destination=input("Type 'home' to lead him home, or 'exorcist' to lead him to an exorcist.")
        if destination=="home":
            print("You walk back to your home. You're not really shocked to see the boy float through the wall not two minutes later.")
            listen=input("You resign yourself to his haunting, but he says he only wants you to listen to his story. Do you want to  listen? Yes or No?")
            if listen=="no" or listen=="yes":
                print("He begins to talk. He tells you that his name was Dylan, and he was 13 years old.")
                print("He was murdered, and his killer was never found. His body was dumped in a river, and never found.")
                print("He tells you that you were the only person to ever listen to his story, and as a result, his wandering has ended.")
        elif destination=="exorcist":
            print("You slowly walk towards a known exorcist in your area, but as soon as you approach the building, the boy disappears. Thinking nothing of it, you go home.")
            print("Two days later, young children and teens begin to appear in your home. ")
            print("You go through the rest of your life, being haunted by the ghosts of young teens and children.")
            print("The End!")
        else:
            print ("Please choose an answer that will continue the story.")
    else:
        print ("Please choose an answer that will continue the story.")

else:
    print ("Please choose an answer that will continue the story.")
