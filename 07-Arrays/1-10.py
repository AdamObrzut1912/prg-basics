###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results)

# calculates the number of correct answers
correct_answers = 0
inncorrect_answers = 0
for answer in test_results:
    if answer == True:
      correct_answers += 1
    else:
        inncorrect_answers += 1


# calculates the percentage of correct answers
percentageCorrectAnwsers = (correct_answers / question_number)*100

print('TEST STATISTICS')
print('===============')
print(f"Number of questions: {question_number} ")
print(f"Number of correct answers: {correct_answers}")
print(f"Number of inncorrect anwsers: {inncorrect_answers}")
print(f"Percentage of correct number: {round(percentageCorrectAnwsers,2)}")
...