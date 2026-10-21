
class QuizApplication:

    def __init__(self):
        self.score = 0
        self.correct = 0
        self.incorrect = 0

    # Question 1
    def question1(self):
        print("\n1. Which keyword defines a function in Python?")
        print("A. function")
        print("B. def")
        print("C. define")
        print("D. fun")

        self.check_answer("B")

    # Question 2
    def question2(self):
        print("\n2. Which data type stores key-value pairs?")
        print("A. List")
        print("B. Tuple")
        print("C. Dictionary")
        print("D. Set")

        self.check_answer("C")

    # Question 3
    def question3(self):
        print("\n3. Which symbol is used for comments in Python?")
        print("A. //")
        print("B. #")
        print("C. @")
        print("D. $")

        self.check_answer("B")

    # Question 4
    def question4(self):
        print("\n4. Which method adds an item to a list?")
        print("A. add()")
        print("B. append()")
        print("C. push()")
        print("D. insert_end()")

        self.check_answer("B")

    # Question 5
    def question5(self):
        print("\n5. Which loop iterates over a sequence?")
        print("A. if")
        print("B. else")
        print("C. for")
        print("D. def")

        self.check_answer("C")

    # Check the user's answer
    def check_answer(self, correct_answer):
        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        while answer not in ["A", "B", "C", "D"]:
            print("Invalid choice! Enter A, B, C, or D.")
            answer = input("Enter your answer: ").strip().upper()

        if answer == correct_answer:
            print("Correct answer!")
            self.score += 1
            self.correct += 1
        else:
            print("Incorrect answer!")
            print("Correct answer is:", correct_answer)
            self.incorrect += 1

    # Display final results
    def show_results(self):
        total = 5
        percentage = (self.score / total) * 100

        print("\n===== QUIZ RESULTS =====")
        print("Total Questions:", total)
        print("Correct Answers:", self.correct)
        print("Incorrect Answers:", self.incorrect)
        print(f"Final Score: {percentage:.0f}%")

        if percentage == 100:
            print("Excellent! Perfect score!")
        elif percentage >= 80:
            print("Great job!")
        elif percentage >= 60:
            print("Good job!")
        else:
            print("Keep practising!")

    # Start all questions
    def start_quiz(self):
        self.score = 0
        self.correct = 0
        self.incorrect = 0

        self.question1()
        self.question2()
        self.question3()
        self.question4()
        self.question5()

        self.show_results()

    # Main menu
    def menu(self):
        while True:
            print("\n===== QUIZ APPLICATION =====")
            print("1. Start Quiz")
            print("2. View Instructions")
            print("3. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                while True:
                    self.start_quiz()

                    replay = input(
                        "\nWould you like to play again? (yes/no): "
                    ).strip().lower()

                    if replay in ["yes", "y"]:
                        continue
                    elif replay in ["no", "n"]:
                        break
                    else:
                        print("Please enter yes or no.")
                        continue

                    break

            elif choice == "2":
                print("\nInstructions:")
                print("1. Answer all 5 questions.")
                print("2. Enter A, B, C, or D.")
                print("3. Each correct answer gets 1 point.")

            elif choice == "3":
                print("Thank you for playing!")
                break

            else:
                print("Invalid menu choice!")


# Create object and run application
quiz = QuizApplication()
quiz.menu()
