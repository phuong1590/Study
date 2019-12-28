print("Hello!")
print("How are you today?") #string
#Here's how you can create and store data in a variable,you can call out variable between plus signs in a sentence.
name = "Ryan" #You can also store a string variable by using phrase,we can also concatenate string variables by using a single plus sign
age = "18" #I will explain why I'm putting 18 as a string value here later
print("Hi I am " + name + " and I'm " + age + " years old.\n")
name = "Cat" #You can update and modify the date stored inside a variable whenever you want,which is really cool
name1 = "Kien"
print ("We are " + name + " and " + name1 + ",we are pile of shits!")
#There are functions that help you to change your variables
phrase = "Kien and Cat always bail all the time so that's why they are horrible!"
print (phrase.upper() + "Fuck them!!!") #If you use the .islower() function,the console will appear as false,since they are uppered by the upper function
print (len(phrase)) #Get the length of the string variable
print (name1[0]) #Use square brackets and enter the index number of the string variable to know the letter at that index position
print (name1.index("e")) #Get to know the index number of the e letter or where the text start inside name1
print (phrase.replace("Kien","Quang")) #Replace an old element with new one
num = 69 #You can change a number variable into a string variable
print(str(num)) #So you can print our numbers,like this
num1 = -69
print(abs(num)) #You can find the absolute of a number with abs function
print(pow(num,2)) #69^69
print(max(69,num1)) #min function does the opposite
print(round(6.9)) #Basic rounding rule,x.<5=>x,x.>5=>x+1
from math import * #Import math functions from math module,there are tons of math functions so feel free to search them on the internet,I have listed the most commonly used functions already so you will have to explore online
print(floor(6.9)) #The result will be 6,as we are flooring the number,the ceil function does the opposite
print(sqrt(81)) #Gives you the square root of a number
#How to get inputs and access those input value as variables
username = input("Please enter your username:")
password = input("Please type in your password:")
print("Welcome to Ryan's first python application,your username is: " + username + "!")
print("And your password is: " + password + ".")
#Python is gonna assume the input that the user put in as a string value,so in order to make a calculator,we need to convert them to number variable by using function(int function for integer numbers/float function for decimal numbers).If not,the answer appeared to the console would be 5+5=55
user_num = input("Enter the first number:")
user_num1 = input("Enter the second number:")
result = float(user_num)+float(user_num1)#user_num + user_num1 will print out the wrong answer,since we didn't convert the data type back to number
print(result)
close_friends = ["Cat" , "Kien" , "Hieu" , "Quang" , "Khanh" , "Hoan" , "Khang"] #In Python,we call these lists,not arrays
print(close_friends[4:7]) #Starts at 4th position and grab the element that's inside 4-7,which means 4,5,6
not_really_close_friends = ["Khai" , "Dang" , "PAnh" , "Dat"] #If somehow they become your close and nice friends,you can add them to the close_friends list using extend function
#For example:close_friends.extend(not_really_close_friends).You can also add a single element using append function.You can use the reverse function to...reverse the order of the element inside a list.
#For example:not_really_close_friends.append("Thanh").Thanh will be added at the end of the list.But let's say you wanna add an element in a particular order/index position,use the insert function
#For example:not_really_close_friends.insert(3,"Tien").If I wanna remove some of them because they are nothing but some judgemental piece of shit,I will use the remove function
#For example:close_friends.remove(0:3).So now Cat,Kien,Hieu have been removed because they are pieces of shit.To remove the last element of the list,use pop function.
#To find an element,use index function,it will tell you the index number of the element if it's in the list.
#You can also count how many time the element appear,using count function.To put the elements in alphabetical/numberical order,use the sort function.
#You can copy a list by creating another list and that list will have the same exact elements in the first list,since we copied it,using copy function.FE:friends = close_friends.copy





