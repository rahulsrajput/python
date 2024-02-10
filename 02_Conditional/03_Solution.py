Grade = ''
score = int(input('Enter a Score: '))
if score >= 101:
    print("Please Verify Your Grade Again")
    exit()

if score >= 90:
    Grade = 'A'
elif score >= 80:
    Grade = 'B'
elif score >= 70:
    Grade = 'C'
elif score >= 60:
    Grade = 'D'
else:
    Grade = 'Fail'

print(f'Grade: {Grade}')