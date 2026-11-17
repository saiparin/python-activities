def calculate_change(payment, bill):
    return payment - bill

money_paid = 4.0
bill_total = 2.50

change = calculate_change(money_paid, bill_total)
print(f"The shopkeeper should return: ${change:.2f}")