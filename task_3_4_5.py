from main_code import calculate_average, assign_grade

# Exercise 3: Workflow
marks = [70, 80, 90]
avg = calculate_average(marks)
grade = assign_grade(avg)

print("Average:", avg)
print("Grade:", grade)

# Exercise 4: Error Check
try:
    avg = "80"   # wrong type
    grade = assign_grade(avg)
except Exception as e:
    print("Error Found:", e)