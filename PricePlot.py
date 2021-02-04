## plot current price of stock over specified time
from matplotlib import pyplot as plt
import requests
from bs4 import BeautifulSoup
import time

power_on = str(input("ready to go?\n(y/n): ")).upper()
if power_on == 'Y':
    print("vroom vroom")
    run = True
else:
    run = False



## todo: write list comprehension for plt.plot function to adjust for input lists
# def line_compiler():
    # price_list = [
    # time_list =
    # lines = []
    # for i in range(len(price_list)):
    #    lines.append(price_list[i-1])
    #    lines.append(time_list[i-1])
    #

## todo: flip while & for loops to get prices of different stocks at the same time interval
# def stock_price_parallel():
#    while time_count < maxtime:
#        for i in stonklist:

## todo: create function that plots multiple stock prices in a single plot
# def multiline_chart(symbols):
#    line_compiler()
#    plt.title("Price graph".format(symbol))
#    plt.xlabel("Time")
#    plt.ylabel("Price ($)")
#    plt.autoscale()
#    plt.plot(lines)
#    plt.show()


def draw_pyplot(symbol, x_axis, y_axis):
    ## todo: configure axes to be legible
    ## todo: find how to auto-close plots
    plt.title("{} price graph".format(symbol))
    plt.xlabel("Time")
    plt.ylabel("Price ($)")
    plt.autoscale()
    plt.plot(x_axis, y_axis)
    plt.show()
#    time.sleep(3)
#    plt.close()


def stock_price_linear():
    base_url = r"https://finance.yahoo.com/quote/"
    stonklist = []
    stonk = str(input("Enter Stock Abbreviation: ")).upper()
    stonklist.append(stonk)
    while True:
        looptest = str(input("Enter another stock, or enter 'n' to calculate: ")).upper()
        if looptest != 'N':
            stonklist.append(looptest)
            continue
        else:
            break
    print("I will now begin searching for the prices of {}".format(stonklist))
    maxtime = int(input("How many seconds would you like to track the price? "))
    for i in stonklist:
        time_count = 0
        y_axis = []
        x_axis = []
        print("\n")
        try:
            while time_count < maxtime:
                #start = time.time()
                url = base_url + i
                YFpage = requests.get(url)
                soup = BeautifulSoup(YFpage.content, 'html.parser')
                price = soup.find("span", {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).get_text(strip=True)
                # print("The current price of ${} is {}".format(i, price))
                y_axis.append(price)
                print("found price of {} for time interval {}".format(i, time_count+1))
                x_axis.append(time.strftime('%H:%M:%S', time.localtime()))
                # print("total time taken this loop: ", time.time() - start)
                time_count += 1
                time.sleep(1)
            draw_pyplot(i, x_axis, y_axis)
        except:
            print("I can't find Stock ${}...\nHow awkward...\nMoving on...".format(i))


while run == True:
#    print("testing...")
    stock_price_linear()
