c=input("enter a sentense:")
for i in "aeiouAEIOU":
    c = c.replace(i,"")
print(c)