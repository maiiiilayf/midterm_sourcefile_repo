
scores = [85, 72, 91, 64, 78]

def get_grade_remark(score):
    if score >=90:
        return "Excellent"
    elif score >=80:
        return "Very Good"
    elif score >=75:
        return "Good"
    else:
        return None


def get_status (score):
    return "Passed" if score >=75 else "Failed"

print ("Student Scores:")
for score in scores:
    print (score)
print ()

total_score = 0
passed_count  = 0
failed_count = 0

for i, score in enumerate(scores, start=1):
    status = get_status(score)
    remark = get_grade_remark(score)


    if status == "Passed":
        print (f"Student {i}: {score} - {remark} - {status}")
        passed_count += 1
    else: 
        print (f"student {i}: {score} - {status}")
        failed_count += 1

    total_score += score


average_score = total_score / len(scores)
highest_score = max(scores)
lowest_score = min(scores)
 

if average_score == int(average_score):
    average_display = int(average_score)
else:
    average_display = round(average_score, 2)
 

print()
print(f"Total Score: {total_score}")
print(f"Average Score: {average_display}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
 
