import sys
number = int(input("enter the number to check if the number is happy"))
seq=[]
def check(num):   
    strSum = str(num)
    while(len(strSum) != 1):
        sqrSum=0
        for i in range(len(strSum)):
            sqrSum=sqrSum+int(strSum[i])*int(strSum[i])
        if (sqrSum==1):
            print("happy")
            print(seq)
            sys.exit()
        else:
            seq.append(sqrSum)
            print(sqrSum)
            check(sqrSum)
check(number)