#stock Portfolio Tracker
prices={"AAPL": 180, "TSLA": 250, "GOOGL": 120, "AMZN": 100, "MSFT": 150} # Hardcoded stock prices — edit this dictionary to add/change stocks or prices

sharevalues=input("Enter the number of shares for each stock (comma-separated): ")
sharenames=input("Enter the names of each stock in the same order using capital letters (comma-separated): ")


sharevalueslist = [int(x.strip()) for x in sharevalues.split(",")]
shareslist = [x.strip() for x in sharenames.split(",")]
result={}

for i in range(len(shareslist)):
    if shareslist[i] not in prices:
        print( "the stock", shareslist[i], "does not exist in the dictionary")
        continue
    else: 
            result[shareslist[i]]=sharevalueslist[i]*prices[shareslist[i]]

print("TOTAL:",sum(result.values()))           
print(result)  

   
