#Telusko code
#https://www.youtube.com/watch?v=Vca808JTbI8
#Using a Function

#First see the swapping varibale programs

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range (i):
            if nums[j]>nums[j+1]:
               temp = nums[j]                           #Swaaping method  using 3 varaibels
               nums[j] = nums[j+1]                            #Assisgnment only
               nums[j+1]= temp

nums= [5,3,8,6,7,2]
sort(nums)
print(nums)