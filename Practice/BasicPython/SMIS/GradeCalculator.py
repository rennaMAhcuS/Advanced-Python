MathMarks = 0
EnglishMarks = 0
SocialMarks = 0
ScienceMarks = 0
SecondLangMarks = 0
Percentage = 0


# Grade Calculator function.
def grade(percentage):
    if percentage > 85:
        return 'A'
    elif 75 < percentage < 85:
        return 'B'
    elif 50 < percentage < 75:
        return 'C'
    elif 30 < percentage < 50:
        return 'D'
    else:
        return "Reappear for the course/exam."


while True:
    Option = input('''---------------------
Enter I for Entering/Updating your Marks
Enter P for displaying your Percentage
Enter G for displaying your Grade
>> ''')

    if Option == 'I':
        # Accepting Marks (or Updating) from user.
        MathMarks = int(input("Enter your marks in Math: "))
        EnglishMarks = int(input("Enter your marks in English: "))
        SocialMarks = int(input("Enter your marks in Social: "))
        ScienceMarks = int(input("Enter your marks in Science: "))
        SecondLangMarks = int(input("Enter your marks in your Second Language: "))

        # Calculating/Updating Percentage:
        Percentage = (MathMarks + EnglishMarks + SocialMarks + ScienceMarks + SecondLangMarks) / 5

    elif Option == 'P':
        print(Percentage)

    elif Option == 'G':
        print(grade(Percentage))
    else:
        print("Wrong input given. Give proper input.")
