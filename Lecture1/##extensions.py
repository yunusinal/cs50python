"""
Implement a program that prompts the user for the name of a file and then
outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
.gif .jpg .jpeg .png .pdf .txt  .zip
If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
"""


def get_media_type(filename):
    suffix = filename.lower().split('.')  # Get the lowercase suffix of the filename and split from . into a list
    suffix= suffix[-1].strip() # If there are multiple extensions, consider only the last one


    """if '.' in suffix:
        suffix = suffix.split('.')[-1]  # If there are multiple extensions, consider only the last one
        print(suffix)
    """

    if suffix in ['gif', 'jpg', 'jpeg', 'png', ]:
        if suffix == 'jpg':
            suffix = 'jpeg'  # jpeg is equivalent to jpg
        return f"image/{suffix}"

    elif suffix in ['pdf','zip']:
        return f"application/{suffix}"

    elif suffix == "txt":
        return "text/plain"

    else:
        return 'application/octet-stream'



def main():
    fname = input("File Name: ")
    media_type = get_media_type(fname)
    print( media_type)

main()





