# ABIGAIL WEE TYNN
# TP075628

# Importing relevant packages

# Import PrettyTable for generating and displaying tabular outputs in the console
from prettytable import PrettyTable 

# Import json for storing and saving data into JSON files, enabling data persistence
import json

# Import os for interacting with the operating system, such as checking file existence and paths
import os


# Declaring an empty dictionary called employees to store all employee data
employees = {}

# Declaring an empty dictionary called payslips to store all employee salary data
payslips = {}


# Define a procedure called loadData to load data from JSON files into the employees and payslips dictionaries
def loadData():
    # Accessing the global variables to modify them within the function
    global employees, payslips
    
    # Check if the employees data file exists in the current directory
    if os.path.exists('employees.json'):
        # Open the employees.json file in read mode
        with open('employees.json') as f:
            # Load data from the JSON file into the employees dictionary
            employees = json.load(f)
    
    # Check if the payslips data file exists in the current directory
    if os.path.exists('payslips.json'):
        # Open the payslips.json file in read mode
        with open('payslips.json') as f:
            # Load data from the JSON file into the payslips dictionary
            payslips = json.load(f)


# Define a procedure called saveData to save all current data in employees and payslips to JSON files
def saveData():
    # Accessing the global variables to save their updated states
    global employees, payslips
    
    # Open the employees JSON file in write mode
    with open('employees.json', 'w') as f:
        # Write the current state of the employees dictionary to the JSON file
        json.dump(employees, f)
    
    # Open the payslips JSON file in write mode
    with open('payslips.json', 'w') as f:
        # Write the current state of the payslips dictionary to the JSON file
        json.dump(payslips, f)


# Define a function called promptIntegerInput to get user input and ensure it is a non-negative integer
def promptIntegerInput(action):
    # Creating an infinite loop to continue prompting until the user enters valid input
    while True:
        try:
            # Attempt to convert user input into an integer
            number = int(input(action))
            
            # Check if the entered integer is non-negative
            if number < 0:
                print("Invalid input. Please ensure that input is a non-negative number.")
                continue  # Return to the beginning of the loop
            
            # Return the input number if it is valid
            return number 
        
        # If input cannot be converted to an integer, handle the error and prompt again
        except ValueError:
            print("Invalid input. Please reenter a valid number.")


# Define a function called promptFloatInput to get input, ensure that the input is a float, and validate it as non-negative
def promptFloatInput(action):
    # Creating an infinite loop to continue prompting until the user enters valid input
    while True:
        try:
            # Attempt to convert the user input into a float
            number = float(input(action))
            
            # Check if the entered float is non-negative
            if number < 0:
                print("Invalid input. Please ensure that input is a non-negative number")
                continue  # Return to the beginning of the loop
            
            # Return the input number if it is valid
            return number 
        
        # If input cannot be converted to a float, handle the error and prompt again
        except ValueError:
            print("Invalid input. Please reenter a valid number.")


# Define a function called promptStringsInput to get input and ensure that the input contains only letters and spaces
def promptStringsInput(action):
    # Creating an infinite loop to continue prompting until the user enters valid input
    while True:
        # Get the user input
        string = input(action)
        
        # Check if the input contains only alphabetic characters and spaces
        if not all(s.isalpha() or s.isspace() for s in string):
            print("Invalid input. The string must contain only letters and spaces.")
            continue  # Return to the beginning of the loop if invalid
        
        # If the input passes the check, return it
        return string


# Define a function called promptEmpIDInput to prompt and validate Employee ID input in a specific format
def promptEmpIDInput(prompt_text="Enter Employee ID (e.g., 'TP00001'): "):
    # Creating an infinite loop until the user enters a valid Employee ID
    while True:
        # Prompt for Employee ID input, remove any extra spaces, and convert it to uppercase for consistency
        empID = input(prompt_text).strip().upper()
        
        # Check if the Employee ID starts with 'TP', is exactly 7 characters, and the last 5 characters are digits
        if empID.startswith("TP") and len(empID) == 7 and empID[2:].isdigit():
            # If the Employee ID is valid, return it
            return empID
        else:
            # Print a warning if the format is incorrect
            print("Invalid Employee ID format. Please enter an ID in the format 'TP00001', 'TP00002', etc.")


