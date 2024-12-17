import random
charlist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
spllist=['!','`','@','#','$','%','^','&','*','(',')','-','_','+','=','/','[',']','{','}',';',':',':','"','<','>','/',',','.']
numlist=['1','2','3','4','5','6','7','8','9','0']
no_char=int(input("Enter the number of characters:"))
no_spl=int(input("Enter the number of special char:"))
no_num=int(input("Enter the total num :"))
password=""
for i in range(no_char):
    password+=random.choice(charlist)
for i in range(no_spl):
    password+=random.choice(spllist)
for i in range(no_num):
    password+=random.choice(numlist)
password_list=[]
for i in password:
    password_list.append(i)
random.shuffle(password_list)
p=""
for i in password_list:
    p+=i
print(p)