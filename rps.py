import random
user_input = input("Rock, paper, or scissors? ")

def rps(user_response):
    options = ['rock', 'paper', 'scissors']
    choice = random.randint(0,2)
    computer_choice = options[choice]
    user_choice = user_response.lower()
    for character in user_choice:
        if character.isdigit():
            print("Please no numbers, just type 'rock', 'paper', or 'scissors'")
            return 
    for character in user_choice:
        if not character.isalnum():
            if character != " ":
                print("Please no symbols, just type 'rock', 'paper', or 'scissors'")
                return 
    if user_choice == computer_choice:
        print('Looks like it is a draw')
        again = input('would you like to play again? ')
        answer = again.lower()
        if answer == 'yes':
            user_input = input("Rock, paper, or scissors? ")
            rps(user_input)
        else:
            print('Goodbye!')

    elif user_choice == 'rock' and computer_choice == 'paper':
        print('Ouch, thats gotta hurt, the computer chose paper! I am sure you will get them next time!')
        again = input('would you like to play again? ')
        answer = again.lower()
        if answer == 'yes':
            user_input = input("Rock, paper, or scissors? ")
            rps(user_input)
        else:
            print('Goodbye!')
            
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print('Yippie! You did it! I knew you would win, the computer chose scissors, you are the supreme leader!')
        again = input('would you like to play again? ')
        answer = again.lower()
        if answer == 'yes':
            user_input = input("Rock, paper, or scissors? ")
            rps(user_input)
        else:
            print('Goodbye!')
            
    elif user_choice == 'paper' and computer_choice == 'scissors':
        print('Ouch, thats gotta hurt, the computer chose scissors! I am sure you will get them next time!')
        again = input('would you like to play again? ')
        answer = again.lower()
        if answer == 'yes':
            user_input = input("Rock, paper, or scissors? ")
            rps(user_input)
        else:
            print('Goodbye!')
            
    elif user_choice == 'paper' and computer_choice == 'rock':
        print('Yippie! You did it! I knew you would win, the computer chose rock, you are the supreme leader!')
        again = input('would you like to play again? ')
        answer = again.lower()
        if answer == 'yes':
            user_input = input("Rock, paper, or scissors? ")
            rps(user_input)
        else:
            print('Goodbye!')
            
    elif user_choice == 'scissors' and computer_choice == 'rock':
        print('Ouch, thats gotta hurt, the computer chose rock! I am sure you will get them next time!')
        again = input('would you like to play again? ')
        answer = again.lower()
        if answer == 'yes':
            user_input = input("Rock, paper, or scissors? ")
            rps(user_input)
        else:
            print('Goodbye!')
            
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print('Yippie! You did it! I knew you would win, the computer chose rock, you are the supreme leader!')
        again = input('would you like to play again? ')
        answer = again.lower()
        if answer == 'yes':
            user_input = input("Rock, paper, or scissors? ")
            rps(user_input)
        else:
            print('Goodbye!')

rps(user_input)

    
