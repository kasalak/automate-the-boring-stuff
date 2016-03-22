IsThereRain = []
while IsThereRain != 'no': #creates loop as long as answer is not 'no'
    print('Is it raining?')
    IsThereRain = input()
    if IsThereRain == 'yes':
        print('Do you have an umbrella?')
        Umbrella = input()
        if Umbrella == 'yes':
            print('Lucky you. Go outside.')
            break
        else:
            print('Wait a while.')
    else:
                print('Then what are you doing inside? Go play!')
