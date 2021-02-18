largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    
    else:
        try:
            num=int(num)
            print(num)
            if largest is None and smallest is None:
                smallest=num
                largest=num
            elif num<smallest:
                smallest=num
            elif num>largest:
                largest=num
        except:
            print("Invalid input")
    

print("Maximum is", largest)
print("Minimum is", smallest)