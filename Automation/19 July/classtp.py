class sar:
    even=lambda x:print("Its even") if x%2==0 else print("odd") 
    def add(a,b):
        ans=a+b 
        return ans

def main():
    x=int(input("Enter the number : "))
    y=int(input("Enthr the number : "))
    y=17
    ret1=sar.add(x,y)
    ret2=sar.even(x)
    #print(ret1)
if __name__ == "__main__":
    main()