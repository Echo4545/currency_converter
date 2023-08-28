class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates
    
    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.rates or to_currency not in self.rates:
            return "Currency not supported"
        
        conversion_rate = self.rates[to_currency] / self.rates[from_currency]
        converted_amount = amount * conversion_rate
        return converted_amount

# Currency exchange rates

exchange_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.72,
    "JPY": 110.20,
    "CAD": 1.25,
    # Add more exchange rates here
}

converter = CurrencyConverter(exchange_rates)

while True:
    print("Available currencies:", ", ".join(exchange_rates.keys()))
    from_currency = input("Enter the source currency (e.g., USD): ").upper()
    to_currency = input("Enter the target currency (e.g., EUR): ").upper()

    amount = float(input("Enter the amount: "))
    
    converted_amount = converter.convert(amount, from_currency, to_currency)
    print(f"{amount:.2f} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}")

    another_conversion = input("Do you want to perform another conversion? (y/n): ")
    if another_conversion.lower() != 'y':
        print("Goodbye!")
        break
