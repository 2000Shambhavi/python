p=float(input("enter the principle amount:"))
r=float(input("enter the rate of interest:"))
t=float(input("enter the number of years:"))

ci=p*(pow((1+r/100),t))
        
print("compound interest:",ci)
