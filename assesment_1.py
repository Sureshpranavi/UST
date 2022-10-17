
#"1. Write a function to take input from user in days and print it in years, month and days input - 397, output - 1 year , 1 month , 1 day"
print("\n\n")
def cal(days):
    years=days//365
    months=(days-years*365)//30
    dayss=(day-years*365-months*30)
    print("number of years=",years)
    print("number of months=",months)
    print("number of days=",dayss)

day=int(input("enter how many days="))
cal(day)




#2. Generate fibnoacci series for 1 to 20")
print("\n")
num=int(input("enetr tha value="))
i=0
fv=0
sv=1
while(i<num):
    if(i<=1):
        res=i
    else:
        res=fv+sv
        fv=sv
        sv=res
    print(res)
    i=i+1




#3. Create a program to play RPS Game")
print("\n")

print("*"*50)
print("\tWelcome all to RPS Game")
print("*"*50)
player1=input("enter the player name 1 = ")
player2=input("enter the player name 2 = ")
print( "Select your options : \n Rock\n Scissor\n Paper\n")
p1_choice=input("enter p1 the option =")
p2_choice=input("enter p2 the option =")

if(p1_choice=="Rock" and p2_choice=="Scissor"):
    print(player1,"win the game with choice of ",p1_choice)
elif(p1_choice=="Rock" and p2_choice=="Paper"):
    print(player2,"win the game with choice of ",p2_choice)
elif(p1_choice=="Scissor" and p2_choice=="Paper"):
    print(player1,"win the game with choice of ",p1_choice)
elif(p1_choice==p2_choice):
    print("Game was Tie")


#4. Write functions to calculate and display grosssalary and netsalary of an employee after getting input as basicsalary")
print("\n")
def allow(basic_sal):
    hra=int(input("enter the HRA allownaces in terms of percentage="))
    da=int(input("enter the DA allownaces in terms of percentage="))
    ta=int(input("enter the TA allownaces in terms of percentage="))
    res1=(   (basic_sal/hra) +  (basic_sal/da) + (basic_sal/ta)  )
    return res1
    
def dedt(basic_sal):
    if (basic_sal>8000):
        profit_tax=basic_sal-200
    else:
        profit_tax=basic_sal-150
    pf=basic_sal/12
    insurance=basic_sal/8
    res2=profit_tax-pf-insurance
    return res2


emp_name=input("enter the emplye name=")
basic_sal=int(input("enter the employee basic salary="))
allowances=allow(basic_sal)
deductions=dedt(basic_sal)
gross_sal=basic_sal+allowances
net_sal=gross_sal-deductions
print("\n")
print("*"*50)
print("Month salary of employee : ",emp_name)

print("*"*50)
print("\n")
print("Total allownces: ",allowances)
print("Total deductions: ",deductions)
print("Employee Gross salary ",gross_sal)
print("Employee Net salary ",net_sal)
print("\n")
print("*"*50)



#5. For the given string-->calculate the number of vowels individually i.e number of a, e, i , o and u calculate total number of consonants")
print("\n")
para="""Python is a widely used general-purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed
by the Python Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their
concepts in fewer lines of code"""


vowels=['a','A','e','E','i','I','o','O','u','U']
punc_chr=[',','.',' ','&']
vowels_count=0
consonants_count=0
consonants=0
for i in para:
    if i in vowels:
        vowels_count+=1
for j  in para:
    if j not in vowels:
        if j not in punc_chr:
            consonants_count+=1
        else:
            consonants+=1
        
print("numbers of charesctres in paragraph :",len(para))
print("number of vovels in paragraph : ",vowels_count)
print("number of consonants in paragraph : ",consonants_count)
print("number of spcial symbols in paragraph : ",consonants)





#6. Ask user a input string and check if the entered string is palindrome. Ex: Input NitiN -> o/p palindrome")
print("\n")

word=input("enter any word/string : ")
rev=word[::-1]
if(rev==word):
    print("its a palindrome")
else:
    print("its not a paindrome")





#7. Ask user to input email and check if the email is in valid form or not. Ex: it should contain single '@', '.', @or.shouldn't be in 1st position")
print("\n")

email=input("enter your email address : ")
if email[0]=="@":
    print("email should not starts with @ symbol...!")
elif ('@' and '.') in email:
    print("its a valid email adress")
else:
    print("invalid email id")




#8. Write a pay computation program with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).


def computepay(hours,rate):
    days=int(input("enter how many days you planned for trip : "))
    total_hours=days*hours
    pay=total_hours*rate
    return pay

def hotel_cost(nights):
    per_night=140
    toatl_cost_night=per_night*nights
    return toatl_cost_night

def plane_ride_cost(city):
    if city=="Charlotte":
        return 183
    elif city=="Tampa":
        return 220
    if city=="Pittsburgh":
        return 222
    if city=="Los Angeles":
        return 475


def rental_car_cost(days):
    per_day=40
    total_cost=days*per_day
    if days>7:
        return total_cost-50
    elif days>3:
        return total_cost-20


def trip_cost(city,days):
    return hotel_price+city_cost+car_cost

hours=int(input("enter how many hours per day: "))
rate=int(input("enter the rate per kilometer : "))
hour_cost=computepay(hours,rate)


nights=int(input("enter the how many nights : "))
hotel_price=hotel_cost(nights)
print("the taotal cost for nights : ", hotel_price)
print("\n")

print("listed tourist places are : \n\tCharlotte\n \tTampa\n  \tPittsburgh\n  \tLos Angeles\n")
city=input("enter the city name:")
city_cost=plane_ride_cost(city)
print("price of code with respect to the cities :",city_cost)
print("\n")
 
days=int(input("enter the number of days :"))
car_cost=rental_car_cost(days)
print("total cost for total days=",car_cost)
print("\n")


total_cost=trip_cost(city,days)
print("total cost for the trip :",total_cost+hour_cost)
print("\n")





#9. Create a shopping cart for the below bakery_items using dictionary or list

bakery_items = {"Bread":40, "Butter":120, "Jam":200, "Cheese":220, "Crossiant":60}



print("*"*80)
print("\twelcome to the UST_campus Style Bakery...")
print("*"*80)
print("\n")
print("""Enter choice :
            1. View the bakery items
            2. Add the item into the cart
            3. View the cart
            4. Update item in the cart
            5. Remove item from the cart
            6. Checkout and generate bill""")
ch=int(input("enter your option : "))
if ch==1:
    bakery_items = {"Bread":40, "Butter":120, "Jam":200, "Cheese":220, "Crossiant":60}
    for item,price in bakery_items.items():
        print(item,"--->",price)

elif ch==2:
    bakery_items = {"Bread":40, "Butter":120, "Jam":200, "Cheese":220, "Crossiant":60}
    for item,price in bakery_items.items():
        print(item,"--->",price)
    cart=[]
    item=input("enter the items u want:")
    cart.append(item)
    print("Item added Successfully")

elif ch==3:
    print("*"*50)
    print("Chart boX")
    print("*"*50)
    bakery_items = {"Bread":40, "Butter":120, "Jam":200, "Cheese":220, "Crossiant":60}
    for item,price in bakery_items.items():
        print(item,"--->",price)
    print("\n")
    print("You have oredered : ",cart)

elif ch==4:
    cart.update(input("enter the item name if u want to change the item name : "))

elif ch==5:
    cart.remove(input("enter item name which one you want to remove:"))

elif ch==6:
    print("\n")
    print("You have oredered : ",cart)
    print("Thanks for visiting...")
    print("***********  visit again  ************")







































        














