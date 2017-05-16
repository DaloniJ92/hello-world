import random
MIN = 1
MAX = 6

def main():
    again = 'y'


    while again == 'y' or again == 'Y':
        print('Rolling the dice...')
        print('Their values are: ')
        Dice1 = (random.randint(MIN,MAX)) 
        Dice2 = (random.randint(MIN,MAX))
        print(' First dice:', Dice1)
        print(' Second dice: ', Dice2)
        Total = Dice1 + Dice2
        print('Both dice add up to: ', Total)
        
        

        again = input('Roll again?')

main()
