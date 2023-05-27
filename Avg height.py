# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

print (student_heights)
c=0

totalh=0
for height in student_heights:
    totalh= totalh+height
    c+=1

avg= totalh/c
print("Average height is "+ str(avg))





