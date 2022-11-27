names=["ojas","ashish","vedant","kartik","tanay"]
#break is used for breaking a statement i.e. the names after the breaked one will not be executed
for name in names:
    if(name=="kartik"):
        break
    print(name)

#continue is used to print all the names without breaking the loop
for name in names:
    if(name=="kartik"):
        continue
    print(name)