# Define a procedure to update existing employee payslip details
def updateEmployee(empID=None, year=None, month=None):
    global employees, payslips

    # Prompt for Employee ID if not provided, using standardized input
    if not empID:
        empID = promptEmpIDInput("Enter Employee ID to update: ")
    
    # Prompt for month if not provided, ensuring it matches valid month names
    if not month:
        month = promptStringsInput("Enter Month (e.g., 'January', 'February'): ").capitalize()
        valid_months = ['January', 'February', 'March', 'April', 'May', 'June', 
                        'July', 'August', 'September', 'October', 'November', 'December']
        while month not in valid_months:
            print("Invalid month. Please enter a valid month name.")
            month = promptStringsInput("Enter Month (e.g., 'January', 'February'): ").capitalize()

    # Prompt for year if not provided, ensuring it is a valid 4-digit integer
    if not year:
        year_input = input("Enter Year (e.g., 2023): ")
        while not year_input.isdigit() or len(year_input) != 4:
            print("Invalid year. Please enter a 4-digit year.")
            year_input = input("Enter Year (e.g., 2023): ")
        year = int(year_input)

    # Check if the payslip record exists for the specified Employee ID, month, and year
    if empID not in payslips or year not in payslips[empID] or month not in payslips[empID][year]:
        print(f"No payslip record found for {month} {year}. Please add the payslip first before updating.")
        return  # Exit if no record is found

    # Display existing payslip data for reference
    print("\nExisting Payslip Data for Reference:")
    existing_table = PrettyTable()
    existing_table.field_names = ["Detail", "Value"]
    existing_data = payslips[empID][year][month]
    for key, value in existing_data.items():
        existing_table.add_row([key, f"{value:.2f}"])
    print(existing_table)

    # Prompt user to update salary components
    basicSalary = promptFloatInput("Enter updated Basic Salary Amount: ")
    allowance = promptFloatInput("Enter updated Allowance Amount: ")
    bonus = promptFloatInput("Enter updated Bonus Amount: ")
    overtime = promptFloatInput("Enter updated Overtime Amount: ")

    # Calculate net salary and other components based on input values
    salaryDetails = calculateNetSalary(basicSalary, allowance, bonus, overtime)

    # Display the updated details using PrettyTable for user confirmation
    table = PrettyTable()
    table.field_names = ["Detail", "Value"]
    table.add_row(["Employee ID", empID])
    table.add_row(["Employee Name", employees[empID]['Employee Name']])
    table.add_row(["Department Name", employees[empID]['Department Name']])
    table.add_row(["Year", year])
    table.add_row(["Month", month])
    for key, value in salaryDetails.items():
        table.add_row([key, f"{value:.2f}"])

    print("\nUpdated Employee and Salary Details:\n")
    print(table)

    # Confirm if the user wants to save the updated payslip details
    confirmation = input("\nDo you want to overwrite the existing payslip with these updated details? (yes/no): ").strip().lower()
    if confirmation != 'yes':
        print("Employee update was canceled. No changes were saved.")
        return  # Exit without saving changes if the user chooses 'no'

    # Update the payslip record with new values in `payslips` dictionary
    payslips[empID][year][month] = salaryDetails

    # Persist updated information to JSON files
    saveData()

    print("Employee data has been successfully updated.")


