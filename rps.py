from random import randint
permanent = ('Rock', 'Paper', 'seissor')
computer = permanent[randint(0, 2)]

player = False

while player == False:
    player = input('Rock, Paper,seissor  : ')
    if player == computer:
        print('tie...computer choose',computer)
    elif player == 'Rock':
        if computer == 'paper':
            print('you lose (: computer choose',computer,)
        else:
            print('you win ): computer choose', computer)
    elif player == 'Paper':
        if computer == 'sessior':
            print('you lose ): computer choose', player, computer)
        else:
            print('win (: computer choose', computer, 'computer choose this')
    elif player == 'sessior':
        if computer == 'Rock':
            print('you lose (:', player, computer)
        else:
            print('you win ):', computer, 'computer choose this')

    else:
        print('enter the valid input *|*')


    player = False
    computer = permanent[randint(0,2)]

