import pandas


student_dict= {"student": ["Angela", "Lily", "Simon"],
               "score": [24, 42 ,44]}



student_frame= pandas.DataFrame(student_dict)

for (index, row) in student_frame.iterrows():
    if row.student=="Angela":
        print(row.score)

