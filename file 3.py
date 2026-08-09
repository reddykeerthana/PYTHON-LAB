# Electricity Bill Generator

# Accept user details
consumer_name = input("Enter Consumer Name: ")
consumer_id = input("Enter Consumer ID: ")
previous_reading = float(input("Enter Previous Meter Reading (kWh): "))
current_reading = float(input("Enter Current Meter Reading (kWh): "))
cost_per_unit = float(input("Enter Cost per Unit (₹): "))

# Calculate bill
units_consumed = current_reading - previous_reading
energy_charge = units_consumed * cost_per_unit
electricity_duty = energy_charge * 0.05
fixed_meter_charge = 100
net_bill = energy_charge + electricity_duty + fixed_meter_charge

# Display bill
print("\n" + "=" * 40)
print("       ELECTRICITY BILL")
print("=" * 40)
print(f"Consumer Name      : {consumer_name}")
print(f"Consumer ID        : {consumer_id}")
print(f"Previous Reading   : {previous_reading} kWh")
print(f"Current Reading    : {current_reading} kWh")
print(f"Units Consumed     : {units_consumed} kWh")
print(f"Cost per Unit      : ₹{cost_per_unit:.2f}")
print("-" * 40)
print(f"Energy Charge      : ₹{energy_charge:.2f}")
print(f"Electricity Duty   : ₹{electricity_duty:.2f}")
print(f"Fixed Meter Charge : ₹{fixed_meter_charge:.2f}")
print("-" * 40)
print(f"Net Bill Amount    : ₹{net_bill:.2f}")
print("=" * 40)
print("Thank You!")
