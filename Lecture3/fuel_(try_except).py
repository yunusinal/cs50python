
def main():
 
    crr= fuel()
    if crr<1:
        print("E")
    elif crr > 99:
        print("F")

    else:
        print(f"{crr}%")        

def fuel():
    while True:
        fuel=input("Fraction: ")
        try:
            x,y= fuel.split("/",1)
            x,y=int(x),int(y)
            if round((x/y)*100)>100:
                pass
            else:
                return round((x/y)*100)
        except (ZeroDivisionError,ValueError):
           pass 
        
main()