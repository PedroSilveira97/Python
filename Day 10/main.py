from another_operation import another_operation_function


first = float(input("What is the first number? "))
first_operation = "yes"
while another_operation_function(first_operation):
    operation = str(input("What operation would you like to make? ")).lower()
    if operation == "division":
        second = float(input("What is the second number? "))
        result = first / second
        print(result)
        first = result
    elif operation == "multiplication":
        second = float(input("What is the second number? "))
        result = first * second
        print(result)
        first = result
    elif operation == "sum":
        second = float(input("What is the second number? "))
        result = first + second
        print(result)
        first = result
    elif operation == "subtraction":
        second = float(input("What is the second number? "))
        result = first - second
        print(result)
        first = result
    else:
        operation = str(input("Invalid operation. Try a valid operation."))
    first_operation = str(input("Would you like to make a new operation? "))
input("Press enter to exit the app.")
