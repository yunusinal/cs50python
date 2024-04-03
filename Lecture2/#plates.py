"""
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; 
AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
"""

def main():
    plate = input("Plate: ")
    plate=plate.upper()

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(inp):
    tmp=0
    number=["0","1","2","3","4","5","6","7","8","9"]
    punc=[".",","," ",";",":","/","|","-","_"]

    if 2<=len(inp)<=6:
        if inp.isdigit():
            return False
        for i in inp:
            if i in number:
                if i=="0"and tmp==0:
                    return False 
                x = inp.split(i,1)
                if x[1].isdigit():
                    return True
                
            elif i in punc:
                return False    
        return True
    else:
        return False            



main()