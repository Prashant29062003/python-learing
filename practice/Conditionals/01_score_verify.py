# 1. score verify

score = 185

if score >= 101:
    print(f"Verify your score (must be 0 to 100), your score {score}")
    exit()

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'C'
else:
    grade = 'F'

print(grade)