# Define a procedure to add a new employee or add a new payslip for an existing employee
def addEmployee():
    global employees, payslips

    # Use a standardized input function to prompt for Employee ID
    empID = promptEmpIDInput("Enter Employee ID: ")
    
    # Check if Employee ID already exists in the `employees` dictionary
    if empID in employees:
        print("This Employee ID already exists. Adding a new payslip record for this employee.")
        # Retrieve existing employee name and department for display and use in the payslip
        employeeName = employees[empID]['Employee Name']
        departmentName = employees[empID]['Department Name']
    else:
        # Collect new employee information if the employee does not exist
        print("This Employee ID does not exist yet. Adding it to the system.")
        employeeName = promptStringsInput("Enter Employee Name: ")
        departmentName = promptStringsInput("Enter Department Name: ")
        
    # Prompt for month and year to associate the payslip record with a specific period
    month = promptStringsInput("Enter Month (e.g., 'January', 'February'): ").capitalize()
    valid_months = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
    # Ensure the month is valid
    while month not in valid_months:
        print("Invalid month. Please enter a valid month name.")
        month = promptStringsInput("Enter Month (e.g., 'January', 'February'): ").capitalize()

    # Prompt for and validate the year
    year = input("Enter Year (e.g., 2023): ")
    while not year.isdigit() or len(year) != 4:
        print("Invalid year. Please enter a 4-digit year.")
    year = int(year)

    # Initialize the structure in `payslips` if this is a new employee or year
    if empID not in payslips:
        payslips[empID] = {}
    if year not in payslips[empID]:
        payslips[empID][year] = {}
    
    # Check if a payslip already exists for the specified month and year
    if month in payslips[empID][year]:
        print(f"A payslip record for {month} {year} already exists.")
        # Prompt the user to update the existing record if desired
        update_choice = input("Would you like to update the existing record instead? (yes/no): ").strip().lower()
        if update_choice == 'yes':
            updateEmployee(empID, year, month)  # Call `updateEmployee` with existing ID, month, and year
        else:
            print("No changes made. Returning to the main menu.")
        return

    # Prompt for salary components
    basicSalary = promptFloatInput("Enter Basic Salary Amount: ")
    allowance = promptFloatInput("Enter Allowance Amount: ")
    bonus = promptFloatInput("Enter Bonus Amount: ")
    overtime = promptFloatInput("Enter Overtime Amount: ")

    # Calculate net salary and related details using a separate function
    salaryDetails = calculateNetSalary(basicSalary, allowance, bonus, overtime)

    # Ask for confirmation to save the new record
    confirmation = input("\nDo you want to save these details? (yes/no): ").strip().lower()
    if confirmation != 'yes':
        print("Employee data and salary details were not saved.")
        return  # Exit the procedure if the user chooses not to save

    # Save employee information and salary details if the user confirms saving
    if empID not in employees:
        employees[empID] = {
            'Employee Name': employeeName,
            'Department Name': departmentName
        }

    # Save payslip information for the specified month and year
    payslips[empID][year][month] = salaryDetails

    # Save data to JSON files to ensure persistence
    saveData()

    print("Employee data has been successfully added and salary details saved.")


# Define a procedure called deleteEmployee to remove an employee's details from both employees and payslips dictionaries,
# and subsequently from the respective JSON files.
def deleteEmployee():
    # Accessing the global variables
    global employees, payslips

    # Use a standardized input function to prompt for Employee ID
    empID = promptEmpIDInput("Enter Employee ID to delete: ")

    # Check if the Employee ID exists in the employees dictionary
    if empID in employees:
        # Delete the employee's record from the employees dictionary
        del employees[empID]
        print(f"Employee data for {empID} has been successfully deleted from the employees dictionary.")
        
        # Check if the employee has any salary records in the payslips dictionary
        if empID in payslips:
            # Delete the employee's salary records from the payslips dictionary
            del payslips[empID]
            print(f"Employee salary records for {empID} have been successfully deleted from the payslips dictionary.")
        else:
            # Inform the user if no salary records are found for the employee in payslips
            print(f"No salary records found for {empID} in the payslips dictionary.")

        # Save changes to ensure the deletions are reflected in the JSON files
        saveData()
        print("All changes have been successfully saved.")
    
    else:
        # Inform the user if the Employee ID does not exist in the employees dictionary
        print("Employee ID does not exist!")


