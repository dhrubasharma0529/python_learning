import requests
url = "https://www.onlinekhabar.com/smtm/search-list/tickers"

r = requests.get(url=url)
if r.status_code == 200:
    data = r.json()['response']
    a=[]
    for result in data:
        if result['sector'] == 'Bond':
            print(result['ticker_name'])
            a.append(result['sector'])
    print(a)


        
    
    # for value in data.values():
    #     a = value 
    #     for i in a:
    #         for value in i.values():
    #             print(value)
    #         print('--------------')
