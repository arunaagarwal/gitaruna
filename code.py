count1=0
count2=0
str =input("enter open closing bracket")
print(str)
check = True;
for j in range(len(str)):
 if str[j] is '[':
    count1=count1+1

 if str[j] is ']':

    count1 = count1 - 1;
 if (count1 <= 0 and j != len(str) - 1):

     print ("NOT OKK")
     check = False;
     break;

if count1!=0 and check :
    print("NOT OK")
elif check :
    print("OK")