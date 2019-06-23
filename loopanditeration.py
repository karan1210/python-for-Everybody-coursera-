# This first line is provided for you
#missmatch may occure in the input syntex like ":" etc...

#explaination : find the max and min among the all input numbers

largest = None
smallest = None
while True:
    try:
        num =input("Enter a number: ")
        if num == "done":
            break

        num = int(num)
        if largest is None or largest < num:
            largest = num
        elif smallest is None or smallest > num:
             smallest = num
    except ValueError:
        print("Invalid input")

print ("Maximum is", largest)
print ("Minimum is", smallest)
