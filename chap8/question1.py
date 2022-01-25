def checkSSN():
 ssn = ""
 while not ssn:
    ssn = str(input("Enter a Social Security Number in the format ddd-dd-dddd: "))
    ssn = ssn.replace("-", "")
    if len(ssn) != 9:
        print("Invalid SSN")
    else:
        print("Valid SSN")

checkSSN()