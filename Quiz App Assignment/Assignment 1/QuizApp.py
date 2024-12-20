import os

def clear_console():
    # Check the OS and use the appropriate command
    os.system('cls' if os.name == 'nt' else 'clear')

users = {}# dictionary was made to store users info

def main(): 
    action = input("\nAre you registered? (yes/no): ").lower()
    if action == 'yes':
        login()
    elif action == 'no':
        if register():
            login()
    else:
        print("\nPlease enter 'yes' or 'no'.")

def register(): #take input from user and check in dictionary.
    enrollment = input("\nEnter unique Enrollment no.: ")
    if enrollment in users: # check user is already enrolled or not
        print("\nEnrollment no. already registered. Please login.\n")
        login()
    else : # store details of users with enrollment a
        users[enrollment] = {
        "name": input("Enter your name: "),
        "password": input("Enter your password: "),
        "sem": input("Enter your semester: "),
        "branch": input("Enter your branch: ")
    } 
    print("\nRegistration successful You can now login.\n")
    login()

def login():
    print("Enter details to Log In\n")
    enrollment = input("Enter your Enrollment no.: ")
    pas = input("Enter your password: ")
    if enrollment in users and users[enrollment]["password"] == pas:
        print(f"\nWelcome , {users[enrollment]['name']} Login successful.\n")
    else:
        print("\nInvalid Enrollment no. or password. Please Register First\n")
        register()

main() #main func. call to run prog.

print(f"\nWelcome to Quiz \n")

# Quiz data for each section
subjects = {
    "DSA": [
        {
            "question": "Which data structure is used for LIFO operations?",
            "options": ["a) Queue", "b) Stack", "c) Array", "d) Linked List"],
            "answer": "b"
        },
        {
            "question": "Which of the following has O(1) time complexity for insertion?",
            "options": ["a) Queue", "b) Array", "c) Stack", "d) Linked List"],
            "answer": "c"
        },
        {
            "question": "Which algorithm is used for finding the shortest path in graphs?",
            "options": ["a) DFS", "b) BFS", "c) Dijkstra", "d) Kruskal"],
            "answer": "c"
        },
        {
            "question": "Which data structure uses nodes and pointers?",
            "options": ["a) Stack", "b) Array", "c) Linked List", "d) Heap"],
            "answer": "c"
        },
        {
            "question": "What is the time complexity of binary search?",
            "options": ["a) O(n)", "b) O(log n)", "c) O(n^2)", "d) O(1)"],
            "answer": "b"
        }
    ],
    "DBMS": [
        {
            "question": "What does SQL stand for?",
            "options": ["a) Structured Query Language", "b) Simple Query Language", "c) Strong Query Language", "d) Special Query Language"],
            "answer": "a"
        },
        {
            "question": "What type of key uniquely identifies a record in a table?",
            "options": ["a) Foreign key", "b) Primary key", "c) Composite key", "d) Candidate key"],
            "answer": "b"
        },
        {
            "question": "Which SQL command is used to remove all records from a table?",
            "options": ["a) DELETE", "b) DROP", "c) TRUNCATE", "d) REMOVE"],
            "answer": "c"
        },
        {
            "question": "Which normal form removes partial dependencies?",
            "options": ["a) 1NF", "b) 2NF", "c) 3NF", "d) BCNF"],
            "answer": "b"
        },
        {
            "question": "What does ACID stand for in DBMS?",
            "options": ["a) Atomicity, Consistency, Isolation, Durability", "b) Addition, Consistency, Isolation, Dependency", "c) Atomicity, Concurrency, Integrity, Dependency", "d) All Consistent, Independent, Dependable"],
            "answer": "a"
        }
    ],
    "Python": [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["a) def", "b) function", "c) lambda", "d) define"],
            "answer": "a"
        },
        {
            "question": "What is the output of 2 ** 3 in Python?",
            "options": ["a) 5", "b) 6", "c) 8", "d) 9"],
            "answer": "c"
        },
        {
            "question": "What is the correct syntax to import a module in Python?",
            "options": ["a) import(module)", "b) import module", "c) include module", "d) using module"],
            "answer": "b"
        },
        {
            "question": "Which of the following is a mutable data type in Python?",
            "options": ["a) Tuple", "b) List", "c) String", "d) Integer"],
            "answer": "b"
        },
        {
            "question": "What does len() function do in Python?",
            "options": ["a) Returns the number of arguments", "b) Returns the type of data", "c) Returns the length of an object", "d) None of the above"],
            "answer": "c"
        }
    ]
}

def start(section): 
    questions = subjects[section]
    score = 0
    print(f"\nStarting the {section} Quiz...\n")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (a/b/c/d): ").lower()

        if answer == q["answer"]: # Check answer 
            print("Correct!\n")
            score += 1
        else:
            print("Wrong! The correct answer is", q["answer"] + ".\n") 

    print(f"Your score for the {section} Quiz is {score} out of {len(questions)}.\n") # Display score 

# Main program
def quiz():

    while True:
        # Display section choices
        print("Please choose a section:")
        for i, section in enumerate(subjects.keys()):
            print(f"{i + 1}) {section}")

        # Get user choice
        try:
            choice = int(input("Enter the number of the section you want to play: "))
            section_names = list(subjects.keys())
            if 1 <= choice <= len(section_names):
                selected_section = section_names[choice - 1]
                start(selected_section)
            else:
                print("Invalid choice. Please select a valid section.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Ask if the user wants to play again or exit
        retry = input("Do you want to try another section? (yes/no): ").lower()
        if retry == 'yes':
            clear_console()
            quiz()
        else:
            print("Thank you for playing! Goodbye!")
            clear_console()
            main()

# Run the quiz program
quiz()
