def matrix_multiplication(A,B):
    row_A=len(A)
    col_A=len(A[0])
    col_B=len(B[0])
    AB=[]
    for row_AB in range(0,row_A):
        row=[]
        for col_AB in range(0,col_B):
              row.append(0)
        AB.append(row)
              
    for rowA in range(0,row_A):
        for colB in range(0,col_B):
            for colA in range(0,col_A):
                    AB[rowA][colB]+= A[rowA][colA]*B[colA][colB]
    return AB

def trace(A):
    n=len(A)
    A_sum=0
    for i in range(0,n):
         A_sum+=A[i][i]
    return A_sum

def main():
    Aa=[
          [0,1,1,0,0,0],
          [1,0,1,1,1,0],
          [1,1,0,0,1,1],
          [0,1,0,0,1,0],
          [0,1,1,1,0,1],
          [0,0,1,0,1,0]
     ]

    Ab=[
          [0,1,1,0,0],
          [1,0,1,1,0],
          [1,1,0,0,1],
          [0,1,0,0,1],
          [0,0,1,1,0]
     ]

    Ac=[
          [0,1,1,1,1],
          [1,0,1,1,1],
          [1,1,0,1,1],
          [1,1,1,0,1],
          [1,1,1,1,0]
     ]

    Aa_2=matrix_multiplication(Aa,Aa)
    Ab_2=matrix_multiplication(Ab,Ab)
    Ac_2=matrix_multiplication(Ac,Ac)

    Aa_3=matrix_multiplication(Aa_2,Aa)
    Ab_3=matrix_multiplication(Ab_2,Ab)
    Ac_3=matrix_multiplication(Ac_2,Ac)

    print("The value of trace(Aa**3) is:",trace(Aa_3)/6)
    print("The value of trace(Ab**3) is:",trace(Ab_3)/6)
    print("The value of trace(Ac**3) is:",trace(Ac_3)/6)

    triangleAa=4
    triangleAb=1
    triangleAc=10
    if trace(Aa_3)/6 > triangleAa:
        print("trace(Aa**3)/6 > three-edge triangles in the graph 3.1(a)")
    elif trace(Aa_3)/6 == triangleAa:
        print("trace(Aa**3)/6 = three-edge triangles in the graph 3.1(a)")
    else:
        print("trace(Aa**3)/6 < three-edge triangles in the graph 3.1(a)")

    if trace(Ab_3)/6 > triangleAb:
        print("trace(Ab**3)/6 > three-edge triangles in the graph 3.1(b)")
    elif trace(Ab_3)/6 == triangleAb:
        print("trace(Ab**3)/6 = three-edge triangles in the graph 3.1(b)")
    else:
        print("trace(Ab**3)/6 < three-edge triangles in the graph 3.1(b)")

    if trace(Ac_3)/6 > triangleAc:
        print("trace(Ac**3)/6 > three-edge triangles in the graph 3.1(c)")
    elif trace(Ac_3)/6 == triangleAc:
        print("trace(Ac**3)/6 = three-edge triangles in the graph 3.1(c)")
    else:
        print("trace(Ac**3)/6 < three-edge triangles in the graph 3.1(c)")
    
main()