import random
import numpy as np

empno=int(input("Number of employees:  "))
file2=open("output.txt","a")
file2.write("The goodies selected for distribution are: \n")
#since the input has only 10 gifts , the gifts alloted to emplyees must be 
# repeated if the number of employee is more than 10.
#Randomly choosing gifts for each emloyee from the ist of gifts. 
if empno>10:
    myword=np.random.choice(open("input.txt").read().split('\n'), size=empno, replace=True)
else:
    myword=np.random.choice(open("input.txt").read().split('\n'), size=empno, replace=False)

nums=[]
for j in range(empno):
    ran=str(myword[j])
    print(myword[j])
    file2.write(ran)
    file2.write("\n")
lenof=len(myword)
for i in range(lenof):
    m=myword[i]
    n=m.split(": ")
    nm=int(n[1])
    nums.append(int(nm))

#print(nums)
# calculating the difference between max and min
maxim=int(max(nums))
mini=int(min(nums))
diff=int(maxim-mini)
#print(diff)
file2.write("\n")
file2.write("And the difference between the chosen goodie with highest price and the lowest price is  ")
file2.write(str(diff))
file2.write("\n")