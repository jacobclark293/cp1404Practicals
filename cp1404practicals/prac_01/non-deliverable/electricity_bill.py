TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
price_per_kwh = int(input("Enter cents per Kwh: "))
daily_kwh_use = float(input("Enter daily use in Kwh: "))
number_billing_days = int(input("Enter number of billing days: "))

estimated_bill = (price_per_kwh * daily_kwh_use * number_billing_days) / 100
print(f"Estimated bill: ${estimated_bill}")

