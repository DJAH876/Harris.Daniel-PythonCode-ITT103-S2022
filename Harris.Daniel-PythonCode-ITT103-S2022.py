# Author: Daniel Harris
# Date Created: April 28, 2022.
# Course:ITT103
# Purpose: This program is to calculate and print the commission received by a salesperson.

def jamex():  # Function to be executed when called.
    salesperson_id = 0  # Initializing the variable
    sales_amount = 1  # Initializing the variable
    sales_class = '1', '2', '3'  # Initializing the variable

    while True:  # Program loops indefinitely until condition is met
        try:  # Instruction to check code for errors
            salesperson_id = int(input("Please enter the salesperson unique number (For Ex . 100002) : "))  #  Prompt user to enter data once true
        except ValueError:  # When error is generated this expression is raised.
            print("Please enter numbers only. ")  # To be displayed when there is an error
            continue  # Continue unto the next instruction within the loop
        if salesperson_id < 0:  # Loop condition
            print("Incorrect number format")  # To be displayed to the user when incorrect data is entered
            continue  # Continue unto the next instruction within the loop
        else:
            break  # Terminate the loop

    print("Salesperson ID is:", salesperson_id)  # To be displayed to the user

    while True:  # Program loops indefinitely until condition is met
        try:  # Instruction to check code for errors
            sales_amount = float(input("Please enter salesperson total sales: $"))  # Prompt user to enter data once true
        except ValueError:  # When error is generated this expression is raised.
            print("Please enter numbers only. ")  # To be displayed when there is an error
            continue  # Continue unto the next instruction within the loop
        if sales_amount < 0:  # Loop condition
            print("Sales amount can not be less than zero")  # To be executed when false
            continue  # Continue unto the next instruction within the loop
        else:
            break  # Terminate the loop

    print("Salesperson total sales: $", sales_amount)  # To be displayed to the user

    while True:  # Program loops indefinitely until condition is met
        try:  # Instruction to check code for errors
            sales_class = int(input("Please enter either '1' for Class1, '2' for Class2, or '3' for Class3: "))  #  Prompt user to enter data once true
        except ValueError:  # When error is generated this expression is raised.
            print("Error!"" ""Incorrect sales class entered! ")  # To be displayed when there is an error
            continue  # Continue unto the next instruction within the loop
        if sales_class <= 0 or sales_class > 3:  # Loop condition
            print("Error!"" ""Incorrect sales class entered! ")  # To be displayed when incorrect data is entered
            continue  # Continue unto the next instruction within the loop
        else:
            break  # Terminate the loop

    print("Salesperson class is: ", sales_class)  # To be displayed to the user

    if sales_class == 1 and sales_amount <= 1000:  # If condition to be tested
        comm_rt: float = 0.06  # Initializing the variable and storing data in it
        comm: float = round(sales_amount * comm_rt, 2)  # Calculation of sales commission rounded up to two decimal place
        print("Sales commission is: $", comm)  # To be displayed to the user
        
#  Conditions to be tested until true #
    elif sales_class == 1 and 1000 < sales_amount < 2000:
        comm_rt: float = 0.07  # Initializing the variable and storing data in it
        comm: float = round(sales_amount * comm_rt, 2)  # Calculation of sales commission rounded up to two decimal place
        print("Sales commission is: $", comm)  # To be displayed to the user

    elif sales_class == 1 and sales_amount >= 2000:
        comm_rt: float = 0.1  # Initializing the variable and storing data in it
        comm: float = round(sales_amount * comm_rt, 2)  # Calculation of sales commission rounded up to two decimal place
        print("Sales commission is: $", comm)  # To be displayed to the user

    elif sales_class == 2 and sales_amount < 1000:
        comm_rt: float = 0.04  # Initializing the variable and storing data in it
        comm: float = round(sales_amount * comm_rt, 2)  # Calculation of sales commission rounded up to two decimal place
        print("Sales commission is: $", comm)  # To be displayed to the user

    elif sales_class == 2 and sales_amount >= 1000:
        comm_rt: float = 0.06  # Initializing the variable and storing data in it
        comm: float = round(sales_amount * comm_rt, 2)  # Calculation of sales commission rounded up to two decimal place
        print("Sales commission is: $", comm)  # To be displayed to the user

    elif sales_class == 3:
        comm_rt: float = 0.45  # Initializing the variable and storing data in it
        comm: float = round(sales_amount * comm_rt, 2)  # Calculation of sales commission rounded up to two decimal place
        print("Sales commission is: $", comm)  # To be displayed to the user

    #  Prompt user to enter data to continue or exit the program
    cont = input("To calculate another salesperson commission? Enter 'Y' continue or 'N' to exit ").upper()
    while cont not in ('N', 'Y'):  # Loop condition
        # To be displayed to the user
        print("Incorrect input, enter either 'Y' to continue or 'N' to exit")
        #  Prompt user to enter data to continue or exit the program
        cont = input("To calculate another salesperson commission? Enter 'Y' continue or 'N' to exit ").upper()

    if cont == "N":  # Predefined condition to terminate the program
        exit("Thank you, goodbye")  # Code to exit program and message to be displayed to the user
    else:
        jamex()  # Function is called to loop to the beginning of the program


jamex()  # Program is terminated
