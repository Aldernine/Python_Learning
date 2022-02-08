choice = ''

started = False

while choice != 'QUIT':
    choice = input('')
    if choice.upper() == 'START':
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started. Ready to go!")
    elif choice.upper() == 'STOP':
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print('Car stopped')
    elif choice.upper() == 'QUIT':
        break
    elif choice.upper() == 'HELP':
        print('''Start - Start car.
Stop - Stop Car.
Quit - Quit.''')
    else:
        print("I don't understand")
