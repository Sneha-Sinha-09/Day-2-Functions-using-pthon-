#FUNCTIONS

def func1():
    print("This is a function.")
func1()


def func2(num1,num2):
    print("num1",num1,"num2",num2)
func2(10,20)

def func3(num1,num2):
    sum=num1+num2
    return sum
print("Value returned",func3(100,200))

def func4(num1,num2):
    sum=num1+num2
    return sum
print("Value returned:",func4(10,10.2))

def func5(num1,num2):
    sum=float(num1)+num2
    return sum
print("Value returned=",func5('10',20.2))

#Categories of functions
#Based on arguments

#1:Positional arguments
def function1(num1,num2,num3,num4):
    print("num1=",num1,"num2=",num2,"num3=",num3,"num4=",num4)
function1(10,20,30,40)
function1(100,200,300) #ERROR missing one required positional argument (TYPE ERROR)
function1(1,2,3,4,5) #ERROR only 4 arguments are required but 5 are given (TYPE ERROR)

def function1(num1,num2,num3,num4):
    print("num1=",num1,"num2=",num2,"num3=",num3,"num4=",num4)
function1(num4=10,num1=20,num3=30,num2=40)

def func6(name,rollno,branch,collegename="GIET"):
    print(name,rollno,branch,collegename)

func6("Aditya",199,"CSE")
func6("Sneha",207,"CSE")
func6("Mahee",153,"CSE")
func6("Aaloo",123,"CST")

def func6(collegename="GIET",name,rollno,branch): #not valid as we are having name as the 2nd argument but we are passing it as 1st argument.
    print(name,rollno,branch,collegename)

func7("Aditya",199,"CSE")
func7("Sneha",207,"CSE")
func7("Mahee",153,"CSE")
func7("Aaloo",123,"CST")

def func6(name,rollno,branch="CSE",collegename="GIET"):
    print(name,rollno,branch,collegename)

func8("Aditya",199,"CSE")
func8("Sneha",207)
func8("Mahee",153)
func8("Aaloo",123,"CST")


def func9(*var):
    for i in var:
        print(i,end=' ')
func9(10,20)
print()
func9(10,20,30)
print()
func9(10,20,30,40)
print()


def add(*var): #tuple=
    sum=0
    for i in var:
        sum+=i
    return sum
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))


def mul(n1,n2,n3):
    if(n1==7):
        print(n2*n3)
    elif(n2==7):
        print(n3)
    elif(n3==7):
        print("-1")
    else:
        print(n1*n2*n3)

mul(1,5,3)
mul(1,5,7)
mul(1,5,9)


#Converting the owned currency to the currency required in INR
def currency(INR,own):
    India=1
    if (own=="Euro"):
        India=INR*0.01417
    elif (own=="British Pound"):
        India=INR*0.0100
    elif(own=="Australian Dollar"):
        India=INR*0.02140
    elif(own=="Canadian Dollar"):
        India=INR*0.02027
    else:
        print(-1)
    return India

INR=int(input("Enter the amount you want to give in INR: "))
own=input("Enter the currency you are having: ")
print("The amount in your currency is: ",currency(INR,own))



#Calculating the total amount to be paid for the tickets after discounts
def ticket(adult,child):
    sum=adult*37550+child*12516.66
    tax=sum*(7/100)
    total=sum+tax
    discount=total*(10/100)
    total_amount=total-discount
    return total_amount

adult=int(input("Enter total number of adults: "))
child=int(input("Enter total number of children: "))
print("Total amount to be paid: ",ticket(adult,child))

#Different approach
def ticket(adult,child):
    total=(((adult*37550)+(child*12516.66)*1.07)*0.90)
    return total

adult=int(input("Enter total number of adults: "))
child=int(input("Enter total number of children: "))
print("Total amount to be paid: ",ticket(adult,child))



#Calculating the number of 5 and 1 rupee coins to be given to make a particular total sum
def amount(five,one):
    possible_amount=5*five+one
    if(to_be_made<=possible_amount):
        to_pay_5=int(to_be_made/5)
        to_pay_1=to_be_made%5
    else:
        print(-1)
    return (to_pay_5,to_pay_1)

five=int(input("Total number of 5 rupee coin: "))
one=int(input("Total number of 1 rupee coin: "))
to_be_made=int(input("Total amount to be paid: "))
print("Number of 5 rupee coin and Number of 1 rupee
coin are",amount(five,one),"respectively")








        
    













    




