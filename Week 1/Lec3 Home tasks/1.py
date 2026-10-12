"""
1. Given a 3x3 nested list representing test scores of 3 students across 3 subjects:
scores = [[85, 92, 78], [79, 95, 88], [90, 82, 94]]

Perform the following tasks:
- Extract and print the scores of the 2nd student.
- Extract the diagonal scores (1st subject of Student 1, 2nd subject of Student 2, 3rd subject of Student 3) into a new list 'diagonal_scores'.
- Append a 4th student's scores [88, 76, 91] to the matrix.
- Remove the lowest score from the 1st student's list using min() and list remove().
- Combine and flatten the last two students' score lists into 'combined_scores' using slicing and concatenation.
- Reverse 'combined_scores' in-place and sort it in descending order.
- Calculate and display the total sum, highest score, lowest score, and average of 'combined_scores' using formatted f-strings.
"""

scores = [
    [85, 92, 78],
    [79, 95, 88],
    [90, 82, 94]
]

student_2_scores = scores[1]
print(f"2nd Student Scores: {student_2_scores}")

diagonal_scores = [scores[0][0], scores[1][1], scores[2][2]]
print(f"Diagonal Scores: {diagonal_scores}")

scores.append([88, 76, 91])
print(f"Updated Matrix (after adding 4th student): {scores}")

lowest_score_s1 = min(scores[0])
scores[0].remove(lowest_score_s1)
print(f"1st Student Scores (after removing lowest {lowest_score_s1}): {scores[0]}")

combined_scores = scores[-2] + scores[-1]
print(f"Combined Scores of last 2 students: {combined_scores}")

combined_scores.reverse()
print(f"Reversed Combined Scores: {combined_scores}")
combined_scores.sort(reverse=True)
print(f"Sorted Descending Combined Scores: {combined_scores}")

total_sum = sum(combined_scores)
highest = max(combined_scores)
lowest = min(combined_scores)
average = total_sum / len(combined_scores)

print(f"Statistics -> Total: {total_sum}, Highest: {highest}, Lowest: {lowest}, Average: {average:.2f}")
