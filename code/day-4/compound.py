principle=int(input("Enter principle amount:"))
time=int(input("Enter time duration:"))
rate=int(input("Enter rate of interest"))
amount = (principle * (1+(int(rate)/100))**time)
compound_interest=amount-principle;
print("Total amount:-  ",amount)
print("compound interest:- ",compound_interest)
