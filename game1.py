import numpy as np

def random_predict(number:int=1) -> int:
    """The number will be guessed random by the computer

    Args:
        number (int, optional): your number. Defaults to 1.

    Returns:
        int: number of attemps
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # number predicted by computer
        if number == predict_number:
            break # exit while
    
    return count


def score_game(random_predict) -> int:
    """Mean number of attempts of guess number algorithm in 1000 tries
    Args:
        random_predict (_type_): guess number fi=unction

    Returns:
        int: mean number of attempts
    """
    np.random.seed(1) # fix random seed
    random_array = np.random.randint(1, 101, size=1000) # array numbers for guess
    count_ls = [] # list of numbers of attempts
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = np.mean(count_ls)
    
    print(f'Average number of attempts to guess the number by this algorithm is {score}')
    return score

if __name__ == '__main__':
    # run
    score_game(random_predict)
    