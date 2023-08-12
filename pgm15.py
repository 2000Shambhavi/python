pname=input("enter the product name:")
qty=int(input("enter the qty:"))
rate=float(input("enter the rate:"))

gamt=qty*rate
damt=gamt*0.1
namt=gamt-damt

print("\n gross amount payable",gamt);
print("\n less discount amount",damt);
print("\n net amount payable",namt);