# Define a procedure called viewEmployee to display all employee records from the employees dictionary
def viewEmployee():
    # Accessing the global employees dictionary to get the data
    global employees

    # Check if there are any employee records in the dictionary
    if not employees:
        print("No employee records found.")  # Inform the user if the dictionary is empty
        return  # Exit the procedure if no records are found

    # Create a PrettyTable object for organized tabular display
    employeeTable = PrettyTable()
    # Set column headers for the table
    employeeTable.field_names = ["Employee ID", "Name", "Department"]

    # Loop through each employee record in the employees dictionary
    for empID, details in employees.items():
        # Add a row to the table for each employee with their ID, name, and department
        employeeTable.add_row([empID, details['Employee Name'], details['Department Name']])

    # Display the complete table of employee records
    print("\nEmployee Records:")
    print(employeeTable)


# Define a function to calculate the net salary, applying EPF deduction, tax, and bonus adjustments based on predefined criteria
def calculateNetSalary(basicSalary, allowance, bonus, overtime):
    # Calculate the gross salary as the sum of all components
    grossSalary = basicSalary + allowance + bonus + overtime
    
    # Calculate EPF (Employees Provident Fund) deduction at 11%
    epfDeduction = grossSalary * 0.11
    # Calculate the salary after EPF deduction
    salaryAfterEPF = grossSalary - epfDeduction

    # Initialize variables for additional adjustments
    additionalBonus = 0  # Additional bonus, if applicable
    taxDeduction = 0     # Tax deduction, if applicable

    # Apply additional adjustments based on salaryAfterEPF criteria
    if salaryAfterEPF < 2000:
        # Add 5% bonus for salary less than 2000
        additionalBonus = salaryAfterEPF * 0.05
    elif salaryAfterEPF > 3000:
        # Deduct 6% tax for salary greater than 3000
        taxDeduction = salaryAfterEPF * 0.06

    # Calculate net salary after applying additional bonus and tax deduction
    netSalary = salaryAfterEPF + additionalBonus - taxDeduction

    # Return a dictionary containing all calculated salary components
    return {
        'Basic Salary': basicSalary,
        'Allowance': allowance,
        'Bonus': bonus,
        'Overtime': overtime,
        'Gross Salary': grossSalary,
        'EPF Deduction': epfDeduction,
        'Additional Bonus': additionalBonus,
        'Tax Deduction': taxDeduction,
        'Net Salary': netSalary
    }


# Define a procedure to interactively calculate and display an employee's net salary based on inputted salary components
def generateNetSalary():
    global employees  # Accessing the global 'employees' dictionary
    
    # Prompt user to enter the employee ID
    empID = promptEmpIDInput("Enter Employee ID: ")
    
    # Check if Employee ID exists in the system
    if empID not in employees:
        print("Employee ID not found. Please check and try again.")
        return

    # Prompt for the specific month and year
    month = promptStringsInput("Enter Month (e.g., 'January', 'February'): ").capitalize()
    valid_months = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
    while month not in valid_months:
        print("Invalid month. Please enter a valid month name.")
        month = promptStringsInput("Enter Month (e.g., 'January', 'February'): ").capitalize()
    
    # Prompt for the year and ensure it is a valid 4-digit number
    year_input = input("Enter Year (e.g., 2023): ")
    while not year_input.isdigit() or len(year_input) != 4:
        print("Invalid year. Please enter a 4-digit year.")
    year = int(year_input)  # Convert validated year input to integer

    # Prompt for salary components
    basicSalary = promptFloatInput("Enter Basic Salary Amount: ")
    allowance = promptFloatInput("Enter Allowance Amount: ")
    bonus = promptFloatInput("Enter Bonus Amount: ")
    overtime = promptFloatInput("Enter Overtime Amount: ")

    # Calculate the net salary and other components using calculateNetSalary
    salaryDetails = calculateNetSalary(basicSalary, allowance, bonus, overtime)

    # Display the calculated salary details
    print("\nCalculated Salary Details:")
    for key, value in salaryDetails.items():
        print(f"{key}: {value:.2f}")  # Output each component in formatted form

    print("Net salary calculation complete (data not saved).")  # Indicate that data is not saved


