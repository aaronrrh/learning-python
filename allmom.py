print('How many calories did you eat today?')
cal=int(input())
print('How many calories did you expend today?')
calexp=int(input())
if cal>calexp:
    print('You gained this many calories:', cal-calexp)
    print('That means you gained this many pounds:', (cal-calexp)/3500)
else:
    print('You have burned this many extra calories:', calexp-cal)
    print('That means you lost this many pounds:', (calexp-cal)/3500)
