def another_operation_function(another_operation):
    if another_operation.lower() == ("yes"):
        another_operation = True
    elif another_operation.lower() == ("no"):
        another_operation = False
    else:
        another_operation = str(input("Invalid answer. Would you like to make another operation."))
    return another_operation
