from datetime import datetime, timedelta

class BudgetingSoftware:
    def __init__(self, biweekly_income, credit_card_balance, credit_card_apr):
        """
        Initialize the budgeting software with user inputs.

        Args:
            biweekly_income (float): Post-tax biweekly paycheck amount.
            credit_card_balance (float): Current credit card balance.
            credit_card_apr (float): Annual interest rate (APR) on the credit card.
        """
        self.biweekly_income = biweekly_income
        self.credit_card_balance = credit_card_balance
        self.credit_card_apr = credit_card_apr
        self.fixed_bills = []  # List of (name, amount, due_date)
        self.discretionary_spending = {}  # {"category": priority}

    def calculate_yearly_income(self):
        """
        Calculate total yearly income based on biweekly income.

        Returns:
            float: Total yearly post-tax income.
        """
        return self.biweekly_income * 26  # 26 pay periods in a year

    def calculate_monthly_income(self):
        """
        Calculate monthly post-tax take-home amounts, accounting for months with 3 pay periods.

        Returns:
            dict: Monthly income for each month of the year.
        """
        pass  # Implement biweekly to monthly conversion

    def add_fixed_bill(self, name, amount, due_date):
        """
        Add a fixed bill to the budget.

        Args:
            name (str): Name of the bill (e.g., "Rent").
            amount (float): Amount of the bill.
            due_date (str): Due date in MM/DD format.
        """
        #TODO: due_date string type and structure verification. normalize capitalization of all names. Make sure amount is in USD and follows
        # "xx.xx" or "x.xx" where the structure represents a float 
        self.fixed_bills.append((name, amount, due_date))

    def set_discretionary_spending(self, category, priority):
        """
        Add a discretionary spending category with its priority.

        Args:
            category (str): Name of the spending category (e.g., "Dinners").
            priority (int): Priority of the category (lower numbers are higher priority).
        """
        self.discretionary_spending[category] = priority

    def calculate_fixed_expenses(self):
        """
        Calculate total fixed expenses based on the input bills.

        Returns:
            float: Total fixed expenses for the month.
        """
        pass  # Implement fixed expense calculation

    def calculate_min_credit_card_payment(self):
        """
        Calculate the minimum payment due for the credit card.

        Returns:
            float: Minimum payment (typically 1-3% of balance).
        """
        pass  # Implement calculation for minimum payment

    def allocate_budget(self):
        """
        Allocate the user's budget based on financial principles.

        Returns:
            dict: Allocated amounts for fixed bills, discretionary spending, credit card payments, and savings.
        """
        pass  # Implement budget allocation logic

    def calculate_credit_card_interest(self, payment_amount):
        """
        Calculate potential interest accrued if only a partial payment is made.

        Args:
            payment_amount (float): Amount paid toward the credit card.

        Returns:
            float: Estimated interest to be accrued.
        """
        pass  # Implement interest calculation formula

    def generate_budget_summary(self):
        """
        Generate a detailed budget summary for the user.

        Returns:
            dict: Summary of income, fixed expenses, discretionary spending, savings, and credit card payments.
        """
        pass  # Implement summary generation
    
class MonthlyBudget:
    
    def __init__(self, month, liquid_funds, total_debt):
        self.month = month
        self.liquid_funds = liquid_funds
        self.total_debt = total_debt
        


# Example Usage
def main():
    """
    Main function to run the budgeting program.
    """
    print("Welcome to the Budgeting Software!")

    # Inputs from the user
    biweekly_income = float(input("Enter your post-tax biweekly paycheck: $"))
    credit_card_balance = float(input("Enter your current credit card balance: $"))
    credit_card_apr = float(input("Enter your credit card APR (as a percentage): "))

    # Initialize the budgeting program
    budget = BudgetingSoftware(biweekly_income, credit_card_balance, credit_card_apr)

    # Add fixed bills
    print("\nAdd your fixed bills (enter 'done' to finish):")
    while True:
        name = input("Bill name (or 'done'): ")
        if name.lower() == 'done':
            break
        amount = float(input(f"Enter the amount for {name}: $"))
        due_date = input(f"Enter the due date for {name} (MM/DD): ")
        budget.add_fixed_bill(name, amount, due_date)

    # Set discretionary spending
    print("\nSet discretionary spending categories and priorities (enter 'done' to finish):")
    while True:
        category = input("Spending category (or 'done'): ")
        if category.lower() == 'done':
            break
        priority = int(input(f"Enter the priority for {category} (lower is higher priority): "))
        budget.set_discretionary_spending(category, priority)

    # Example output generation
    print("\nGenerating budget summary...")
    # Call functions to calculate and display the budget
    summary = budget.generate_budget_summary()
    print(summary)


if __name__ == "__main__":
    main()


'''TODO:
- Flesh out the pass sections with proper calculations.
- Add input validation (e.g., correct date formats, numeric checks).
- Create sample outputs for testing the program logic.
'''