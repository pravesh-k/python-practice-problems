## Problem from hacker rank website, titled "Nested Lists".

# Problem statement: 
'''
Given the names and grades for each student in a class of n students, store 
them in a nested list and print the name(s) of any student(s) having the 
second lowest grade.

Note: If there are multiple students with the second lowest grade, order 
their names alphabetically and print each name on a new line.
'''
# Sample IO:
# input:
'''
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
'''
# Output
'''
Berry
Harry
'''
# Constraints
'''
2 <= n <= 5
There will always be one or more students having the second lowest grade.
'''

# Code:

def second_lowest_grade(grades):
    
    grades = dict(grades)
    second_lowest_score = sorted(set(grades.values()))[1]
    second_low_scorers = [each for each in grades if grades[each] == second_lowest_score]
    return sorted(second_low_scorers)


if __name__ == '__main__':
    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name, score])

    print('\n'.join(second_lowest_grade(grades)))