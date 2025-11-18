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
    max_iterations=0
    for N in range(1,9999):
        N_old=None
        N_new=N
        iterations=0
        while N_new != N_old:
            N_old=N_new
            a_ascending=sort_digits(N_old,0)
            b_desending=sort_digits(N_old,1)
            N_new=b_desending-a_ascending
            iterations=iterations+1
        if iterations>max_iterations:
            max_iterations=iterations
    print("the maximum number of Main Loop iterations is",max_iterations)
main()