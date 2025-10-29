## Grading Scale ##
# 90–100 → A
# 80–89 → B
# 70–79 → C
# below 70 → F

# Exam score input
exam_score = int(input("Enter your exam score (0-100): "))


if exam_score >= 90 and exam_score <= 100:
    print("You earned an A")
elif exam_score >= 80 and exam_score <= 89:
    print("You earned an B")
elif exam_score >= 70 and exam_score <= 79:
    print("You earned an C")
elif exam_score >= 0 and exam_score < 70:
    print("You earned an F")
else:
    print("Invalid score. Please enter a number between 0 and 100.")
