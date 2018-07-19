from prettytable import PrettyTable
import datetime
from datetime import timedelta


def addDay(ha, year, month, day):
    ha.append(datetime.date(year, month, day))


def addStandardAccrual(tab, index):
    tbt['Paycheck'].append(index)
    tbt['Date'].append(
        tbt['Date'][-1] + timedelta(days=14))
    tbt['Hours'].append(
        tbt['Hours'][-1] + getTopAccRate(tbt['Date'][-1]))


def adjust(tab, arr, amount):
    for xx in arr:
        if xx > tab['Date'][-2] and xx <= tab['Date'][-1]:
            tab['Hours'][-1] += amount


def checkForTimeOff(arr, xx):
    ll = ""
    vdc = sum(day > tbt['Date'][xx - 1] and day <= tbt['Date'][xx] for day in arr)
    if vdc == 1:
        ll += str(vdc) + " day!"
    if vdc > 1:
        ll += str(vdc) + " days!"
    return ll


def addHoliday(year, month, day):
	addDay(h, year, month, day

)
def addVacation(year, month, day):
	addDay(v, year, month, day)

def getTopAccRate(date):
	# If you've been working for more than seven years you get max
	if dateOfHire + datetime.timedelta(days=365*7) < date:
		return topAccRate[-1]
	else:
		return topAccRate[(date - dateOfHire).days // 365]


# Initialize Holidays and Vacation Day Arrays
h = []
v = []
# Store the TOP Accrual Rate
topAccRate = [5.31, 5.54, 5.77, 6.00, 6.24, 6.47, 6.70, 6.93]

# ===================================================
# ============== USER CONFIGURABLE ==================
# ===================================================

dateOfHire = datetime.date(2018, 4, 7) # The date of your first paycheck
latestPaycheck = datetime.date(2018, 5, 11) # The paycheck you'd like to start at
curBalance = 12.90 # The number of TOP hours you have at the paycheck above
paychecksToCompute = 20 # The number of paychecks you'd like to compute

# Add your Paid Holidays
addHoliday(2018, 5,  28) # Memorial Day
addHoliday(2018, 7,  4 ) # July 4th
addHoliday(2018, 9,  3 ) # Labor Day
addHoliday(2018, 11, 22) # Thanksgiving
addHoliday(2018, 11, 23) # Black Friday
addHoliday(2018, 12, 24) # Christmas Eve
addHoliday(2018, 12, 25) # Christmas Day
addHoliday(2019, 1,  1 ) # New Year's Day
addHoliday(2019, 4,  1 ) # Easter

# Add your Planned Time Off
addVacation(2018, 8,  10) # ShawBra Wedding
addVacation(2018, 8,  13) # ShawBra Wedding
addVacation(2018, 9,  4 ) # Labor Day backpacking?
addVacation(2018, 9,  5 ) # Labor Day backpacking?
addVacation(2018, 9,  6 ) # Labor Day backpacking?
addVacation(2018, 9,  7 ) # Labor Day backpacking?
addVacation(2018, 11, 19) # Visit Dad?
addVacation(2018, 11, 20) # Visit Dad?
addVacation(2018, 11, 21) # Visit Dad?
addVacation(2018, 12, 26) # Christmas Vacation?
addVacation(2018, 12, 27) # Christmas Vacation?
addVacation(2018, 12, 28) # Christmas Vacation?
addVacation(2018, 12, 31) # Christmas Vacation?
addVacation(2019, 1,  2 ) # Christmas Vacation?
addVacation(2019, 1,  3 ) # Christmas Vacation?
addVacation(2019, 1,  4 ) # Christmas Vacation?

# ===================================================
# ============ END USER CONFIGURABLE ================
# ===================================================

# Create TOP Balance Table
tbt = {'Paycheck': [], 'Date': [], 'Hours': []}
tbt['Paycheck'] = []
tbt['Date'] = [latestPaycheck]
tbt['Hours'] = [curBalance]

# Set up table header
t = PrettyTable()
t.field_names = ["Paycheck", "Date", "Days Avail", "Hours Avail", "Vacation", "Paid Holiday"]

# Compute hours and output results
for payPeriod in range(paychecksToCompute + 1):
    # Add the standard accrual amount
    addStandardAccrual(tbt, payPeriod)
    # Adjust for paid holidays
    adjust(tbt, h, 3.5)
    # Adjust for vacation days
    adjust(tbt, v, -8)

    t.add_row([
    	tbt['Paycheck'][payPeriod],
    	tbt['Date'][payPeriod],
    	round((tbt['Hours'][payPeriod] / 8), 2), 		
    	round(tbt['Hours'][payPeriod], 2),
    	checkForTimeOff(v, payPeriod),
    	checkForTimeOff(h, payPeriod)]
    	)

print t