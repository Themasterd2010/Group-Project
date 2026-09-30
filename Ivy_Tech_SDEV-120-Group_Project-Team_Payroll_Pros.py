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