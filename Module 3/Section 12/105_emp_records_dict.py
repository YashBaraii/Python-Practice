# Create a dictionary of employee records with nested data (emp_id: {name, salary}).

import json
from os.path import exists

FILE = "105_emp_data.json"


def load_data():
    if exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(emp_records):
    with open(FILE, "w") as f:
        json.dump(emp_records, f, indent=4)


emp_records = load_data()


def add_employee(emp_records):
    print("\n--- Add Employee:\n")

    try:
        emp_id = int(input("\nEnter the employee id: "))
    except ValueError:
        print("\n--- Err: Emp ID must and integer")
        return

    emp_name = input("Enter employee name: ")
    try:
        emp_salary = float(input("Enter employee salary: "))
    except ValueError:
        print("\n--- Err: Emp salary must and float or integer")
        return

    emp_id = str(emp_id)
    if emp_id not in emp_records:
        emp_records[emp_id] = {}
    emp_records[emp_id]["name"] = emp_name
    emp_records[emp_id]["salary"] = emp_salary

    print(f"\n--- Successfully added {emp_name} into the records.")
    save_data(emp_records)


def update_salary(emp_records):
    print("\n--- Update Employee:\n")

    try:
        emp_id = int(input("\nEnter the employee id: "))
    except ValueError:
        print("\n--- Err: Emp ID must and integer")
        return

    emp_id = str(emp_id)
    if emp_id in emp_records:
        try:
            emp_salary = float(input("Enter employee's new salary: "))
        except ValueError:
            print("\n--- Err: Emp salary must and float or integer")
            return

        emp_records[emp_id]["salary"] = emp_salary
        print(
            f"\n--- Successfully updated {emp_records[emp_id]["name"]}'s salary into the records."
        )
        save_data(emp_records)
    else:
        print("\n--- Err: Employee not found in records!")


def remove_employee(emp_records):
    print("\n--- Remove Employee:\n")

    try:
        emp_id = int(input("\nEnter the employee id: "))
    except ValueError:
        print("\n--- Err: Emp ID must and integer")
        return

    emp_id = str(emp_id)
    if emp_id in emp_records:

        emp_records.pop(emp_id)
        print(f"\n--- Successfully removed employee ID {emp_id} from the records.")
        save_data(emp_records)
    else:
        print("\n--- Err: Employee not found in records!")


def show_employees(emp_records):
    print("\n--- Show Employee:\n")

    print("    E_ID  E_Name    E_Salary")
    print("    ----  ------    --------")
    for emp in emp_records:
        print(
            f"    {emp}.  {emp_records[emp]["name"]}  -  ₹ {emp_records[emp]["salary"]}"
        )
    print()


def search_employee_by_id(emp_records):
    print("\n--- Search Employee:\n")

    try:
        emp_id = int(input("\nEnter the employee id: "))
    except ValueError:
        print("\n--- Err: Emp ID must and integer")
        return

    emp_id = str(emp_id)
    if emp_id in emp_records:
        print("    E_ID  E_Name    E_Salary")
        print("    ----  ------    --------")
        print(
            f"    {emp_id}.  {emp_records[emp_id]["name"]}  -  ₹ {emp_records[emp_id]["salary"]}"
        )
    else:
        print("\n--- Err: Employee not found in records!")


try:
    print("\n----- EMPLOYEE RECORDS SYSTEM -----\n")

    while True:
        print("\n1. Add new employee")
        print("2. Update employee salary")
        print("3. Remove employee by ID")
        print("4. Show all employee details")
        print("5. Search employee by ID: ")
        print("6. EXIT !")

        try:
            choice = int(input("-> Enter your choice: "))
        except ValueError:
            print("\n--- Err: Choice must an integer !")
            continue

        match (choice):
            case 1:
                add_employee(emp_records)
            case 2:
                update_salary(emp_records)
            case 3:
                remove_employee(emp_records)
            case 4:
                show_employees(emp_records)
            case 5:
                search_employee_by_id(emp_records)

            case 6:
                save_data(emp_records)
                break
            case _:
                print("\n--- Err: Please choose a valid option !")

except KeyboardInterrupt:
    print("\n\nProgram interrupeted by user!")
    save_data(emp_records)
