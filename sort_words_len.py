## Problem on sorting based on a key function.

# Problem statement: 
'''
Given a sentence as string, rearrange the words of string in a manner such that
word with the minimum length appears at the beginning and subsequently words with
length greater than previous word, thus keeping the lengthiest word at the last.
'''
# Sample IO:
# Input:
'''
sentence = 'Hi this language is python'
'''
# Output
'''
sorted_sentence = 'Hi is this python language'
'''

# Code:

sentence = 'Hi this language is python'
sorted_sentence = sorted(sentence.split(), key=len)
print(' '.join(sorted_sentence))