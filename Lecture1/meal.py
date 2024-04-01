"""
 implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. 
 Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. 
 For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.
 
To the corresponding number of hours as a . For instance, given a like (i.e., 7 hours and 30 minutes), 
should return (i.e., 7.5 hours)convertmaintimestrfloattime"7:30"convert7.5.
"""


def main():

    input_time=input("What time is it? ")
    out_time =convert(input_time)

    if 7 <= out_time <= 8:
        print("breakfast time")
    elif 12<= out_time <= 13:
        print("lunch time")
    elif 18<= out_time <= 19:
        print("dinner time")


def convert(time):
   
   time = time.split(":")
   time = int(time[0])+ float(int(time[1])/60) 
   return time
   
if __name__ == "__main__":
    main()





    