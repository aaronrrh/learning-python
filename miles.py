keepAsking=True
while keepAsking:
    distance=int(input('How many miles do you live from GRS?'))
    if distance==3:
        print('You live exactly 3 miles away from GRS')
    if distance <3:
        print('You live less than 3 miles away from GRS')
    if distance>3:
        print('You live more than 3 miles away from GRS')
    answer=input('Keep playing?')
    if answer.lower()=='n' or answer.lower()=='no':
        keepAsking=False
