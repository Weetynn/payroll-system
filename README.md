# Payroll Redefined: A Complete Guide to Automated Salary Management

## 📚 Introduction

The Payroll Management System is a Python-based application developed to streamline payroll processes within organizations by automating essential tasks related to employee compensation. Designed with a modular structure, the system provides functionalities for managing employee profiles, calculating salaries, generating payslips, and maintaining accurate records. By integrating business rules directly into the system, it ensures data consistency, automates salary adjustments based on predefined criteria, and reduces the manual workload for Human Resources teams.

## 📋 Task Overview

#### 📌 Main Program and Interface Design:

    ▪️ Develop a structured Main Menu to facilitate navigation across system functions.
    
    ▪️ Implement submenus for managing employee profiles and payslips, allowing user access to specific operations like adding, updating, and deleting records.
    

#### 📌 Employee Record Management:

    ▪️ Create functionality for adding new employees, including essential details such as Employee ID, name, department, and salary components.
    
    ▪️ Include procedures to view, update, and delete employee information.

    ▪️ Ensure data validation for employee details, ensuring consistency and accuracy.


#### 📌 Salary and Payslip Management:

    ▪️ Develop a procedure to generate payslips, calculating net salary based on defined components (basic salary, allowance, bonus, overtime).
    
    ▪️ Implement rules for EPF deduction and additional adjustments (5% bonus for gross salaries below RM2000; 6% tax for gross salaries above RM3000).

    ▪️ Enable functionality to view and search specific payslips by employee ID, month, and year.

    ▪️ Provide a consolidated view for all payslips of a specified employee, organized by year.


#### 📌 Data Storage and Persistence:

    ▪️ Use JSON files (employees.json and payslips.json) to store employee and payslip data, ensuring data persistence across sessions.
    
    ▪️ Develop procedures to load and save data efficiently to maintain the state of the system.


#### 📌 Input Validation:

    ▪️ Implement functions to validate user input across various data types (integer, float, string, and specific employee ID formats) to prevent errors and maintain system robustness.
    

#### 📌 Additional Functionalities:

    ▪️ Include an error-handling feature to manage non-existent records during employee and payslip searches.
    
    ▪️ Design procedures for quick and temporary net salary calculations without saving the data.
    

#### 📌 Exit Procedure:

    ▪️ Ensure the program has a clear exit procedure that saves any pending changes to employee and payslip data.


#### 📌 Documentation and Testing:

    ▪️ Document each function and procedure, including pseudocode for logical flow and explanations.
    
    ▪️ Test the system thoroughly using sample inputs, capturing valid and invalid inputs to demonstrate functionality and error handling.

