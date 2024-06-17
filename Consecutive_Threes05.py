#Design a function that takes a list of integers as input
#And returns true is if it contains two consecutive 3's

#Using for statement to iterate through the list
#we are checking pairs of adjacent elements hence we start from index 0 to index length of list -2

def consecutive_threes(list):
    for i in range(len(list)-1):
        #check if adjacent numbers equal to 3
        if list[i]==3 and list[i+1]==3:
            return True
        return False
    
print(consecutive_threes([1,2,3,4]))
print(consecutive_threes([3,3,3,4]))