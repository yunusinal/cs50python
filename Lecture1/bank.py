ans = input("Greeting:")

if ans.strip().lower().startswith("hello"):
    print ("$0")
elif ans.strip().lower().startswith("h") and not ans.strip().lower().startswith("hello") :
    print("$20")
else:
    print("$100")



