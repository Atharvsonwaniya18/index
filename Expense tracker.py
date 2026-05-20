expensesList = []
print("Welcome To Expense Tracker")

while True :
    print("======MENUE=====")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Spent")
    print("4. EXIT")

    choice = int(input("Enter your choice --->"))

    #ADD EXPENSE

    if(choice ==1):
        date = input("Enter a date of expense :")
        category = input("Category of Expense :")
        description = input("Tell about your purchase :")
        amount = float(input("Enter the amount :"))

        expense = {
            "Date" : date,
            "Category" : category,
            "Description" : description,
            "Amount" : amount,
        }
        expensesList.append(expense)
          
        print("\n DONE , YOUR EXPENSES IS ADDED SUCCESSFULLY")

    elif(choice ==2):
        if(len(expensesList)==0):
            print("NO Expenses are added , Spend some money")

        else:
            print("This is your expense")

            count =1
            for eachspend in expensesList:
                print(f'spend number {count} --> {eachspend["Date"]} , {eachspend["Category"]} , {eachspend["Description"]} , {eachspend["Amount"]}')
                count = count + 1

    elif(choice ==3):
        total = 0
        for eachspend in expensesList:
            total = total + eachspend["Amount"]            

            print("\n Total Spend =" , total)
              
    elif(choice ==4):     
         print("Thanks For Using Our System")
         break
    
    else:
        print("INVALID CHOICE , TRY AGAIN")