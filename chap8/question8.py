def DecimalToBinary(BinaryValue):
    if BinaryValue >= 1:
        DecimalToBinary(BinaryValue // 2)
    print(BinaryValue % 2, end='')

if __name__ == '__main__':
    dec_val = eval(input("enter"))
    DecimalToBinary(dec_val)
