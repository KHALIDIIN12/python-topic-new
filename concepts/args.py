def  greet(*args):
    for arg in args:
        print("Name is",arg)
        

def sum(*args):
    ans=0
    for n in args:
        # print(f"{ans}={ans}+{n}")
        print(ans,"=",ans,"+",n)
        ans=ans+n
    
    print("Ans is ",ans)
    return ans

sum(100,50,20,30,150,200,700,900)
# sum(4,1,2)