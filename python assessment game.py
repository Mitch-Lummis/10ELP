import time
import random
# Setting while loops to false
dragonRealm = False
secretNumber = False
treasureHunt = False
nextgame = False
play = False
# Defining colours to make the code more interactive
colourGreen =  '\033[32m'
colourWhite = '\033[37m'
colourYellow = '\033[33m'
colourRed = '\033[31m'
colourBlue = '\033[34m'
# Setting counters to 0
guesses = 0
timesTreasureWon = 0
timesTreasureWon = int(timesTreasureWon)
gamesPlayed = 0
gamesPlayed = int(gamesPlayed)
#the intro code to my game, explainging how it works
name = input(colourWhite + 'Hey there! Whats your name? ')
time.sleep(1)
#This allows the player to enter their name
print('Welcome to my electronics and programming game ' + name)
time.sleep(3)
print('There are three different games you can play')
time.sleep(3)
print('For every game you win, you find some treasure')
time.sleep(3)
print('Try and win the treasure as many times as you can ' + name)
time.sleep(3)
print('For your first game, would you like to...''')
time.sleep(3)
print(colourYellow + '''a: play dragon realm
b: guess my number
c: complete a treasure hunt ''' + colourWhite)
time.sleep(3)
whichGame = input('Which letter: ')
play = True
if whichGame == 'a':
    dragonRealm = True
elif whichGame == 'b':
    secretNumber = True
elif whichGame == 'c':
    treasureHunt = True
else:
    print('That was not an option')

#This play while loop allows games to be played again
while play == True:

    while nextgame == True:
        #This is the code where you choose your next game or choose to stop playing
        time.sleep(3)
        timesTreasureWon = str(timesTreasureWon)
        gamesPlayed = str(gamesPlayed)
        print('''

Great job ''' + name + '! You have got the treasure ' + timesTreasureWon + ' times!')
        timesTreasureWon = int(timesTreasureWon)
        gamesPlayed = int(gamesPlayed)
        time.sleep(3)
        print('''For your next game would you like to''')
        print(colourYellow + '''a: play dragon realm
b: guess my number
c: complete a treasure hunt''' + colourWhite)
        time.sleep(3)
        print('press anything else to stop playing')           
        time.sleep(3)
        nextgamedr = input('Which letter: ')
        nextgame = False
        if nextgamedr == 'b':
            secretNumber = True
            nextgame = False
        elif nextgamedr == 'c':
            treasureHunt = True
            nextgame = False
        elif nextgamedr == 'a':
            dragonRealm = True
            nextgame = False
        else:
            play = False
            dragonRealm = False
            secretNumber = False
            treasureHunt = False
            nextgame = False

    #the code for the Dragon Realm game
    while dragonRealm == True:
        nextgame = False
        print('Welcome to Dragon Realm ' + name)
        time.sleep(3)
        continueGame = True
        print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.''')
        continueGame = True
        while continueGame == True:
            letter = random.choice('ab')
            print('Which cave will you go into?')
            time.sleep(2)
            choice = input(colourYellow + '1 or 2: ' + colourWhite)
            print('You approach the cave and the dragon...')
            time.sleep(3)
            if choice == '1':
                if letter == 'a':
                    print(colourRed + 'Gobbles you down in one bite!')
                    time.sleep(2)
                    print('Dam ' + name + ', you really suck :(' + colourWhite)
                    gamesPlayed = int(gamesPlayed +1)
                    dragonRealm = False
                    continueGame = False
                    nextgame = True
                    break
                elif letter == 'b':
                    print(colourGreen + 'Gives you all his treasure!' + colourWhite)
                    timesTreasureWon = int(timesTreasureWon +1)
                    gamesPlayed = int(gamesPlayed +1)
                    dragonRealm = False
                    nextgame = True
                    break
                    #game won
            elif choice == '2':
                if letter == 'b':
                    print(colourRed + 'Gobbles you down in one bite!')
                    time.sleep(2)
                    print('Dam ' + name + ', you really suck :(' + colourWhite)
                    gamesPlayed = int(gamesPlayed +1)
                    dragonRealm = False
                    continueGame = False
                    nextgame = True
                    break
                elif letter == 'a':
                    print(colourGreen + 'Gives you all his treasure!' + colourWhite)
                    timesTreasureWon = int(timesTreasureWon +1)
                    gamesPlayed = int(gamesPlayed +1)
                    dragonRealm = False
                    nextgame = True
                    break
                    #game won
            else:
                print('That was not an option')
                dragonRealm = False


    #the code for the Guess my Number game
    while secretNumber == True:
        nextgame = False
        guesses = int(guesses)
        if guesses == 3:
            break
        print('Welcome to guess my number ' + name)
        guesses = 0
        time.sleep(3)
        guesses= 0 
        print('Well ' + name + ' I am thinking of a number between one and ten')
        time.sleep(3)
        print('You have three guesses.')
        number = random.randint(1,10)
        time.sleep(2)
        while guesses < 3:
            if guesses == 3:
                break
            x = int(input(colourYellow + 'Take a guess: ' + colourWhite))
            if x == number:
                gamesPlayed = int(gamesPlayed +1)
                timesTreasureWon = int(timesTreasureWon +1)
                secretNumber = False
                nextgame = True
                break
                #game won
            elif x < number:
                print('Your guess was too low')
                guesses = guesses + 1
            elif x > number:
                print('Your guess was too high')
                guesses = guesses + 1
            else:
                print('That is not a number!')
                guesses = guesses + 1
        if guesses > 2.1:
            print(colourRed + 'unlucky, you ran out of guesses' + colourWhite)
            guesses = 0
            gamesPlayed = int(gamesPlayed +1)
            nextgame = True
            secretNumber = False
        elif guesses < 3:
            print(colourGreen + 'Good job ' + name + '. You guessed my number!' + colourWhite)
            guesses = 0
            nextgame = True
            secretNumber = False

    #the code for the Treasure hunt
    while treasureHunt == True:
        nextgame = False
        print('Welcome to the treasure hunt ' + name)
        time.sleep(2)
        print('''You find yourself on an island.''')
        time.sleep(3)
        print('''You look around and see a treasure map.''')
        time.sleep(3)
        print('''The map shows treasure on the other side of the island.''')
        time.sleep(5)
        print('You begin walking through a forest and run into some bandits.')
        time.sleep(4)
        print('''Would you like to:''')
        time.sleep(2)
        print(colourYellow + '''a: sneak around the bandits
