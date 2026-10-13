stocks={
    'APPLE':180,
    'GOOGLE':130,
    'TATA':140
}
investment=[]
n=int(input("Enter no of stocks:"))
for i in range(n):
    name=input("Enter name of stock:").upper()
    quan=int(input(f"Enter quantity {name}:"))
    if name in stocks:
        price=stocks[name]
        investment.append(price*quan)
    else:
        print("Stocks not found!")
print("Total investment")
print("----------------")
print(sum(investment))