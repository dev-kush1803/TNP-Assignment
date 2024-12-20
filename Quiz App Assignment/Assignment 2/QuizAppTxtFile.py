import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

DATA_FILE = "data.txt"

def read_data():
    """Reads data from the data file."""
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r") as file:
        lines = file.readlines()

    users = {}
    for line in lines:
        parts = line.strip().split(",")
        if len(parts) == 5:
            enrollment, name, password, sem, branch = parts
            users[enrollment] = {
                "name": name,
                "pass": password,
                "sem": sem,
                "branch": branch
            }
    return users

def write_data(users):
    """Writes user data to the data file."""
    with open(DATA_FILE, "w") as file:
        for enrollment, details in users.items():
            file.write(",".join([enrollment, details["name"], details["pass"], details["sem"], details["branch"]]) + "\n")

def main():
    users = read_data()
    action = input("\nAre you registered? (yes/no): ").lower()
    if action == 'yes':
        login(users)
    elif action == 'no':
        if register(users):
            login(users)
    else:
        print("\nPlease enter 'yes' or 'no'.")

def register(users):
    enrollment = input("\nEnter unique Enrollment no.: ")
    if enrollment in users:
        print("\nEnrollment no. already registered. Please login.\n")
        login(users)
    else:
        users[enrollment] = {
            "name": input("Enter your name: "),
            "pass": input("Enter your password: "),
            "sem": input("Enter your semester: "),
            "branch": input("Enter your branch: ")
        }
        write_data(users)
        print("\nRegistration successful. You can now login.\n")
        login(users)

def login(users):
    print("Enter details to Log In\n")
    enrollment = input("Enter your Enrollment no.: ")
    password = input("Enter your password: ")
    if enrollment in users and users[enrollment]["pass"] == password:
        print(f"\nWelcome, {users[enrollment]['name']}! Login successful.\n")
    else:
        print("\nInvalid Enrollment no. or password. Please register first.\n")
        register(users)

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
