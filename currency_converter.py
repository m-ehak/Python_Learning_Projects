amount = float(input("Enter the amount you want to convert: "))
source_currency = input("Source Currency (USD, EUR, JPY, GBP, AUD, INR): ").upper()
target_currency = input("Target Currency (USD, EUR, JPY, GBP, AUD, INR): ").upper()

exchange_rates = {
    "USD": 1,
    "EUR": 0.85,
    "JPY": 110,
    "GBP": 0.75,
    "AUD": 1.30,
    "INR": 83.0
}

if source_currency not in exchange_rates or target_currency not in exchange_rates:
    print("Sorry, we do not support one or both of the currencies entered.")
else:
    amount_in_usd = amount / exchange_rates[source_currency]
    
    converted_amount = amount_in_usd * exchange_rates[target_currency]
    print(converted_amount)