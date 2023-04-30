# To print numbers in Python to print number of unique letter in a string 
s=input(" ").lower()
l=[]
for i in s:
    if i not in l:
        l.append((i))
temp=""
for j in l:
     temp+=j+","
# l=str(l)
# l.strip(",")
print(temp.strip(","))
    


