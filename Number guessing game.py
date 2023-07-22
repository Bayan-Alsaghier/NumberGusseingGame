import random
num = random.randint(0, 10)
x = 5
for _ in range(5):
    a = input(f"Enter number between 0 and 10. You have only {x} attempts: ")
    x -= 1
    if not a.isdigit():
        if _ == 4:
            print(f"You answer is wrong the correct number was {num} !! You have used all the attempts. Try again :)")
        else:
            print('Wrong input please enter a valid integer')
    if a.isdigit():
        a = int(a)
        if a < num:
            if _ == 4:
                print(f"You answer is wrong the correct number was {num} !! You have used all the attempts. Try again")
            else:
                print('Your guess is lower. Please input a higher number')
        elif a > num:
            if _ == 4:
                print(f"Your answer is wrong the correct number was {num} !! You have used all the attempts. Try again")
            else:
                print('Your guess is higher. Please input a lower number')
        else:
            print('Your guess correct, Congratulation!')
            break
