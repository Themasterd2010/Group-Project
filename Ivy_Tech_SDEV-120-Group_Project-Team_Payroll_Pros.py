#Payroll Pros Program
def get_first_name():
    while True:
        first_name = input("Enter first name: ").strip()

        if first_name:
            return first_name
        else:
            print("First name cannot be empty. Please try again.")


def get_last_name():
    while True:
        last_name = input("Enter last name: ").strip()

        if last_name:
            return last_name
        else:
            print("Last name cannot be empty. Please try again.")


def get_employee_id():
    while True:
        Employee_Id = input("Enter employee ID: ").strip()

        if Employee_Id:
            return Employee_Id
        else:
            print("Employee ID cannot be empty. Please try again.")


def get_dependents():
    while True:
        try:
            dependents = int(input("Enter number of dependents: "))

            if dependents < 0:
                print("Number of dependents cannot be negative.")
            else:
                return dependents

        except ValueError:
            print("Please enter a whole number.")


def get_hours_worked():
    while True:
        try:
            hours_worked = float(input("Enter hours worked: "))

            if hours_worked < 0:
                print("Hours worked cannot be negative.")
            else:
                return hours_worked

        except ValueError:
            print("Please enter a valid number.")


def get_hourly_rate():
    while True:
        try:
            hourly_rate = float(input("Enter hourly pay rate: $"))

            if hourly_rate < 0:
                print("Hourly pay rate cannot be negative.")
            else:
                return hourly_rate

        except ValueError:
            print("Please enter a valid number.")


def get_employee_information():
    first_name = []
    last_name = []
    Employee_Id = []
    dependents = []
    hours_worked = []
    hourly_rate = []

    for i in range(10):
        print("\n------------------------------")
        print("Employee", i + 1)
        print("------------------------------")

        first_name.append(get_first_name())
        last_name.append(get_last_name())
        Employee_Id.append(get_employee_id())
        dependents.append(get_dependents())
        hours_worked.append(get_hours_worked())
        hourly_rate.append(get_hourly_rate())

    return first_name, last_name, Employee_Id, dependents, hours_worked, hourly_rate

# Payroll Pros Program
# Gross Pay, State Tax, and Federal Tax Calculations


# Calculate gross pay
def calculate_gross_pay(hours_worked, hourly_rate):

    if hours_worked <= 40:
        gross_pay = hours_worked * hourly_rate

    else:
        regular_pay = 40 * hourly_rate
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * hourly_rate * 1.5

        gross_pay = regular_pay + overtime_pay

    return gross_pay


# Calculate state tax at 5.6%
def calculate_state_tax(pre_tax_amount):

    state_tax = pre_tax_amount * 0.056

    return state_tax


# Calculate federal tax at 7.9%
def calculate_federal_tax(pre_tax_amount):

    federal_tax = pre_tax_amount * 0.079

    return federal_tax

def calculate_pre_and_post_tax():
    # Calculate pre and post tax
    # amounts & save results in a file

        list_of_results = []
        i = 0

        while i < 10:
            # variable setup
            # gross_income will be set in Mike's code, but for testing purposes, I will set it here
            gross_income = float(input("Enter your gross income: "))
            if gross_income <= 0:
                print("Error: You can't have no gross income.")
                raise SystemExit

            def calculate_pre_tax_income(gross_income):
                # Input
                k401_contribution = float(input("Enter your 401k contribution, this amount will be matched by five percent and up to $2,000: "))
                if k401_contribution < 0 or k401_contribution > gross_income:
                    print("Error: Contribution cannot be negative, or more then your income.")
                    return None

                # Processing
                if k401_contribution * 0.05 > 2000:
                    total_matched_amount = 2000
                else:
                    total_matched_amount = k401_contribution * 0.05

                # Output
                print(f"Your matched amount is: {total_matched_amount}")
                print(f"Your total 401k contribution is: {k401_contribution + total_matched_amount}")

                # Additional
                new_income = gross_income - k401_contribution
                print(f"Your pre-tax income is: {new_income}")
                return new_income

            # changing global variables
            pre_income = calculate_pre_tax_income(gross_income)
            if pre_income is not None:
                # safety check to make sure that gross income does change
                print("your new gross income is: " + str(pre_income))

            def calculate_taxes(pre_income):
                # Calculating taxes
                state_tax = pre_income * 0.056
                federal_tax = pre_income * 0.079

                # Output
                print(f"Your state tax is: {state_tax}")
                print(f"Your federal tax is: {federal_tax}")

            calculate_taxes(pre_income)

            def calculate_post_tax_income(pre_income):
                # Calculating post tax income
                state_tax = pre_income * 0.056
                federal_tax = pre_income * 0.079

                post_tax_income = pre_income - (state_tax + federal_tax)

                # Output
                print(f"Your post-tax income is: {post_tax_income}")
                return post_tax_income

            calculate_post_tax_income(pre_income)
            
            list_of_results.append([gross_income, pre_income, calculate_post_tax_income(pre_income)])

            i = i + 1

        print("list_of_results: " + str(list_of_results))

calculate_pre_and_post_tax()

# This is global variable 
employee_list = []



def insert_employee_data():

    for emp_dict in employee_list:
      
        hours_worked= int(emp_dict.get("hours_worked"))
        hourly_rate= int(emp_dict.get("hourly_rate"))
        gross_pay = calculate_gross_pay(hourly_rate, hours_worked)
        total_tax = calculate_taxes(gross_pay)
        net_pay = calculate_net_pay(total_tax, gross_pay)
        emp_dict["net_pay"] = net_pay
    display_employee_data()

#Display employee data in table formate
def display_employee_data():

    for emp in employee_list:        
        print(f"Name: {emp['first_name']} { emp['last_name']}\t employee_id: {emp['employee_id']}\t dependents: {emp['dependents']}\t hours_worked: {emp['hours_worked']}\t hourly_rate: {emp['hourly_rate']}\t net_pay: {emp['net_pay']}")
    