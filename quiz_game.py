questions = ['What is the capital of India?',
             'What is my name?',
             'What is my age?',
             'Who are you?']

options = [
    'A. Delhi B. Kerala C. Mumbai',
    'A. Alan B. Aman C. Anil',
    'A. 19 B. 34 C. 21',
    'A. Bitch B. Lucy C. Ken'
]

# Loop through each question and its corresponding options
for question_no in range(len(questions)):
    print(questions[question_no])  # Print the question
    print(options[question_no])    # Print the corresponding options
    print()  # Add a newline for better readability