# Define a procedure called searchSpecificPayslip to search for a particular employee's payslip based on month and year
def searchSpecificPayslip():
    global payslips  # Accessing the global 'payslips' dictionary

    # Loop to allow re-entry if Employee ID is not found
    while True:
        # Prompt for Employee ID
        empID = promptEmpIDInput("Enter Employee ID: ")

        # Check if Employee ID exists in the payslips dictionary
        if empID not in payslips:
            print("No records found for this Employee ID.")
            retry = input("Would you like to try again with a different Employee ID? (yes/no): ").strip().lower()
            if retry != 'yes':
                print("Returning to the main menu.")
                return  # Exit if user chooses not to retry
            else:
                continue  # Prompt for Employee ID again if user chooses to retry

        # If Employee ID exists, proceed to prompt for month and year
        month = promptStringsInput("Enter Month (e.g., 'January', 'February'): ").capitalize()
        valid_months = ['January', 'February', 'March', 'April', 'May', 'June', 
                        'July', 'August', 'September', 'October', 'November', 'December']
        
        # Validate the entered month
        while month not in valid_months:
            print("Invalid month. Please enter a valid month name (e.g., 'January').")
            month = promptStringsInput("Enter Month (e.g., 'January', 'February'): ").capitalize()

        # Prompt for the year, ensuring it's a valid 4-digit year
        year_input = input("Enter Year (e.g., 2023): ")
        while not year_input.isdigit() or len(year_input) != 4:
            print("Invalid year. Please enter a 4-digit year.")
            year_input = input("Enter Year (e.g., 2023): ")
        year = int(year_input)  # Convert validated year to integer

        # Check if payslip exists for the specified month and year
        if year not in payslips[empID] or month not in payslips[empID][year]:
            print(f"No payslip record found for {month} {year} for Employee ID {empID}.")
            return  # Exit if no record is found

        # Retrieve the payslip details
        payslip_details = payslips[empID][year][month]

        # Display the payslip details using PrettyTable
        payslip_table = PrettyTable()
        payslip_table.field_names = ["Detail", "Value"]
        
        for key, value in payslip_details.items():
            payslip_table.add_row([key, f"{value:.2f}"])

        # Print the payslip details table
        print(f"\nPayslip for Employee ID: {empID} for {month} {year}")
        print(payslip_table)
        return  # End function after displaying the payslip


# Define a procedure called viewAllPayslips to view all payslips for a specific employee in descending year order
def viewAllPayslips():
    global payslips  # Accessing the global 'payslips' dictionary

    # Prompt for Employee ID using standardized input
    empID = promptEmpIDInput("Enter Employee ID: ")

    # Check if Employee ID exists in the payslips dictionary
    if empID not in payslips:
        print("No payslip records found for this Employee ID.")
        # Allow user to retry if no records are found
        retry = input("Would you like to try again with a different Employee ID? (yes/no): ").strip().lower()
        if retry != 'yes':
            print("Returning to the main menu.")
            return  # Exit the procedure if user does not wish to retry
        else:
            return viewAllPayslips()  # Retry for a different Employee ID

    # Sort the years in descending order to display most recent payslips first
    for year in sorted(payslips[empID].keys(), reverse=True):
        months = payslips[empID][year]
        
        # Create a PrettyTable for displaying payslip details for the current year
        year_table = PrettyTable()
        year_table.field_names = ["Month", "Basic Salary", "Allowance", "Bonus", "Overtime", "Gross Salary", 
                                  "EPF Deduction", "Additional Bonus", "Tax Deduction", "Net Salary"]
        
        # Populate table with each month's details in the current year
        for month, details in months.items():
            year_table.add_row([
                month,
                f"{details.get('Basic Salary', 0.00):.2f}",
                f"{details.get('Allowance', 0.00):.2f}",
                f"{details.get('Bonus', 0.00):.2f}",
                f"{details.get('Overtime', 0.00):.2f}",
                f"{details.get('Gross Salary', 0.00):.2f}",
                f"{details.get('EPF Deduction', 0.00):.2f}",
                f"{details.get('Additional Bonus', 0.00):.2f}",
                f"{details.get('Tax Deduction', 0.00):.2f}",
                f"{details.get('Net Salary', 0.00):.2f}"
            ])

        # Display the formatted table for each year
        print(f"\nPayslip Summary for Employee ID: {empID} for Year: {year}")
        print(year_table)


