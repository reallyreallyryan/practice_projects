# BJJ Sub Mission v3.1
import random
import sys

#function to run script
def sub_mission():
    global counter
    global user
    global sub_options_gi
    global sub_options_nogi
    global pos_options
    
    #counter for subs completed
    counter = 0
    #lists of gi/ no gi/ position options
    sub_options_gi = ['kneebar', 'armbar', 'bow and arrow', 'collar choke']
    sub_options_nogi = ['triangle', 'arm triangle', 'darce', 'americana']
    pos_options = ['side control', 'mount', 'back', 'guard']
    #get randcom choice from lists
    gi_choice = random.choice(sub_options_gi)
    nogi_choice = random.choice(sub_options_nogi)
    pos_choice = random.choice(pos_options)
    # asks for user, chooses 1 of 3 options
    user = input("This is the BJJ Sub Mission!\nAre you in Gi (G) or No-Gi? (NG): ").upper()
    if user == 'G':
        print("Your sub mission today is: " + str(gi_choice) + " from " + str(pos_choice))
    elif user == 'NG':
        print("Your sub mission today is: " + str(nogi_choice) + " from " + str(pos_choice))
    else:
        sys.exit("Come back when you wanna roll.")
#the user_result function prints here
    def user_result():
        global counter
        #asks for user input
        result = input("Did you complete your mission? (Y/N)").upper()
        if result == 'Y':
            #is 'yes' counter goes up 1, asks for user input to continue
            counter += 1
            retry = input("Good job! You've done " + str(counter) + " subs.\nDo you want to try again? (Y/N)").upper()
            #if user wants to continue -> ongoing_mission function starts
            if retry == 'Y':
                print(ongoing_mission())
            else:
                sys.exit("Thanks for rolling. Your final sub mission score is: " + str(counter))
        else:
            sys.exit("Maybe next time!")
    #similar function to user_result but this loops
    
    def ongoing_mission():
        global user
        global counter
        global sub_options_gi
        global sub_options_nogi
        global pos_options
        
        #establish new random choices for ongoing loop
        new_gi_choice = random.choice(sub_options_gi)
        new_nogi_choice = random.choice(sub_options_nogi)
        new_pos_choice = random.choice(pos_options)
        #if user picked 'gi' or 'no-gi' from start
        if user == 'G':
            print("Your next sub mission today is: " + str(new_gi_choice) + " from " + str(new_pos_choice))
        elif user == 'NG':
            print("Your next sub mission today is: " + str(new_nogi_choice) + " from " + str(new_pos_choice))
        else:
            sys.exit("Come back when you wanna roll.")
        #asks user input if sub was completed
        next_result = input("Did you complete this mission? (Y/N)").upper()
        if next_result == "Y":
            #if 'yes' counter goes up 1 and user is asked to continue
            counter += 1
            next_retry = input("Good job! You've done " + str(counter) + " subs.\nDo you want to try again? (Y/N)").upper()
            #if user continues, return the same function
            if next_retry == 'Y':
                print(ongoing_mission())
            else:
                sys.exit("Thanks for playing! Your final sub mission score is: " + str(counter))
        else:
            sys.exit("Nice work today. You've done " + str(counter) + " subs.")
    # after presenting user sub, code then runs through user_result function
    #function printed from above
    print(user_result())

#start the script
print(sub_mission())
