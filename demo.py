#list automatically has index value 
card_no="5610591081018250"# its a string not a list so therefore it is difficult to assign the indexes
odd_sum=0
even_sum=0
double_list=[]
number=list(card_no) 
for (idx,val) in enumerate(number):  # enumerate is use to get the indexes, we have access to both now indexes and value 
    if idx % 2  !=0:      #checking for odd number
        odd_sum+=int(val)
                                      
    else:  # this is an even number
      double_list.append(int(val)*2)
    
#converting the list into a string 
double_string=""
for x in double_list:
    double_string+=str(x)   #double string is storing the doubled of value we got

#converting the string back to list 
double_list=list(double_string)

for x in double_list:
    even_sum+=int(x)
    
     
net_sum=odd_sum+even_sum
if net_sum%10==0:
    print('valid card')
else:
    print('invalid card')
