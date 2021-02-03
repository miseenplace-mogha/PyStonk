## plot current price of stock over specified time
from matplotlib import pyplot as plt
import requests
from bs4 import BeautifulSoup
import time

url = r"https://finance.yahoo.com/quote/"
stonklist = []


def draw_pyplot(symbol):
    plt.title("{} price graph".format(symbol))
    plt.xlabel("Time")
    plt.ylabel("Price ($)")
## todo: configure axes min & max
#    plt.axis(min(x_axis), max(x_axis), min(plot_price), max(plot_price))
    plt.autoscale()
    plt.plot(x_axis, plot_price, marker='o')
    plt.show()


## todo: create function that plots multiple stock prices in a single plot
## todo: write list comprehension for plt.plot function to adjust for input lists
## todo: flip while & for loops to get prices of different stocks at the same time interval
# def multiline_chart(symbols):
#    plt.title("Price graph".format(symbol))
#    plt.xlabel("Time")
#    plt.ylabel("Price ($)")
#    plt.axis(min(x_axis), max(x_axis), min(plot_price), max(plot_price))
#    plt.autoscale()
#    plt.plot()
#    plt.show()

stonk = str(input("Enter Stock Abbreviation: ")).upper()
stonklist.append(stonk)
while True:
    looptest = str(input("Enter another stock, or enter 'n' to calculate: ")).upper()
    if looptest != 'N':
        stonklist.append(looptest)
        continue
    else:
        break
#print(stonklist)
maxtime = int(input("How many seconds would you like to track the price? "))
for i in stonklist:
    plot_price = []
    time_count = 0
    x_axis = []
    print("\n")
    try:
        while time_count < maxtime:
            #start = time.time()
            urla = url + i
            YFpage = requests.get(urla)
            soup = BeautifulSoup(YFpage.content, 'html.parser')
            price = soup.find("span", {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).get_text(strip=True)
            # print("The current price of ${} is {}".format(i, price))
            plot_price.append(price)
            print("found price of {} for time interval {}".format(i, time_count+1))
            x_axis.append(time.strftime('%H:%M:%S', time.localtime()))
            # print("total time taken this loop: ", time.time() - start)
            time_count += 1
            time.sleep(1)
        draw_pyplot(i)
    except:
        print("I can't find that stock...\nHow awkward...\nMoving on...")