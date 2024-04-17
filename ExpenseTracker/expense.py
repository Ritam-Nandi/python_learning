class Expenses:
    def __init__(self,categoryName,expenseValue,expenseDate):
        self.categoryName=categoryName
        self.expenseValue=expenseValue
        self.expenseDate=expenseDate
    
    def printExpense(self):
        print ("Category Name : %s  Expense Value: %s Expense Date: %s" % (self.categoryName,self.expenseValue,self.expenseDate))

class Category:
    def __init__(self,categoryName,expenseValue):
        self.categoryName=categoryName
        self.expenseValue=expenseValue


allExpenses = []
allCategories = []

userInput=6
while(userInput!=5):
    print("\nExpense Tracker Menu:\n1. Add Expense \n2. Add Category \n3. View Expenses\n4. View Categories\n5. Exit ")
    userInput= int(input())

    if userInput == 1:
        print("Enter the date of the expense in the format YYYY-MM-DD")
        dateExp=input()
        print("Enter the amount of the expense")
        amountExp=int(input())
        print("Enter the category of the expense") 
        categoryExp=input()
        print("\n")
        ep=Expenses(categoryExp,amountExp,dateExp)
        flagValue=0
        for i in range(len(allCategories)):
            if allCategories[i].categoryName == categoryExp:
                flagValue=1
                allExpenses.append(ep)
                allCategories[i].expenseValue = allCategories[i].expenseValue + amountExp
                
        if flagValue == 0:
            print("Catefory does not exist")
        

    elif userInput == 2:
        print("Enter the name of the new category")
        categoryInput=input()
        cat=Category(categoryInput,0)
        allCategories.append(cat)


    elif userInput == 3:
        print("The application will display the total expenses for each category")
        for i in allCategories:
            print("Category Name: %s  Total Expense: %d" % (i.categoryName, i.expenseValue))


    elif userInput == 4:
        print("The application will display a list of available categories")
        for i in allCategories:
            print(i.categoryName)


    elif userInput == 5:
        print("Thank you for using this Expense Tracker")


    else:
        print("Please enter a valid option")
        