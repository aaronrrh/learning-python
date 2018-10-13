print('How much does your cargo weigh?')
weight=float(input())
if weight>30:
    print('Your cargo is too heavy.')
else:
    print('Sure, you can ship',weight,'kgs')
    if weight<=10:
        print('It will cost $'+ str(weight*215))
    elif weight<=20:
        print('It will cost $'+ str(weight*155))
    elif weight<=30:
        print('It will cost $'+ str(weight*115))
    
