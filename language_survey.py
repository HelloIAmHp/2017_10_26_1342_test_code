from survey import AnonymousSurvey

question = "What language did you first learn?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at anytime to quit.\n")
while True:
    response = input("Language: ")
    if 'q' == response:
        break
    my_survey.store_response(response)

print("Thank you for help")
my_survey.show_results()
