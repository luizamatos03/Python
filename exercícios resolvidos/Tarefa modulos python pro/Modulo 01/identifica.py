def multi5(num):
    if num % 5 == 0:
        result = 'fizz'
        return result
    else:
        return False

def multi7(num):
    if num % 7 == 0:
        result = 'buzz'
        return result
    else:
        return False

def multi5e7(num):
    if num % 5 == 0 and num % 7 == 0:
        result = 'fizzbuzz'
        return result
    else:
        return False

def nao_multi(num):
    if num % 5 != 0 or num % 7 != 0:
        result = 'miss'
        return result
    else:
        return False
