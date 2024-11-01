def invest(amount, rate, years):
    if years==0:
        return amount
    years_amount = invest(amount,rate,years-1)
    after_interest = round(rate*years_amount+years_amount,2)
    print("year",years,": $"+str(after_interest))
    return after_interest
invest(100,.05,4)