from prettytable import PrettyTable
import numpy as np

# User Config
minCost = float(290000)
maxCost = float(390000)
granCost = 10000
minInterest = 4.1
maxInterest = 5.1
granInterest = 0.05
downPayment = float(20)
# End User Config

numberOfPayments = float(30) * 12

t = PrettyTable()

temp = []
for house in np.arange(minCost, maxCost + 1, granCost):
	headercell = "$" + str(format(house, ',')) # + " Loan"
	temp.append(headercell)
t.field_names = [""] + temp

for rate in np.arange(minInterest, maxInterest + granInterest, granInterest):
	row = [str(rate) + "%"]
	for house in np.arange(minCost, maxCost + 1, granCost):
		loan = float(house)
		interest = float(rate)/100/12
		monthlyPayments = loan * (interest * (1 + interest) ** numberOfPayments) / ((1 + interest) ** numberOfPayments - 1)
		totalCost = round(numberOfPayments * monthlyPayments, 2)
		costOfLoan = round(totalCost - house, 2)

		cell = "$" + str(format(totalCost, ','))
		# cell += "\nLC: $" + str(format(costOfLoan, ','))

		row.append(cell)

	t.add_row(row)
	
print("==================================================================")
print("The table shows the total cost of a loan at a given interest rate.")
print("Interest rate is on the left, loan amount is on the top.")
print("==================================================================")
print("")
print(t)	
