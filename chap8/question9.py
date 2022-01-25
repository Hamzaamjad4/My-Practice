def binaryToHex(binaryValue):
    number = int(binaryValue, 2)
    return format(number, 'X')
def main():
    binaryValue = input('Enter a binary number: ')
    print('The hex value is', binaryToHex(binaryValue))
main()