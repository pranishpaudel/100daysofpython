import random
names= ["Maduri", "Agnel", "homeris", "gingasin", "Merotin"]

new_dict= {student:random.randint(1,100) for student in names}

print(new_dict)


passed= {student:score for (student, score) in new_dict.items() if score>=60}

print(passed)