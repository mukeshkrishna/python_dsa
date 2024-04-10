

def TOH(n,A,B,C):
    if n >0:
        TOH(n-1,A,C,B)
        print(f"({A},{C})")
        TOH(n-1,B,A,C)

TOH(3,1,2,3)