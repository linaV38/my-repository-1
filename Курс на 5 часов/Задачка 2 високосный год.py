year_ = input("Enter the year ")
if int(year_) % 100 == 0 and int(year_) % 400 > 0 and int(year_) % 4 == 0:
    print("non-leap year")
elif int(year_) % 4 == 0:
        print("leap year")
else:
    print("non-leap year")







