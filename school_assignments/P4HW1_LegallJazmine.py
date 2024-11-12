# Jazmine Legall
# 10/30/2024
# P4HW1
'''
Description:
Building on P2HW2 assignment, program will use a loop and display score average
as well as letter grade
'''

# Ask user to enter for number of scores they would like to enter
num_scores = int(input('How many scores do you want to enter? '))

# Initializing an empty list to store valid scores
scores = []

# Loop to collect scores from user
for i in range(num_scores):
# Loop untila valid score is entered
    while True:
        score = float(input(f"Enter score #{i +1}: "))

        if 0 <= score <= 100:
            # append adds the valid score is entered
            scores.append(score)
            break
        else:
            print('\nINVALID Score entered!!!!')
            print('Score should be between 0 and 100')
            score = float(input(f"Enter score #{i + 1} again: "))
# Restarts the Loop
            if 0 <= score <= 100:
                scores.append(score)
                break
    
# Calculates lowest score
lowest_score = min(scores)
# Modify list without lowest score
scores_mod = [score for score in scores if score != lowest_score]

# Calculates the average of the modified list
if scores_mod:
    average_score = sum(scores_mod) / len(scores_mod)
else:
    average_score = 0

# Determind the letter grade based on average score
if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display the results
print('\n------------Results------------')
print(f"{'Lowest Score   :'} {lowest_score:.1f}")
print(f"{'Modified List  :'} {scores_mod}")
print(f"{'Scores Average :'} {average_score:.2f}")
print(f"{'Grade          :'} {grade}")
print('---------------------------------')