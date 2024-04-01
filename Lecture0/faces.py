"""
implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 
and any :( converted to 🙁 . All other text should be returned unchanged.
"""
def main():
    txt = str(input(""))
    txtconverted=convert(txt)
    print(txtconverted)

def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text

main()


