print('Welcome to allcalc v1.1! What\'s your name?')
nam=input()
print('Please input a number,',nam)
num=float(input())
print('Please input a second number!')
numnum=float(input())
print('What operation?')
opr=input()
if opr=='addition':
  print('the answer is',num+numnum)
if opr=='subtraction':
  print('The answer is',num-numnum)
if opr=='multiplication':
  print('The answer is',num*numnum)
if opr=='division':
  print('The answer is',num/numnum)
if opr=='easteregg':
  print('Created by Aaron Ropers-Huilman')
else:
  print('Thanks for using this program,',nam)
  eag=input()
  if eag=='Vega':
    print('Well, it looks as if you have found the main easter egg. This particular egg doesen\'t really have anything malicious in it, so you have nothing to fear. Or do you? It\'s your call. Proceed?')
    ans=input()
    if ans=='yes':
      print('Well... you have chosen to preceed. I. Am. Coming.')
      d=True
      if d==True:
        print('ERROR')
        print('ERR0R')
        print('3RR0R')
        print('3RR0R/')
        print('3RR09/')
        print('3RR09/#')
        print('34509/#')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
        print('34509/#!o')
    if ans=='no':
      print('Alright... you will never know the secret...')
  if eag=='command':
    print('You have been granted admin settings.')
    thanks=input()
    if thanks=='thanks':
      print('You\'re welcome,',nam)
