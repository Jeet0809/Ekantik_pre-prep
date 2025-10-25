# students = ["Jeet", "Omkar", "Ninad" , "Kaivalya"]

# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])

# houses = ["Malad", "Borivali", "Virar", "Mira-Road"]

# Dict
students = {"Jeet": "Malad", 
            "Omkar": "Borivali",
            "Ninad": "Virar",
            "Kaivalya": "Mira Road"}


# print(students["Jeet"])
# print(students["Kaivalya"])


# iterates over keys and not values
# for student in students: 
#     print(student)
    
# keys and values
for student in students:
    print(student , students[student], sep=", ")
    
    