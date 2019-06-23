# This first line is provided for you
#missmatch may occure in the input syntex like ":" etc...

#explaination : we can also write the last condition "else:" but make sure then no
#condition there
# when i enter 0.85 1st elif loop run and print "B"

score = input("Enter Score: ")
k = float(score)
if k >= 0.9 :
    print("A")
elif k >= 0.8 :
    print("B")
elif k >= 0.7 :
    print("c")
elif k >= 0.6 :
    print("D")
elif k < 0.6 :
    print("E")
quit()
