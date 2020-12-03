
income = int(input("Enter company income ($) - \n"))
outcome = int(input("Enter company outcome ($) -\n"))
employees = int(input("Employees number - \n"))

if income > outcome:
    net_profit = income - outcome
    print("Good! Your business is profitable! You have earned - ", net_profit,"$")
    roe = net_profit / income
    print("Your ROE = ", roe)
    profit_per_person = net_profit // employees
    print("Profit per person - ", profit_per_person, "$")
else:
    print("Very sad! Business is unprofitable :( ")
