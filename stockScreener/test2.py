import yfinance as yf

# Lists
data_set = []
stocks = []

# Import Stocks from File
myfile = open('test_list.txt', 'r')
for word in myfile:
    if word.rstrip() != "":
	stocks.append(word.rstrip())

# Import Data
print("[****************IMPORTING DATA******************]")
data = yf.download(stocks, period="3mo") #, start="2021-01-01", end="2021-04-02")
data2 = yf.download(stocks, period="6mo") #, start="2021-01-01", end="2021-04-02")

# Print Stock List
print(stocks)

#print(data)
print("***************************************************************************")

for i in stocks:
    open = data['Close'][i][0]
    close = data['Close'][i][-1]
    three_pg = round((close-open)/open*100,2)

    open = data2['Close'][i][0]
    close = data2['Close'][i][-1]
    six_pg = round((close-open)/open*100,2)

    data_set.append([i,three_pg,six_pg])

data_set = sorted(data_set, key = lambda x: (x[1], x[2]),reverse=True)

print(data_set)



#print(sorted(data_set, key = lambda x: x[2],reverse=True))

print("***************************************************************************")
#print(three)
print("***************************************************************************")
#print(six)


# Rank Stocks by Performance



# 5-Day Pullback



# 200 Day moving average hit? (move to cash)



# Russell 2000 6-month low? (move to cash)
