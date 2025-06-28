import random
while True:
    emoji={
    'p':'📃',
    'r':'🥊',
    's':'✂ '}
    choices=('r','p','s')

# choices.remove('r')
    user_choice=input('rock,paper or  scissor (r/p/s) :  ').lower()
    if user_choice not in choices :
        print('Invalid choice')
        continue

    computer_choice = random.choice(choices)

    print(f'your choice {emoji[user_choice]} ')
    print(f'computer choice {emoji[computer_choice]}')

    if user_choice == computer_choice:
        print("tie")
    elif (user_choice == 'r' and computer_choice =='s') or (user_choice == 's' and computer_choice =='p') or (user_choice == 'p' and computer_choice =='r'):
        print('you win')
    else:
        print("you lose")

    should_continue=input('continue ? (y/n)').lower()
    if should_continue =='n':
        break
