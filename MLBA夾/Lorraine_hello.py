#
#Lorraine, 2026/2/25
#Lorraine_Hello.py
#print Hello
#

name = "THU"
price = 250
units_sold = 1200

total_sales = price* units_sold
discount = total_sales*0.05
net_sales = total_sales - discount
print(f"total_sales:${total_sales}")
print(f"Discount    : ${discount:,.2f}")
print(f"Net Sales   : ${net_sales:,.2f}")

customer_age  = 35
account_value = 120_000

if customer_age >= 30 and account_value >= 100_000:
    print("Eligible for premium wealth management services.")
else:
    print("Standard account services apply.")