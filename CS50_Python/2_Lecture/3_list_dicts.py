students = [
    {"name": "Jeet", "place": "Malad", "status": "Studying"} , 
    {"name": "Omkar", "place": "Pune", "status": "Job"} , 
    {"name": "Ninad", "place": "Virar", "status": "Job"} ,
    {"name": "Kaivalya", "place": "Mira Road", "status": "Studying"} , 
]


for student in students :
    print(student["name"] , student["place"] , student["status"], sep=", ")