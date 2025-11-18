def validate_input(n):
    if n<0 or n>9999:
        return False
    str_n=str(n)
    if len(str_n)<=4:
        add_zero= 4-len(str_n)
        N=str(0)*add_zero+str_n
        allsame=["0000","1111","2222","3333","4444","5555","6666","7777","8888","9999"]
        if N in allsame:
            return False
        else:
            return True

def sort_digits(n,b):
    str_n=str(n)
    if len(str_n)<=4:
        add_zero= 4-len(str_n)
        N=str(0)*add_zero+str_n
        digits=list(N)
        alist=[]
        if b==1:
            while digits != []:
                max_num=digits[0]
                for num in digits:
                    if num>max_num:
                        max_num=num
                alist=alist+[max_num]
                digits.remove(max_num)
        elif b==0:
            while digits != []:
                min_num=digits[0]
                for num in digits:
                    if num<min_num:
                        min_num=num
                alist=alist+[min_num]
                digits.remove(min_num)
        result_str="".join(alist)
        return int(result_str)

def main():
    while True:
        N=int(input("enter a four-digit number:"))
        if validate_input(N)==True:
            break
        else:
            N=int(input("enter a four-digit number:"))
    N_old=None
    N_new=N
    iterations=0
    while N_new != N_old:
        N_old=N_new
        a_ascending=sort_digits(N_old,0)
        b_desending=sort_digits(N_old,1)
        N_new=b_desending-a_ascending
        iterations=iterations+1
        print("iterations times:",iterations)
        print("the number is:", N_new)
    str_N=str(N_new)
    if len(str_N)<=4:
        add_zero= 4-len(str_N)
        N_str=str(0)*add_zero+str_N
    print("the end result is:",N_str)
    print("the first digit of final number is:",N_str[0])
    print("the third digit of final number is:",N_str[2])
    print("total iterations:",iterations)
main()

"""
Docstring:
TEST CASE 1: 104
  iteration times | number
                1 | 4086
                2 | 8172
                3 | 7443
                4 | 3996
                5 | 6264
                6 | 4176
                7 | 6174
                8 | 6174
The end result is: 6174
The first digit of final number is: 6
The third digit of final number is: 7
Total iterations: 8

TEST CASE 2: 0011
  iteration times | number
                1 | 1089
                2 | 9621
                3 | 8352
                4 | 6174
                5 | 6174
The end result is: 6174
The first digit of final number is: 6
The third digit of final number is: 7
Total iterations: 5

TEST CASE 3: 1234
  iteration times | number
                1 | 3087
                2 | 8352
                3 | 6174
                4 | 6174
The end result is: 6174
The first digit of final number is: 6
The third digit of final number is: 7
Total iterations: 4

TEST CASE 4:1738
  iteration times | number
                1 | 7353
                2 | 4176
                3 | 6174
                4 | 6174
The end result is: 6174
The first digit of final number is: 6
The third digit of final number is: 7
Total iterations: 4

TEST CASE 5: 12
  iteration times | number
                1 | 2088
                2 | 8532
                3 | 6174
                4 | 6174
The end result is: 6174
The first digit of final number is: 6
The third digit of final number is: 7
Total iterations: 4

"""