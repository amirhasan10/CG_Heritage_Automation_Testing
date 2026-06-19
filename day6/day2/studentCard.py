# Real-life example: Student Report Card

# Constants — values that don't change
PASS_MARKS    = 35
TOTAL_MARKS   = 100

# Descriptive variable names
student_name  = "Rohit Sharma"
maths_marks   = 78
science_marks = 82
english_marks = 69

# Calculated variable
average_marks = (maths_marks + science_marks + english_marks) / 3
is_passed     = average_marks >= PASS_MARKS

print(student_name, "| Average:", round(average_marks, 2), "| Passed:", is_passed)