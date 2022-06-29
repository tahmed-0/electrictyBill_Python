powerConsumption = input("Enter power consumption\n")
HoursPerDay = input("Enter hours of use per day\n")
kWh = input("Enter 1 kilowatt-hour (kWh) cost\n")

eConsumption = (powerConsumption * HoursPerDay) / 1000
totalCostPerDay = float(eConsumption * 12) / 100


monthlyCost = totalCostPerDay * 30.45
yearlyCost = monthlyCost * 12

print("Electricity cost per day: $" + str(totalCostPerDay))
print("Electricity cost per month: $"+str(monthlyCost))
print("Electricity cost per year: $"+str(yearlyCost))


