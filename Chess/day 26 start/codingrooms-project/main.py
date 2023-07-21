

# Write your code above 👆



file1= open("Chess/day 26 start/codingrooms-project/file1.txt")
file2= open("Chess/day 26 start/codingrooms-project/file2.txt")

list1= []
list2= []

data1= file1.readlines()
for num in data1:
    list1.append(int(num))

data2= file2.readlines()
for num in data2:
    list2.append(int(num))

new_list= [n for n in list1 if n in list2]

print(new_list)
