ename=input("enter employee name:")
bs=float(input("basic salary:"))
hra=bs*0.2
ta=bs*0.2
da=bs*0.1

gs=bs+hra+ta+da

pf=gs*0.08
pt=gs*0.03
it=gs*0.06

ns=gs-(pf+pt+it)

print("---------")
print("employee name:",ename)
print("basic salary:",bs)
print("---------",)
print("total addition:")
print("hra:",hra)
print("ta:",ta)
print("da:",da)
print("---------")
print("gross salary",gs)
print("--------")
print("total deduction")
print("pf:",pf)
print("pt:",pt)
print("it",it)
print("net salary:",ns)
print("--------")
