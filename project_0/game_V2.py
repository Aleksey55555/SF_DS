import numpy as np


def alg_predict(number:int=1) -> int:
    """The number will be guessed by algorithm

    Args:
        number (int, optional): your number. Defaults to 1.

    Returns:
        int: number of attemps to guess
    """
    count = 0
    predict_number = 50 # determine first prediction
    pre_predict_number = 0 # need for increment and decrement of prediction
    
    while True:
 
        count += 1
        temp = predict_number
        difference = abs(predict_number - pre_predict_number) / 2 # increment/decrement of prediction
        if difference < 1: # round to 1 if increment = 0.5 to pevent loop (prediction = preprediction)
            difference = 1
        
        if number == predict_number:
            break # cycle exit
        elif number > predict_number:
            predict_number += difference # increment of prediction
            predict_number = int(predict_number)
            pre_predict_number = temp
        else:
            predict_number -= difference # decrement of prediction
            predict_number = int(predict_number)
            pre_predict_number = temp
    
    return count


def score_game(predict) -> int:
    """Mean number of attempts of guess number algorithm per 1000 attempts
    Args:
        predict (_type_): guess number function

    Returns:
        int: mean number of attempts
    """
    np.random.seed(1) # fix random seed
    random_array = np.random.randint(0, 101, size=1000) # array numbers for guess
    count_ls = [] # list of numbers of attempts
    
    for number in random_array:
        count_ls.append(predict(number))
    
    score = np.mean(count_ls) # calculate mean number of attempts
    
    print(f'Average number of attempts to guess the number by this algorithm is {score}')
    return score


if __name__ == '__main__':
    # run
    score_game(alg_predict)
    