# Define a procedure called exit to exit the program
def exit():
    # Call saveData to save any changes made to employees and payslips dictionaries
    saveData()
    
    # Inform the user that the program is closing
    print("Exiting the program.")
    
    # End the function, signaling the end of the program flow
    return


# Define a procedure called empProfileSubMenu to display the sub menu for Employee Profile.
def empProfileSubMenu():
    # Accessing the global variable to ensure any changes in employee data are updated
    global employees

    # Creating an infinite loop to keep displaying the sub menu until the user decides to return to the main menu
    while True:
        # Displaying the options that the user can choose from in the Employee Profile sub menu
        print("\n------ Employee Profile ------")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. View Employee List")
        print("5. Return to Main Menu")
        
        # Prompt the user to enter their option
        option = input("Enter your choice: ")
        
        # Process the user's choice using if-elif-else statements
        if option == "1":
            addEmployee()  # Calls addEmployee procedure to add a new employee
        
        elif option == "2":
            updateEmployee()  # Calls updateEmployee procedure for modifying existing employee data
        
        elif option == "3":
            deleteEmployee()  # Calls deleteEmployee procedure to remove an employee record
        
        elif option == "4":
            viewEmployee()  # Calls viewEmployee procedure to display all employee records
        
        elif option == "5":
            # Exit the loop to return to the Main Menu
            break
        
        else:
            # Prompt for a valid choice if input is other than "1", "2", "3", "4", or "5"
            print("Choice is invalid. Try entering choice again.")


# Define a procedure called payslipSubMenu to display the sub menu for Payslip options.
def payslipSubMenu():
    # Infinite loop to keep showing the Payslip sub menu until the user decides to return to the main menu
    while True:
        # Displaying the options available in the Payslip sub menu
        print("\n*** Payslip ***")
        print("1. Search Specific Payslip")  # Option to search for a specific payslip by month and year
        print("2. View All Payslips")  # Option to view all payslips for a specific employee
        print("3. Return to Main Menu")  # Option to return to the main menu

        # Prompt the user to enter their choice
        choice = input("Enter your choice: ")  

        # Processing the user's choice using if-elif-else statements
        if choice == "1":
            searchSpecificPayslip()  # Calls searchSpecificPayslip procedure to search for a particular payslip
        elif choice == "2":
            viewAllPayslips()  # Calls viewAllPayslips procedure to display all payslips for an employee
        elif choice == "3":
            break  # Exits the loop to return to the main menu
        else:
            # Prompt for a valid choice if input is other than "1", "2", or "3"
            print("Invalid choice. Please try again.")


# Define a procedure called mainMenu to display the main menu to the user
def mainMenu():
    # Load data from files into the employees and payslips dictionaries when the program starts
    loadData()
    
    # Infinite loop to display the main menu continuously until the user chooses to exit
    while True:
        # Displaying the main menu options
        print("\n------- Main Menu -------")
        print("1. Employee Profile")         # Option to access employee profile functions
        print("2. Salary Generator")         # Option to generate net salary for an employee
        print("3. Payslip Profile")          # Option to view or search payslip records
        print("4. Exit")                     # Option to exit the program
        
        # Prompt the user to enter their option
        option = input("Enter your option: ")
        
        # Handle each menu option with if-elif statements to call the corresponding function
        if option == "1": 
            print("Employee Profile has been chosen")
            empProfileSubMenu()              # Calls the sub menu for employee profile procedures
        elif option == "2":  
            print("Salary Generator has been chosen")
            generateNetSalary()              # Calls the procedure to calculate and display net salary
        elif option == "3":  
            print("Payslip Profile has been chosen")
            payslipSubMenu()                 # Calls the sub menu for payslip procedures
        elif option == "4": 
            print("Exiting program.")
            exit()                           # Calls the exit procedure to save data and terminate the program
        else: 
            # Informs the user if their input is invalid and prompts them to re-enter a valid choice
            print("Choice is invalid. Try entering choice again.")


# Call the mainMenu function to start the program.
mainMenu()



