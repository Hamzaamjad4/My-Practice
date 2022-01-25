n = input("Enter 16-digit Credit Card Number:")

def validate_credit_card():
    if len(n) == 16:
        print("Valid Credit Card")
    else:
        print("Credit Card number limit Exceeded!!!!")
        exit()


if __name__ == "__main__":
    validate_credit_card()