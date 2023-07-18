#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("/Users/air/Desktop/100daysofpython/Mail Merge Project Start/Input/Names/invited_names.txt") as all_names:
    names= all_names.readlines()


with open("/Users/air/Desktop/100daysofpython/Mail Merge Project Start/Input/Letters/starting_letter.txt") as start_letter:

    letter= start_letter.read()
    for name in names:
        x= letter.replace("[name]",name.strip())
        new_file= "sample"+"_"+name.strip()
        newfilee= open("Mail Merge Project Start/Output/ReadyToSend/"+new_file, mode="w")
        newfilee.write(x)
      