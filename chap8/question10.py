def decimalToBinary(value):
    if value < 0:
        return 'Not positive'
    elif value == 0:
        return (0,)
    else:
         return decimalToBinary(value//2) + (value%2,)

    print(decimalToBinary(12))
decimalToBinary()