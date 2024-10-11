# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month, 
# and the amount of state and county sales tax collected. 
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.  
# Write a program that asks the user to enter the total sales for the month.  
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program
county_tax = 0.25
state_tax = 0.5
county_sales_tax = 0
state_sales_tax = 0
sales_total = 0



def main():
    print("Sales tax calculator")
    sales_total = float(input("What was your total sales this month?"))
    county_sales_tax = sales_total * county_tax
    state_sales_tax = sales_total * state_tax
    total_sales_tax = county_sales_tax + state_sales_tax
    total_tax = round(total_sales_tax, 2)
    print(f"County Sales Tax: {county_sales_tax}")
    print(f"State Sales Tax: {state_sales_tax}")
    print(f"Total Sales Tax: {total_sales_tax}")

main()