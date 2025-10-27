def main():
    
# ============================================
# TOPIC 2: Variables in Python
# ============================================
    
    name = "Jeet Pimpale"
    age = 22 
    semester = 7 
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Semester: {semester}")
    print()

# ============================================
# TOPIC 3: Data Types in Python
# ============================================

    marks = 85 
    print(f"Marks: {marks}, Type: {type(marks)}")
    
    cgpa = 8.15
    print(f"CGPA: {cgpa}, Type: {type(cgpa)}")

    college = "Atharva College"
    print(f"College: {college}, Type: {type(college)}")

    is_student = True
    print(f"Is Student: {is_student}, Type: {type(is_student)}")
    print()
    
# ============================================
# TOPIC 4: Sum of a & b (Simple Arithmetic)
# ============================================
    print("=== Arithmetic Operations ===")
    a = 10
    b = 20
    sum_result = a + b
    print(f"a = {a}, b = {b}")
    print(f"Sum: {sum_result}")
    print()

# ============================================
# TOPIC 5: Comments in Python
# ============================================
# This is a single-line comment (Java: // comment)

    """
    This is a multi-line comment
    (Java: /* comment */)
    Used for documentation
    """
    
# ============================================
# TOPIC 6: Input from User
# ============================================
    a = input("What's your name\n").strip().title()
    print(f"his name is {a}")
    
# ============================================
# TOPIC 10: Type Conversion
# ============================================

    a = "100"
    print(f"Number: {a}, Type: {type(a)}")
    b = int(a)
    print(f"Number: {b}, Type: {type(b)}")
    
    age_int = 23
    age_str = str(age_int)
    print(f"Integer {age_int} → String '{age_str}'")
    print()
    
    
if __name__ == "__main__":
    main()