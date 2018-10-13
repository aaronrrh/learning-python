print('Welcome to the AsCan program! Please state your height in inches:')
height=int(input())
if height<58 or height>76:
    print('You are either too tall or too short to be an Astronaut... Sorry.')
else:
    print('How far can you swim in open sea?')
    swim=int(input())
    if swim<75:
        print('I\'m sorry.. you cannot swim far so you cannot be an Astronaut.')
    else:
        print('Congrats! I see potential! Contact your nearest AsCan office now!')
