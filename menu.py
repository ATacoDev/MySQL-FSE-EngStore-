import csv
import re
import options

endProgram = 0
def promptMenu():
    selection = input("Which would you like to do? (Please enter a number 1 - 7)\n"
                      "1) List all products that are out of stock\n"
                      "2) Find the total number of orders placed by each customer\n"
                      "3) Display the details of the most expensive product ordered in each order\n"
                      "4) Retrieve a list of products that have never been ordered\n"
                      "5) Show the total revenue generated by each supplier\n"
                      "6) Add a new order\n"
                      "7) Quit\n")
    try:
        selection = int(selection)
        if selection < 1 or selection > 7:
           print("Error: Please enter a valid option")
           promptMenu()
        elif selection == 1:
            options.optionOne()
        elif selection == 2:
            options.optionTwo()
        elif selection == 3:
            options.optionThree()
        elif selection == 4:
            options.optionFour()
        elif selection == 5:
            options.optionFive()
        elif selection == 6:
            options.optionSix()
        else:
            print("Closing down.")
            global endProgram
            endProgram = 1
    except:
        print(f"Error: Please enter an integer value.")

