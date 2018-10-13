print('Please enter your GPA:')
gpa=float(input())
if gpa>3.0:
    print('Congrats! You made the Dean\'s list!')
else:
    if gpa==2.0:
        print('You common muggle...')
    else:
        if gpa<2:
            print('You need work. That\'s all. Work.')
