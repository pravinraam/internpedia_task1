import requests

def currency_converter(amount, from_currency, to_currency):
    api_key = 'fca_live_W7jxHpsZjflsbMnBe8W6opDo2iCW4rpcAXpScQh4'
    url = f'https://api.freecurrencyapi.com/v1/latest?apikey={api_key}&currencies={from_currency}%2C{to_currency}'
    
    response = requests.get(url)
    data = response.json()
    
    if 'error' in data:
        print(data['error']['message'])
        return None
    
    rates = data['data']
    from_rate = rates[from_currency]
    to_rate = rates[to_currency]
    
    converted_amount = amount * (to_rate / from_rate)
    
    return converted_amount

def main():
    while True:
        try:
            amount = float(input("Enter amount to convert: "))
        except:
            print('-',len('Enter only number...!!'))
            print('Enter only number...!!')
            print('-'*len('Enter only number...!!'))
        from_currency = input("Enter from currency (e.g., USD): ").upper()
        to_currency = input("Enter to currency (e.g., EUR): ").upper()
        
        if from_currency == 'QUIT' or to_currency == 'QUIT' or from_currency == '' or to_currency == '':
            print("Exiting...")
            break
        
        result = currency_converter(amount, from_currency, to_currency)
        
        if result is not None:
            print(f"{amount} {from_currency} = {result:.2f} {to_currency}")

if __name__ == "__main__":
    main()
