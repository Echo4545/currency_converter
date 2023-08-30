# Python program to convert the currency
# of one country to that of another country

# Import the modules needed
import requests
import json

class Currency_convertor:
	# empty dict to store the conversion rates
	rates = {}
	def __init__(self, url):
		data = requests.get(url).json()

		# Extracting only the rates from the json data
		self.rates = data["rates"]

	# function to do a simple cross multiplication between
	# the amount and the conversion rates
	def convert(self, from_currency, to_currency, amount):
		initial_amount = amount
		if from_currency != 'EUR' :
			amount = amount / self.rates[from_currency]

		# limiting the precision to 2 decimal places
		amount = round(amount * self.rates[to_currency], 2)
		print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))

# Driver code
if __name__ == "__main__":

	# YOUR_ACCESS_KEY = 'GET YOUR ACCESS KEY FROM fixer.io'
	url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

querystring = {"from":"from_country","to":"to_country","amount":"amount"}

headers = {
	"X-RapidAPI-Key": "a322f610f3mshc1ad9ed367e92d6p1fffa0jsn3f04cff0f7bb",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
    c = Currency_convertor(url)
	from_country = input("From Country: ")
	to_country = input("TO Country: ")
	amount = int(input("Amount: "))

	c.convert(from_country, to_country, amount)

