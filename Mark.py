

#Mark = int(input("Enter your Mark: "))

#if Mark >= 85:
#    print("Distinction")
#elif Mark >= 65:
#    print("Pass")
#else:
#    print("Fail")


Mark = int(input("Enter your Mark: "))

if Mark >= 85:
    print("Distinction")
if not ( 65 > Mark < 85):
    print("Pass")
else:
    print("Fail")