def stockticker(stocklist):
    import sys, subprocess
    ## use pip to install 'bs4' and 'requests' modules:
    consent = input("Can I try installing the necessary libraries, bs4 & requests, to run this script?\n (y/n): ")

    def pip_install():
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', 'bs4', 'requests'])
        except:
            print("necessary libraries already installed")

    def pip_uninstall():
        subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', '-q', 'bs4', 'requests'])
        print("Uninstall complete")

    if consent == 'y':
        print("installing necessary libraries \n mwahahahaha")
        pip_install()
    else:
        print("Ok, I might try to run this script, but it will not work without the necessary libraries")


    ## code to manually build a list of stocks to search
    #stocklist = []
    #while True:
        #stock = str(input("Enter Stock Abbreviation: ")).upper()
        #stocklist.append(stock)
        #looptest = str(input("Enter another stock, or enter 'n' to calculate: \n"))
        #if looptest != 'n' or looptest != "'n'":
        #    continue
        #elif looptest == 'n':
        #    break

    ## search Google Finance -- NYSE & NASDAQ for stock price
    import requests
    from bs4 import BeautifulSoup
    url = r'https://www.google.com/finance/quote/'
    for i in stocklist:
        try:
            #print('building the URL...')
            urla = url + i +':NYSE'
            YFpage = requests.get(urla)
            #print('retrieving the html...')
            soup = BeautifulSoup(YFpage.content, 'html.parser')
            #print('searching for the price on NYSE...')
            price = soup.find("div", {"class":"YMlKec fxKbKc"}).get_text(strip=True)
            print("The current price of ${} is {}".format(i, price))
        except:
            #print("couldn't find the price on NYSE...")
            urla = url + i + ':NASDAQ'
            YFpage = requests.get(urla)
            soup = BeautifulSoup(YFpage.content, 'html.parser')
            #print('now searching for the price on NYSE...')
            price = soup.find("div", {"class": "YMlKec fxKbKc"}).get_text(strip=True)
            print("The current price of ${} is {}".format(i, price))


    ## ask to delete installed libaries
    ask_delete = str(input("Would you like me to remove the 'bs4' and 'requests' libraries? \n(y/n): "))
    if ask_delete == 'y':
        pip_uninstall()
    else:
        print("Thank you for letting me know, I will leave these libraries installed")

