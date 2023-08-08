import numpy as np


number = np.random.randint(1, 101) # computer determines random number
count = 0

while True:
    count += 1 # count attempts
    predict_number = int(input('Guess the number: ')) # prediction by user
    if predict_number > number:
        print('number must be lower')
    elif predict_number < number:
        print('number must be higher')
    else:
        print('You did it')
        break # cycle exit

print(f'You guessed in {count} attempts. The number is {number}')