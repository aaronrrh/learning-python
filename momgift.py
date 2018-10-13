print('Happy birthday, Mom!')
print('How old are you turning?')
age=int(input ())
print('Oh! So you\'re turning',age)
print('Well, happy birthday!')
print(age)
if age > 49:
    print('Also, I think you\'re lying. Too young.')
if age<47:
    print('Also, I think you\'re lying. Too old.')
else:
    print('So, how are you feeling about turning', age)
    feels=input()
    if feels=='good' or feels=='great':
        print('That\'s good! I hope that this birthday is awesome!')
    if feels=='bad' or feels=='meh':
        print('Well, I\'m sure that things will be fine...')
    if feels=='mediocre':
        print('Well, meh.')
    if feels=='easteregg':
        print('So, this code was made by aaron. hi, mom! boyoboyo...')

    else:
        print('Anyway, happy, happy birthday!!!')
        print('Did you like this code? yes or no?')
        yn=input()
        if yn=='yes':
            print('Thanks, Mom! I love you very much!')
        if yn=='no':
            print('Aw... I didn\'t want to dissapoint you... and I did..')
        print('Well, thanks for giving this a try!')



