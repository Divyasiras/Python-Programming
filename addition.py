def Addition(A,B):
    Result = 0
    Result = A+B
    return Result

def main():
    no1 = 0
    no2 = 0
    Ans = 0

    print("Enter First number :")
    no1 = int(input())

    print("Enter Second number :")
    no2 = int(input())

    Ans = Addition(no1,no2)

    print("Addition is :",Ans)

main()
