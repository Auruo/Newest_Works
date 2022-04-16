import sys,time,random

##################
#                #
# Philip Squires #
#                #
##################

###########################################################################################################################################
##                                                                                                                                        #
## The following concepts are within this game:                                                                                           #
## while loops                                                                                                                            #
## utilizing sys and time functions to make new functions that make the text come to life and allow time to read                          #
## using random functions to make chances, to determine a stat, and to make a timer for text                                              #
## using booleans, integers, arrays, comparative operators, nested if/elif statements, user input capture and storage,                    #
## using the quit function, print & custom print functions (printSlow, printFast), and string variables.                                  #
##                                                                                                                                        #
###########################################################################################################################################

# Determines the speed at which text is displayed
text_speed = 140
text_speed2 = 210

# Two options, fast and slow
def printSlow(sentence):
    for character in sentence:
        sys.stdout.write(character) # writes single character
        sys.stdout.flush() # flushes between characters, required to work properly (took a while to figure that out)
        time.sleep(random.random()*10.0/text_speed) # Adds the delay
    print()
def printFast(sentence):
    for character in sentence:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/text_speed2)
    print()

# Main function
def game():
    
    # Declaring variables used throughout the game. 
    playerLuck = random.randint(0,100)
    playerLuckLevel = ""
    inPittsburgh = False
    decision1 = 0
    
    # Arrays to allow a multitude of different viable answers to each question
    answer1 = ["1", "one", "ONE","1."]
    answer2 = ["2","two","TWO","2."]
    answer3 = ["3","three","THREE","3."]
    answery = ["y","Y","YES","yes","Yes","yeah","YEAH","Yeah","yep","YEP","YERPADERPA"]
    answern = ["n","N","No","NO","no","nah","nope","NOPE","NAH"]
    
    # Beginning of game
    printFast("***************")
    printSlow("*** WELCOME ***")
    printFast("***************")
    
    # Ask for the players name
    playerName = input('What is your name? ')
    
    # incorporate name in the games title, which isn't a great idea for a real game, but seemed okay for this
    print("**Welcome to",playerName,"travels forward in time**")
    printSlow("The goal of this game is to get back to 1988 by making the right decisions, which may not be the morally 'good' decisions, without dying.")
    printSlow("Decisions are made by answering 'y' or 'n' or choosing a number from a list of responses, for example '1' or '2'")
    printFast("First things first, your game-changing stat:")
    
    # Using if statements to determine your luck level.
    if playerLuck < 20:
        playerLuckLevel = "Very Bad"
    if playerLuck > 19 < 40:
        playerLuckLevel = "Bad"
    if playerLuck > 39 < 60:
        playerLuckLevel = "Okay"
    if playerLuck > 59: # "Good" range is large so all chances are still chances
        playerLuckLevel = "Good"
    print("Luck:",playerLuckLevel)
    printFast("Your luck influences various parts of the game for your character.")
    printSlow("You may want to avoid risks depending on your luck. Some decision paths require a lot of luck, some require little or no luck.")
    printSlow("Just keep in mind, some actions will fail with low luck and some will fail no matter what.")
    printSlow("Additionally, very dangerous decisions are mostly avoidable, but if faced with one can lead to death quite easily depending on luck.")
    
    # Allows you to infinitely re-roll your luck to more certainly get better or worse outcomes from luck-based decisions.
    # No exact number is given intentionally.
    # Added this to show I can use loops and to add some unpredictability to the game itself
    choice = input("Would you like to reroll? Y/N: ")
    while choice in answery:
        playerLuck = random.randint(0,100)
        if playerLuck < 20:
            playerLuckLevel = "Very Bad"
        if playerLuck >= 20 & playerLuck <= 40:
            playerLuckLevel = "Bad"
        if playerLuck > 40 & playerLuck <= 60:
            playerLuckLevel = "Okay"
        if playerLuck > 60:
            playerLuckLevel = "Good"
        print("Luck: ",playerLuckLevel)
        choice = input("Reroll again?(Y/N) ")
    
    print()
    printSlow("THE ADVENTURE BEGINS:")
    printFast("You're a VCR salesman from the year 1988. You suddenly awake in an entirely different place.")
    printFast("You stand up from the compacted dirt and look around to see nothing but corn fields surrounding you.")
    printFast("You smell decay, like that of the beach. A strong salty breeze is swaying the corn.")
    printFast("You stand up and as you brush yourself off an elderly stranger approaches you, dressed in overalls with a long beard, looks like he's ex-amish.")
    printFast("STRANGER: What are you doing on my farm?!")
    printSlow("You're disoriented, what do you do?")
    printFast("1. Lie")
    printFast("2. Be honest")
    printFast("3. Run away")
    
    # Because of the nature of Python, I can just use one variable (choice) to store and determine paths throughout the game
    choice = input("Select a numbered option, e.g. '1' '2' or '3': ")
    
    # If you choose to run away, you leave without any knowledge of your situation. That is tracked via "decision1"
    if choice in answer3:
        decision1 = 1
        choice = 3
    
    # If you choose to lie, the stranger may or may not believe you depending on the random number vs your luck level
    if choice in answer1:
        if playerLuck > random.randint(30, 60):
            printSlow("YOU: Well, I'm going through haze week at the moment.")
            printSlow("STRANGER: You stupid college kids always messing with my corn field. Get before I call the police!")
            printSlow("You beginning walking down the driveway.")
            printSlow("YOU: Sorry to bother you, but do you happen to know where are we?")
            printSlow("STRANGER: You're a few miles outside Pittsburgh.")
            printSlow("YOU: Again, so sorry, I'm going to leave, but which way to Pittsburgh?")
            printSlow("STRANGER: Take a left out the driveway, now GET!")
            decision1 = 2
            choice = 3
        else:
            printSlow("YOU: Sorry, I thought this was a McDonalds")
            printSlow("STRANGER: Something is seriously wrong with you, I'm calling the police. Don't move.")
            printSlow("As he calls the police, you begin to panic.")
            printSlow("1. Don't move, wait for the police to arrive.")
            printSlow("2. Run away")
            choice = input("What do you do? ")
            
            # Nested if statements allow paths within paths that can either lead back to the main storyline or end the game
            if choice in answer1:
                printSlow("You wait for the police to arrive, still disoriented.")
                printSlow("'Good, maybe the police can help me figure out how I got here' you think.")
                printSlow("As the police race up the driveway in a TANK with lights and sirens blaring you begin to sweat")
                printSlow("You clinch your entire body")
                printSlow("The police jump out of their tank, guns drawn, shouting indiscernible instructions at you")
                printSlow("You have no idea what they're saying and yell 'what?!'")
                printSlow("OFFICERS: COMPLY OR DIE!")
                printSlow("YOU: I CAN'T UNDERSTAND YOU WHEN YOU BOTH TALK AT THE SAME T............")
                printSlow("Gunshots deafen your ears, you look down to see multiple wounds before collapsing on the ground.")
                printSlow("GAME OVER, you died without making it back to 1988.")
                quit()
            
            # Essentially puts you back on the main path, but also you still leave with no knowledge having made relatively bad decisions
            # that affect the rest of the game
            if choice in answer2:
                decision1 = 1
                choice = 3
                # Decision1 = 1 is having no knowledge, decision1 = 2 is leaving with knowledge
                
    if choice in answer2:
        printSlow("YOU: I don't know where I am or how I got here!")
        printSlow("STRANGER: Are you on drugs er summ'n buddy?")
        printSlow("YOU: No, I'm just lost!")
        printSlow("STRANGER: Well, you're about a half hour outside Pittsburgh, right smack dab in the middle, between the beach and the city.")
        printSlow("YOU: The beach? The ocean is a state away isn't it?")
        printSlow("STRANGER: The beach been in Pennsylvania for almost fifty years. My granpappy Bart remembers when the ocean was out that far.")
        printSlow("YOU: What year is it?!")
        printSlow("STRANGER: 2108 of course. You alright? You sure you haven't been on the sauce awhile?")
        printSlow("'Well, at least the venacular hasn't changed around here' you think to yourself.")
        printSlow("YOU: 2108? Oh man...I gotta go.")
        printSlow("YOU: Which way to Pittsburgh?")
        printSlow("STRANGER: Hang a left out the driveway.")
        printSlow("YOU: THANK YOU!")
        decision1 = 2
        choice = 3
        
    if choice == 3:
        printSlow("You begin running down the driveway towards the road in the distance.")
        printSlow("You get to the road and look around, there's seems to be nothing but corn.")
        
        # Different text depending on whether you gathered intel earlier
        if decision1 == 1:
            printSlow("You take a right turn out of the driveway and start walking up the road.")
        if decision1 == 2:
            printSlow("You take a left turn out of the driveway, headed to Pittsburgh.")
        printSlow("You start thinking of how to get there faster.")    
        printSlow("1. Try to hitchhike as you walk down the road")
        printSlow("2. Walk down the road without hitchhiking")
        choice = input("What will you do? ")
        
        # If you pick option 1 and have knowledge
        if choice in answer1 and decision1 == 2:
            printSlow("You raise your thumb as you walk down the road.")
            printSlow("After half an hour, an Amish buggy offers you a ride.")
            choice = input("Do you take the ride from them? ")
            
            if choice in answery:
                printSlow("YOU: Thanks for the ride!")
                printSlow("AMISH: No problem, where you headed?")
                printSlow("YOU: I'm headed to the nearest...science laboratory?")
                printSlow("AMISH: Well, that sounds like the work of the devil, but we can drop you off in Pittsburgh.")
                printSlow("YOU: That would be great, thank you.")
                printSlow("FIVE HOURS LATER")
                printSlow("YOU: Thanks for the ride Jebadiah!")
                printSlow("AMISH: That's not my name.")
                printSlow("As you walk away you wonder what he could be talking about. Every amish man is named Jebadiah, aren't they?")
                inPittsburgh = True
                
            if choice in answern:
                printSlow("You decline the ride and continue walking, following signs for Pittsburgh.")
                printSlow("After a few hours you see the tall buildings of Pittsburgh in the distance.")
                inPittsburgh = True
        
        # If you pick option 1 and have no knowledge        
        elif choice in answer1 and decision1 == 1:
            printSlow("You begin walking down the road with your thumb in the air. You have got to get back home.")
            printSlow("After an hour, someone pulls over in front of you. It's a work van.")
            printSlow("You run up to the driver-side window.")
            printSlow("YOU: Hi, thanks so much for stopping.")
            printSlow("MAN: Get in.")
            printSlow("You hop in the van, but feel a little creeped out by the man.")
            printSlow("YOU: Can you take me to Pittsburgh...also...what year is it?")
            printSlow("MAN: It's 2108, duh. Uh...buddy you're over an hour from Pittsburgh, you were going in the wrong direction and I'm not headed there.")
            printSlow("You get a bad feeling from this guy when suddenly he locks the doors. Your face changes to one of fear. What is he doing?")
            printSlow("MAN: I'm headed to West Virginia, now give me all your Bezos Bucks!")
            printSlow("He slowly raises a gun from his left side holster.")
            printSlow("1. Try to punch the man and reach over him to unlock the door.")
            printSlow("2. Try to grab the gun from the man.")
            choice = input("What will you do? ")
            
            # Random low odds of survival in the situation determined by the chance1/chance2 variables
            chance1 = random.randint(40,80)
            chance2 = random.randint(60,100)
            if choice in answer1 and playerLuck > chance1:
                printSlow("You punch the man and his head smacks the window, knocking him out. You immediately unlock the door and stumble from the van, shaking.")
                printSlow("The future is hellish, you think as you run away from the van, this time in the right direction.")
                printSlow("You run down the street, going the right direction. You dare not ask for a ride.")
            if choice in answer1 and playerLuck < chance1:
                printSlow("You punch the man but you slipped and the punch was more of a tap. The man immediately shoots you.")
                printSlow("GAME OVER: You were too unlucky.")
                quit()
            if choice in answer2 and playerLuck > chance2:
                printSlow("You successfully disarm the man.")
                printSlow("1. Tell the man to drive you to Pittsburgh.")
                printSlow("2. Get out and walk to Pittsburgh with his gun.")
                choice = input("What will you do? ")
                if choice in answer1:
                    printSlow("The man drives you to Pittsburgh, you have his gun on him the whole time.")
                    inPittsburgh = True
                if choice in answer2:
                    printSlow("You tell him to unlock the door and he lets you out.")
                    printSlow("You run down the street, going the right direction. You dare not ask for a ride.")
                    printSlow("Eventually, you see the tall buildings of Pittsburgh line the horizon.")
                    inPittsburgh = True
            if choice in answer2 and playerLuck < chance2:
                printSlow("You grab for the gun and he pulls the trigger")
                printSlow("GAME OVER: You died.")
                quit()
                
        # if you choose answer 2 and have no knowledge        
        elif choice in answer2 and decision1 == 1:
            printSlow("You walk down the road for what feels like endless hours. You're starving, it's night time and you hear a howl.")
            printSlow("You're terrified, you feel like you have only gotten further from civilization. There aren't even houses here.")
            printSlow("You begin looking around to try to find shelter when a bear comes charging at you before you even realize what's happening")
            printSlow("GAME OVER: You're mauled to death.")
            quit()
            
        # if you choose answer 2 and have knowledge    
        elif choice in answer2 and decision1 == 2:
            printSlow("You walk down the road towards Pittsburgh. After a few hours, you see tall buildings in the distance!")
            inPittsburgh = True
            
        # Variable completely pointless, but I wanted to show I knew booleans    
        if inPittsburgh == True:
            printSlow("You look around to see a bustling, hilly metropolis. 'Still no flying cars?' you think. How disappointing.")
            printSlow("You start walking down the street until you see a gas station, oddly it doesn't have any gas pumps.")
            printSlow("You walk into the gas station and realize nobody works there.")
            printSlow("MR ROBOT-O: Hello, welcome to AMAZON CHARGING STATION #4057. How may I help you UNIDENTIFIED HUMAN?")
            printSlow("You're startled. The voice is seemingly coming from a speaker.")
            printSlow("YOU: HELLO?! Is somebody there?")
            printSlow("MR ROBOT-O: Yes, I am Amazon's Mr Robot-O 8900. What can I help you with today?")
            printSlow("You're confused. Is this a robot? It sounds extraordinarily human.")
            printSlow("YOU: Hi, yes, umm...do you know how to get to the nearest science laboratory?")
            printSlow("MR ROBOT-O: There are 4 laboratories in Pittsburgh, what is your purpose for visiting?")
            printSlow("YOU: Uhh...I somehow got here and I'm from 1988. I think I time traveled and need to get back to my time.")
            printSlow("MR ROBOT-O: Excellent. The Department of Teleportation and Time-Traveling is located on the 9th block of Jeff Bezos Avenue.")
            printSlow("MR ROBOT-O: Fun fact: Our eternal Overlord Jeff Bezos and his Vice Overlord Elon Musk renamed 9th avenue in 2051.")
            printSlow("MR ROBOT-O: Our gracious eternal overlords were once humble businessmen before buying the country in 2049.")
            printSlow("MR ROBOT-O: Would you like to pay to be teleported directly there for only 5,000 Bezos Bucks?")
            printSlow("YOU: Uhh..no, I have no idea what those are. How do I WALK there?")
            printSlow("MR ROBOT-O: Exit the building and take a right. Follow that road until you reach the intersection of")
            printSlow("MR ROBOT-O: Jeff Bezos Avenue and Benedict Cumberbatch Lane. Take a left onto Jeff Bezos Avenue and the laboratory will be on the left.")
            printSlow("YOU: Thank you!")
            printSlow("You begin walking down Benedict Cumberbatch Lane, thinking about how creepy that robot was. Who the heck is Jeff Bezos?")
            printSlow("After about 20 minutes of walking, you see the laboratory. You walk inside.")
            printSlow("Upon entering the building the secretary jumps out of her chair upon seeing you.")
            printSlow("SECRETARY: Oh my goodness! You're going to have to come with me, we were worried sick, you were supposed to arrive HERE!")
            printSlow("YOU: You know me? How?")
            printSlow("SECRETARY: Just follow me, Dr Lichtenstein will explain everything.")
            printSlow("You follow the secretary into a sterile looking laboratory with massive machines. She calls for the Dr.")
            printSlow("DOCTOR: I can't believe you made it! We thought we had failed!")
            printSlow("YOU: Uh...can you send me back to 1988 please. What the heck.")
            printSlow("DOCTOR: Absolutely, but first, where did you end up?")
            printSlow("YOU: Uh...some farm.")
            printSlow("DOCTOR: Odd..I must not have calculated the location exactly according to the earths rotation.")
            printSlow("DOCTOR: Well, let's get you back then. Thanks for participating.")
            printSlow("YOU: It wasn't by choice!")
            printSlow("DOCTOR: It was for the good of humanity. Off you go!")
            printSlow("""You awake back where you were, back at the VCR store. You look at the clock, it's the same time as when you left.""")
            printSlow("THE END, YOU WIN!")
            quit()
            
game()
