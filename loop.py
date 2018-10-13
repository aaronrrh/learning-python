haveKey=False
doorLocked=True
doorClosed=True
gameOver=False
describeRoom=True
lightOn=False

print('You are in a room. ',end='')
while not gameOver:
    if describeRoom:
        if lightOn:
            print('There is a door that is ',end='')
            if doorClosed and doorLocked:
                print('closed and locked. ',end='')
            elif doorClosed and not doorLocked:
                print('closed and unlocked. ',end='')
            elif not doorClosed and not doorLocked:
                print('open. ',end='')
            if not haveKey:
                print('There is a key on the floor.')
            else:
                print()
        else:
            print('The room is dark and you see nothing. Maybe there\'s a switch?')
        describeRoom=False
        
    userInput=input('\nWhat do you do? ')
    cmd=userInput.lower()
    if (cmd=='get key' or cmd=='pick up key') and lightOn:
        if haveKey:
            print('You already have the key')
        else:
            haveKey=True
            print('You picked up the key')
    elif (cmd=='open door' or cmd=='open the door') and lightOn:
        if doorLocked:
            print('The door is locked. It won\'t budge.')
        elif not doorClosed:
            print('The door is already open.')
        else:
            print('The door opens!')
            doorClosed=False
    elif cmd=='turn on light' or cmd=='turn on the light' or cmd=='turn on lights' or cmd=='turn on the lights' or (not lightOn and cmd=='flip switch'):
        if not lightOn:
            lightOn=True
            print('You turn on the light.')
            describeRoom=True
        else:
            print('The light is already on.')
    elif cmd=='turn off light' or cmd=='turn off the light' or cmd.lower=='turn off lights' or cmd=='turn off the lights' or (lightOn and cmd=='flip switch'):
        if lightOn:
            lightOn=False
            print('You turn off the light.')
        else:
            print('The light is already off.')
    elif (cmd=='unlock door' or cmd=='use key') and lightOn:
        if not doorLocked:
            print('The door is already unlocked.')
        elif haveKey:
            doorLocked=False
            print('You unlocked the door.')
        else:
            print('You do not have the key.')
    elif (cmd=='leave room' or cmd=='exit') and lightOn:
        if doorClosed:
            print('The door is closed. You cannot leave.')
        else:
            gameOver=True
            print('You leave the room. YOU WIN!')
    elif cmd=='look':
        describeRoom=True
    else:
        if lightOn:
            print('I don\'t understand.')
        else:
            print('It\'s too dark! You can\'t see anything!')
print('Thanks for playing!')
