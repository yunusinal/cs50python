"""
implement a program that prompts the user for a str of text and then outputs that same text but 
with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""
word = input("Input:")
for i in word:
 
    if i in ["a","e","u","o","i","A","E","U","O","I"]:
        word=word.replace(i,"")
        
print(word)
