# Cho-Han, a game by Aman Sheikh

import random

maxBet = 5000
print('''Cho-Han by Aman Sheikh
In this traditional Japanese game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess
if the dice total to an even(Cho) or an odd (Han) number''')

while True:
    print(f'You have {maxBet} mon. How much do you bet? (or QUIT)')
    bet = input('> ')
    if bet.isdecimal():
        bet = int(bet)
        if bet > maxBet:
            print('Enter an amount lesser than', maxBet)
            continue
    else:
        bet = bet.upper()
        if bet == 'QUIT':
            break
        else:
            print('Please give an appropriate bet amount (or write QUIT)')

    print('''The dealer swirls the cup and you hear the rattle of dice.
The dealer slams the cup on the floor still covering the
dice and asks you for your bet''')
    cho = 'CHO (even)'
    han = 'HAN (odd)'
    pline = cho[:11].center(11) + ' or ' + han[:11].center(11)
    print(pline)
    choice = input('> ')
    choice = choice.upper()
    if not choice.isalpha():
        print('Please enter CHO or HAN')
    elif choice == 'CHO' or choice == 'HAN':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sum = dice1 + dice2
        print(sum)
        if sum % 2 == 0:
            if choice == 'CHO':
                print('Congrats you won!')
                maxBet += bet
            else:
                print('You lose!')
                maxBet -= bet
        else:
            if choice == 'HAN':
                print('Congrats you won!')
                maxBet += bet
            else:
                print('You lose!')
                maxBet -= bet