b: attack them!''' + colourWhite)
        time.sleep(2)
        bandits = input('Which letter: ')
        if bandits == 'b':
            time.sleep(4)
            print(colourRed + '''You run to attack them but a hidden scout
shoots you with an arrow and you die.''' + colourWhite)
            gamesPlayed = int(gamesPlayed +1)
            treasureHunt = False
            nextgame = True
            #game over
        elif bandits == 'a':
            time.sleep(2)
            print(colourGreen + 'You slip unnoticed past the bandits. Good job' + colourWhite)
            time.sleep(3)
            print('''You continue walking and come acorss a big river.
Would you like to:''')
            time.sleep(3)
            print(colourYellow + '''a: try and swim across
b: try and steal a boat''' + colourWhite)
            time.sleep(3)
            river = input('Which letter: ')
            if river == 'a':
                time.sleep(4)
                print(colourRed + '''You get halfway when the current
becomes to strong and you drown.''' + colourWhite)
                gamesPlayed = int(gamesPlayed +1)
                treasureHunt = False
                nextgame = True
                #game over
            elif river == 'b':
                time.sleep(2)
                print(colourGreen + '''With no one at the docks, you 
successfully steal a boat and get across the river.''' + colourWhite)
                time.sleep(4)
                print('''As you close in on the treasure, you suddenly...''')
                time.sleep(6)
                print('''Fall into a pit of quicksand. Before you
realise it the quicksand is up to your shoulders.
And then...''')
                time.sleep(7)
                print('''Help arrives! A stranger appears and helps you
out of the quicksand! Would you like to tell this new friend
about your treasure hunt?''')
                time.sleep(5)
                print(colourYellow + '''a: Tell the stranger
b: Continue alone''' + colourWhite)
                time.sleep(2)
                stranger = input('Which letter: ')
                if stranger == 'a':
                    time.sleep(2)
                    print('Your friend agrees to help you.')
                    time.sleep(2)
                    print('The two of you find the treasure!')
                    time.sleep(2)
                    print('However...')
                    time.sleep(5)
                    print(colourRed + '''The stranger stabs you with a hidden knife,
steals the treasure for himself, and you die.''' + colourWhite)
                    gamesPlayed = int(gamesPlayed +1)
                    treasureHunt = False
                    nextgame = True
                    #game over
                elif stranger == 'b':
                    time.sleep(2)
                    print('You thank your rescuer and continue alone')
                    time.sleep(1)
                    print('You get to the spot on your map and begin digging...')
                    time.sleep(5)
                    print(colourGreen + 'And you find the treasure. Well done!' + colourWhite)
                    gamesPlayed = int(gamesPlayed +1)
                    timesTreasureWon = int(timesTreasureWon +1)
                    treasureHunt = False
                    nextgame = True
                    #end of treasure hunt game
                else:
                    print('That was not an option')    
            else:
                print('That was not an option')
        else:
            print('That was not an option')
        treasureHunt = False

timesTreasureWon = str(timesTreasureWon)
gamesPlayed = str(gamesPlayed)
#the code at the end of the game where you see your stats
print(colourBlue + 'Bye ' + name + '. You got the treasure ' + timesTreasureWon + ' times, from ' + gamesPlayed + ' attempts.')
time.sleep(2)
print('Thanks for playing! :) ' + colourWhite)