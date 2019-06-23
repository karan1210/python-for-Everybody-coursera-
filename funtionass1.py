# This first line is provided for you
#missmatch may occure in the input syntex like ":" etc...

#explaination : Rate calculation by function call "computery"
hrs = input("Enter Hours:")
rate = input("Enter rate:")
def computepay(h,r):

    r = float(rate)
    h = float(hrs)
    if h>=40:
             ovrhrs = (h-40)
             regular = (r*40)
             othrs = ovrhrs * (r *1.5)
             ovrpay = (regular + othrs)
             return(ovrpay)
    else:
        k=h*r
        return(k)
print(computepay(hrs,rate))
