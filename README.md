# Payroll Redefined: A Complete Guide to Automated Salary Management

## 📚 Introduction

The Payroll Management System is a Python-based application developed to streamline payroll processes within organizations by automating essential tasks related to employee compensation. Designed with a modular structure, the system provides functionalities for managing employee profiles, calculating salaries, generating payslips, and maintaining accurate records. By integrating business rules directly into the system, it ensures data consistency, automates salary adjustments based on predefined criteria, and reduces the manual workload for Human Resources teams.

## 📋 Key Areas of Discussion

### Section 1: Task Overview

#### 📌 System Design and Interface:

    ▪️ Design a Main Menu to navigate the system, with clear options for employee and payslip management.
    
    ▪️ Implement submenus for both employee profiles and payslips, with a consistent and intuitive layout.


#### 📌 Employee Record Management:

    ▪️ Add Employee: Collect employee ID, name, department, and salary components; validate input types.
    
    ▪️ Update Employee: Allow updates to employee details and monthly payslip information, with ID and date checks.

    ▪️ View Employee: Display a list of all employees in a formatted table.

    ▪️ Delete Employee: Fully remove employee details, including associated payslips.

#### 📌 Salary and Payslip Management:

    ▪️ Generate Net Salary: Apply rules for calculating net salary, including EPF, bonuses, and tax based on thresholds.
    
    ▪️ Payslip Generation: Allow calculation of monthly salary, including a quick calculation option that does not save data.

    ▪️ View and Search Payslip: Implement functions to view payslips for specific months or an entire year, organizing data by employee ID.


#### 📌 Data Storage and Persistence:

    ▪️ Use JSON files (employees.json and payslips.json) to store employee and payslip data, ensuring data persistence across sessions.
    
    ▪️ Develop procedures to load and save data efficiently to maintain the state of the system.


#### 📌 Input Validation:

    ▪️ Implement functions to validate user input across various data types (integer, float, string, and specific employee ID formats) to prevent errors and maintain system robustness.
    

#### 📌 Additional Functionalities:

    ▪️ Error handling for non-existent records or invalid inputs, providing clear feedback for re-entry.
    

#### 📌 Exit Protocol:

    ▪️ Ensure the program has a clear exit procedure that saves any pending changes to employee and payslip data.


#### 📌 Documentation and Testing:

    ▪️ Document assumptions, functions, and design decisions (including pseudocode).
    
    ▪️ Run extensive testing, covering valid, boundary, and error cases, with screenshots for demonstration.

---
### Section 2: System Assumptions and Constraints

    ▪️ Each employee has a unique ID in the format "TP00001" to "TP99999," stored as a string.
    
    ▪️ The system can manage up to 99,999 employees.

    ▪️ Gross salary is calculated as (Basic Salary + Allowance + Bonus + Overtime) with an 11% EPF deduction.
    
    ▪️ Net salary adjustments: 5% bonus for gross salaries under RM2000; 6% tax for gross salaries over RM3000; no adjustments for salaries between RM2000 and RM3000.

    ▪️ All salary values are assumed accurate, treated as amounts in Ringgit Malaysia (RM).

    ▪️ Employee and payslip data are stored in employees.json and payslips.json files.

    ▪️ The system is designed for single-user operation with no concurrent access.

    ▪️ No security features are assumed, such as authentication or malicious input handling.

    ▪️ "Function" and "Procedure" terms are used to distinguish tasks that return results from those that do not.

---

### Section 3: Proposed Improvements

    ▪️ Implement a delete payslip procedure to remove individual payslips.
    
    ▪️ Refine the viewEmployee function by ordering records for easier access.

