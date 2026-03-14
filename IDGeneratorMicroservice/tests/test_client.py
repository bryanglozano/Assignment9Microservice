#written by coen

from src.microservice7 import IDGenerator

def main():
    print("Welcome to the microservice 7: ID Generator unit tests \n")
    print("We are going to start by feeding the function sets of matching inputs \nwith the expectation that it will produce matching IDs \n")
    # consistant id test 1
    print("Calling ID Generator with inputs 10/27/15(date), Test1(title)")
    result1 = IDGenerator("10/27/15","Test1")
    result2 = IDGenerator("10/27/15","Test1")
    print("Output 1: ", result1, "\nOutput 2: ", result2)
    if result1 == result2:
        print("Passed test")
    else:
        print("Failed test")
    print("\n")
    # consistant id test 2
    print("Calling ID Generator with inputs 3/10/26(date), Test2(title)")
    result1 = IDGenerator("3/10/26","Test2")
    result2 = IDGenerator("3/10/26","Test2")
    print("Output 1: ", result1, "\nOutput 2: ", result2)
    if result1 == result2:
        print("Passed test")
    else:
        print("Failed test")
    print("\n")
    
    print("Next we will test for replacement of spaces with underscores \n")
    #spaces to underscores test
    print("Calling ID Generator with inputs 3/11/26(date), Test 3(title)")
    result = IDGenerator("3/11/26","Test 3")
    print("Expected output: 31126test_3 \nActual output: ", result)
    if result == "31126test_3":
        print("Passed test")
    else:
        print("Failed test")
    print("\n")
    
    print("Next we will test for replacement of uppercase letters with undercase letters \n")
    # uppercase to lowercase test
    print("Calling ID Generator with inputs 3/12/26(date), TEST4(title)")
    result = IDGenerator("3/12/26","TEST4")
    print("Expected output: 31226test4 \nActual output: ", result)
    if result == "31226test4":
        print("Passed test")
    else:
        print("Failed test")
    print("\n")
    
    print("Lastly we will test for the removal of special characters \n")
    # special characters removed test
    print("Calling ID Generator with inputs 3/13/26(date), Test5!(title)")
    result = IDGenerator("3/13/26","Test5!")
    print("Expected output: 31326test5 \nActual output: ", result)
    if result == "31326test5":
        print("Passed test")
    else:
        print("Failed test")
    print("\n")
    
    print("This concludes the microservice 7: ID Generator unit tests \nthank you for testing with us")
