# This first line is provided for you
#missmatch may occure in the input syntex like ":" etc...

#explaination : when working hrs go beyond 40 hrs rate increase 1.5 time so..
# we mul 1.5*rate

hrs = input("Enter Hours:")
p = input("Enter rate:")
r = float(p)
h = float(hrs)
if h>=40:
    k=(h-40.0)*(1.5*r)+(40*r)
else:
     k=h*r
print(k)
quit()
