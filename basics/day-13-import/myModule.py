import random
def pass_generator():
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = lower.upper()
    digit = '0123456789'
    symbol = '{[(!@#$%^&*+=-/?<>,.:;")]}'

    allchar = lower + upper + digit + symbol

    acak = "".join(random.sample(allchar, k=12))

    return acak

if __name__ == '__main__':
    pass

    