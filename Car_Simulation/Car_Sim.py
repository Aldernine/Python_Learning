choice = ''

while choice != 'QUIT':
    choice = input('')
    if choice.upper() == 'START':
        print("Car started. Ready to go!")
    elif choice.upper() == 'STOP':
        print('Car stopped')
    elif choice.upper() == 'QUIT':
        break
    elif choice.upper() == 'HELP':
        print("Start - Start car."
              "Stop - Stop Car"
              "Quit - Quit")
    else:
        print("I don't understand")
